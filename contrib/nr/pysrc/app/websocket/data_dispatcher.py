from flask_socketio import emit
from flask import current_app
from app.websocket import socketio
from cache.data_cache import DataCache


@socketio.on('dataset_profiling')
def dataset_profiling(data: dict):
    """
    Create data cache for a specific dataset.
    :param data: Dictionary containing dataset information.
    :return:
    """
    data_cache = current_app.config['data_cache']
    dataset_name = data['dataset_name']
    nfeat = data['nfeat']
    nfield = data['nfield']

    # create datacache
    _cache = DataCache()
    _cache.dataset_statistics = (nfeat, nfield)
    data_cache[dataset_name] = _cache

    emit('response', {'message': 'Done'})


@socketio.on('receive_db_data')
def receive_db_data(data: dict):
    """
    Receive data from the database UDFs.
    :param data: Dictionary containing dataset name and data.
    :return:
    """
    dataset_name = data['dataset_name']
    dataset = data['dataset']
    _cache = current_app.config['data_cache'][dataset_name]

    if _cache.add(dataset):
        emit('response', {'message': 'Data received and added to queue!'})
    else:
        emit('response', {'message': 'Queue is full, data not added.'})


def emit_request_data(key: str):
    """
    Emit request_data event to clients
    :param key:
    :return:
    """
    socketio.emit('request_data', {'key': key})
