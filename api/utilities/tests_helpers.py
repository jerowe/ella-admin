import json


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def load_bytes(path):
    file = open(path, "rb")
    data = file.read()
    file.close()

    return data

def load_fixture(path):
    with open(path, 'r') as f:
        return f.read()