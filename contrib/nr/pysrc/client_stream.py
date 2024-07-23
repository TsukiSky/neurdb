import requests
import socketio

# Define the server address and port
SERVER_URL = "http://localhost:8090"

# Global dataset string
dataset = """0 204:1 4798:1 5041:1 5046:1 5053:1 5055:1 5058:1 5060:1 5073:1 5183:1\n
1 42:1 1572:1 5042:1 5047:1 5053:1 5055:1 5058:1 5060:1 5070:1 5150:1\n
1 282:1 2552:1 5044:1 5052:1 5054:1 5055:1 5058:1 5060:1 5072:1 5244:1\n
0 215:1 1402:1 5039:1 5051:1 5054:1 5055:1 5058:1 5063:1 5069:1 5149:1\n
0 346:1 2423:1 5043:1 5051:1 5054:1 5055:1 5058:1 5063:1 5088:1 5149:1\n
0 391:1 2081:1 5039:1 5050:1 5054:1 5055:1 5058:1 5060:1 5088:1 5268:1\n
0 164:1 3515:1 5042:1 5052:1 5053:1 5055:1 5058:1 5062:1 5074:1 5149:1\n
0 4:1 1177:1 5044:1 5049:1 5054:1 5057:1 5058:1 5060:1 5071:1 5152:1"""

# Socket.IO client
sio = socketio.Client()


# Define the event handler for the 'response' event
@sio.on('response')
def on_response(data):
    print(f"Server response: {data}")


# Define the event handler for the 'request_data' event
@sio.on('request_data')
def on_request_data(data):
    key = data.get('key')
    print(f"Received request_data for key: {key}")
    # Handle the request data logic here
    # For example, you might fetch data from a file or database and send it back to the server
    sio.emit('receive_db_data', {'dataset_name': key, 'dataset': dataset})


# Connect to the Socket.IO server
sio.connect(SERVER_URL)


def test_train_endpoint(batch_size, model_name, dataset_name):
    url = f"{SERVER_URL}/train"
    data = {
        'batch_size': batch_size,
        'model_name': model_name,
        'dataset_name': dataset_name
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(f"Response from {url}:")
        response_json = response.json()
        print(response_json)
        return response_json.get('model_id')
    else:
        print(f"Failed to get a valid response from {url}. Status code: {response.status_code}")
        return None


def test_inference_endpoint(model_name, model_id):
    url = f"{SERVER_URL}/inference"
    data = {
        'model_name': model_name,
        'model_id': model_id
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(f"Response from {url}:")
        print(response.json())
    else:
        print(f"Failed to get a valid response from {url}. Status code: {response.status_code}")
        print("Response content:")
        print(response.content)


def test_dataset_profiling(dataset_name, nfeat, nfield):
    profiling_data = {
        'dataset_name': dataset_name,
        'nfeat': nfeat,
        'nfield': nfield
    }
    sio.emit('dataset_profiling', profiling_data)


def test_receive_db_data(dataset_name, dataset):
    db_data = {
        'dataset_name': dataset_name,
        'dataset': dataset
    }
    sio.emit('receive_db_data', db_data)


if __name__ == "__main__":
    # Test dataset profiling via Socket.IO
    test_dataset_profiling('frappe', 5500, 10)

    # Test sending the libsvm data to train endpoint
    _batch_size = 32  # Example batch size
    _model_name = 'armnet'  # Example model name
    _dataset_name = 'frappe'

    _model_id = test_train_endpoint(_batch_size, _model_name, _dataset_name)

    if _model_id:
        _model_id = 1
    test_inference_endpoint(_model_name, int(_model_id))

    # Test sending dataset data via Socket.IO
    test_receive_db_data('frappe', dataset)

    # Wait for responses and then disconnect
    sio.sleep(2)
    sio.disconnect()
