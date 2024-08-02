import ast
import json

from logger.logger import logger
from flask import current_app, request
from flask_socketio import SocketIO, Namespace, emit, disconnect
from cache import DataCache, LibSvmDataDispatcher

socketio = SocketIO(
    ping_timeout=30, ping_interval=5, logger=False, engineio_logger=False
)


class NRDataManager(Namespace):
    """
    NRDataManager register some socket endpoints
    """

    def on_connect(self):
        """
        Handle client connection event.
        Store the client session ID and notify the client.
        """
        sid = request.sid
        current_app.config["clients"][sid] = sid

        logger.info(f"Client connected: {sid}")
        _current_clients = current_app.config["clients"]
        logger.debug(f"Current registered clients: {_current_clients}")
        emit("connection", {"sid": sid}, room=sid)

    # todo: this cannot connected by c client.
    def on_disconnect(self):
        """
        Handle client disconnection event.
        Remove the client session ID and associated data from the server.
        """
        try:
            sid = request.sid
            logger.info(
                f"[socket: Discinnect & Recording] : {sid} Client disconnected: "
            )
            current_app.config["clients"].pop(sid, None)
            current_app.config["data_cache"].remove(sid)

            for dataset_name, ele in current_app.config["dispatchers"].get(sid).items():
                print(
                    f"[socket: Discinnect & Recording] dataset {dataset_name}, sid {sid} time usage {ele.total_preprocessing_time}"
                )
            current_app.config["dispatchers"].remove(sid)

            current_app.config["dispatchers"].remove(sid)
        except Exception as e:
            logger.debug(f"Error {e}")

    def on_dataset_init(self, data: str):
        """
        Handle dataset initialization event.
        1. Create data cache for a specific dataset.
        2. Create dispatcher and start it.
        :param data: Dictionary containing dataset information.
        :return:
        """
        # str to dict
        data = ast.literal_eval(data)

        socket_id = request.sid
        dataset_name = data["dataset_name"]
        nfeat = data["nfeat"]
        nfield = data["nfield"]
        total_batch_num = data["nbatch"]
        cache_num = data["cache_num"]

        logger.info(f"[socket: on_dataset_init] on_dataset_init, receive: {data}")

        # 1. Create data cache if not exist
        data_cache = current_app.config["data_cache"]
        if not data_cache.contains(socket_id, dataset_name):
            _cache = DataCache(
                dataset_name=dataset_name,
                total_batch_num=total_batch_num,
                maxsize=cache_num,
            )
            _cache.dataset_statistics = (nfeat, nfield)
            data_cache.add(socket_id, dataset_name, _cache)
        else:
            _cache = data_cache.get(socket_id, dataset_name)

        # 2. Create dispatcher if not exist
        dispatchers = current_app.config["dispatchers"]
        if not dispatchers.contains(socket_id, dataset_name):
            _data_dispatcher = LibSvmDataDispatcher()
            dispatchers.add(socket_id, dataset_name, _data_dispatcher)
            _data_dispatcher.bound_client_to_cache(_cache, socket_id)
            _data_dispatcher.start(emit_request_data)

        emit("dataset_init", {"message": "Done"})

    def on_batch_data(self, data: str):
        """
        Handle the event of receiving database data.
        Add the received data to the appropriate cache queue.
        :param data: Dictionary containing dataset information and the actual data.
        """
        socket_id = request.sid
        data = json.loads(data)

        dataset_name = data["dataset_name"]
        dataset = data["dataset"]

        logger.debug(
            f"[socket: on_batch_data]: {socket_id} receive_db_data name {dataset_name} and data {dataset[:10]}..."
        )

        # Check if dispatcher is launched for this dataset
        dispatchers = current_app.config["dispatchers"]
        if not dispatchers.contains(socket_id, dataset_name):
            logger.debug(
                f"dispatchers is not initialized for dataset {dataset_name} and client {socket_id}, "
                f"wait for train/inference/finetune request"
            )
            emit(
                "response",
                {
                    "message": f"dispatchers is not initialized for dataset {dataset_name} and client {socket_id}, "
                    f"wait for train/inference/finetune request"
                },
            )
        else:
            # logger.debug(f"dispatchers is initialized for dataset {dataset_name} and client {socket_id}")
            dispatcher = dispatchers.get(socket_id, dataset_name)
            if not dispatcher:
                logger.debug("[socket: on_batch_data]: dispatcher is not initialized")
                emit("response", {"message": "dispatcher is not initialized"})
            else:
                dispatcher.add(dataset)
                emit("response", {"message": "Data received and added to queue!"})

    def force_disconnect(self):
        """
        Forcefully disconnect a client.
        :param sid: Session ID of the client to disconnect.
        """
        sid = request.sid
        current_app.config["clients"].pop(sid, None)
        current_app.config["data_cache"].remove(sid)

        for dataset_name, ele in current_app.config["dispatchers"].get(sid).items():
            print(
                f"[socket: Discinnect & Recording] dataset {dataset_name}, sid {sid} time usage {ele.total_preprocessing_time}"
            )
        current_app.config["dispatchers"].remove(sid)

        logger.info(
            f"[socket: Discinnect & Recording] Forcefully disconnecting client: {sid}"
        )
        disconnect(sid)


def emit_request_data(client_id: str):
    """
    Emit request_data event to clients.
    :param client_id: The client ID to send the request to.
    :return:
    """

    socketio.emit("request_data", {}, to=client_id)
