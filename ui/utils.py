import json

def load_thread_data(json_path="data/batch_output.json"):
    with open(json_path, "r") as f:
        return json.load(f)

def get_thread_by_id(data, thread_id):
    return next((t for t in data if t["thread_id"] == thread_id), None)
