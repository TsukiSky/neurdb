from app.handlers.data_dispatcher import LibSvmDataDispatcher
from flask import current_app, g
from dataloader.steam_libsvm_dataset import StreamingDataSet


def before_request_func():
    print("before_request executing!")
    g.data_dispatcher = LibSvmDataDispatcher()


def after_request_func(response):
    print("after_request executing!")
    g.data_dispatcher.stop()
    g.data_dispatcher = None


def before_execute(dataset_name: str, data_key: str, client_id: str) -> bool:
    """
    Start LibSvmDataDispatcher and create StreamingDataSet
    :param dataset_name:
    :param data_key: train, infernece
    :param client_id: socket client id
    :return:
    """
    print("before_execute executing!")
    # get the data cache for that dataset
    data_cache = current_app.config['data_cache']
    if dataset_name not in data_cache:
        return False
    _cache = data_cache[dataset_name]

    client = current_app.config['clients'][client_id]
    print(f"[socket]: set task for client {client_id}...")

    # register it as global variables
    # todo: multiple request share same dispatcher, add refercne count
    dispatchers = current_app.config['dispatchers']
    if dataset_name not in dispatchers:
        dispatchers[dataset_name] = g.data_dispatcher

    # assign the data dispaccher
    g.data_dispatcher.set_task(_cache, client)
    if not g.data_dispatcher.start():
        return False

    # create dataset
    data = StreamingDataSet(_cache, data_key=data_key)
    g.data_loader = data
    return True
