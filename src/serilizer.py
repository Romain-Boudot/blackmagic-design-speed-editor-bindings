import json


def serialize(obj, path):
    file = open(path, 'w')
    dict_as_string = json.dumps(obj, skipkeys=True)
    file.write(dict_as_string)
    file.close()


def deserialize(path):
    open(path, 'a+').close()
    file = open(path, 'r')
    dict_as_string = file.read() or '{}'
    obj = json.loads(dict_as_string)
    file.close()
    return obj
