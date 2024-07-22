import threading
import time
from flask_socketio import SocketIO
from cache.data_cache import DataCache
import torch


class LibSvmDataQueue:
    def __init__(self, socketio: SocketIO, data_cache: DataCache, max_nfields: int):
        self.socketio = socketio
        self.data_cache = data_cache
        self.max_nfields = max_nfields
        self.thread = threading.Thread(target=self._background_thread)
        self.thread.daemon = True
        self.thread.start()

    def batch_preprocess(self, data: str):
        data = data.split('\n')

        sample_lines = 0
        ids_list = []
        values_list = []
        labels_list = []

        for line in data:
            if not line:
                continue  # skip empty lines
            columns = line.strip().split(' ')
            pairs = [list(map(int, pair.split(':'))) for pair in columns[1:]]
            ids, values = zip(*pairs) if pairs else ([], [])
            ids_list.append(ids)
            values_list.append(values)
            labels_list.append(float(columns[0]))
            sample_lines += 1

        nsamples = sample_lines
        feat_id = torch.zeros((nsamples, self.max_nfields), dtype=torch.long)
        feat_value = torch.zeros((nsamples, self.max_nfields), dtype=torch.float)
        y = torch.tensor(labels_list, dtype=torch.float)

        for i in range(nsamples):
            try:
                feat_id[i, :len(ids_list[i])] = torch.tensor(ids_list[i], dtype=torch.long)
                feat_value[i, :len(values_list[i])] = torch.tensor(values_list[i], dtype=torch.float)
            except Exception as e:
                print(f'Incorrect data format in sample {i}! Error: {e}')
        print(f'# {nsamples} data samples loaded...')

        return {'id': feat_id, 'value': feat_value, 'y': y}

    def add(self, key: str, data: str):
        batch_data = self.batch_preprocess(data)
        if self.data_cache.set(key, batch_data):
            return True
        else:
            return False

    def _background_thread(self):
        print("[LibSvmDataQueue] thread started...")
        while True:
            key = self.data_cache.is_full()
            if key:
                print(f"[LibSvmDataQueue] fetching data for {key}...")
                self.socketio.emit('request_data', {'key': key})
            time.sleep(0.1)
