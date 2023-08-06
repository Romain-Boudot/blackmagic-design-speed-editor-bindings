import json

from flask import Flask, request, send_from_directory
from flask_cors import CORS
from multiprocessing import Process, Manager

from bmd import SpeedEditor
from handler import SpeedEditorHandler
from serilizer import serialize, deserialize

app = Flask(__name__)
CORS(app)

bindings = {}


@app.route('/api/keys')
def get_all_keys():
    return json.dumps(bindings.copy())


@app.route('/api/keys/<string:code>', methods=['POST'])
def set_key(code):
    bindings[code] = request.form.get('binding')
    print(bindings.copy())
    serialize(bindings.copy(), 'bindings.json')
    return {'code': code, 'binding': request.form.get('binding')}


@app.route('/<path:path>', methods=['POST'])
def static_files(path):
    return send_from_directory('dist', path)


def run_davinci(_bindings):
    se = SpeedEditor()
    se.authenticate()
    se.set_handler(SpeedEditorHandler(se, _bindings))
    while True:
        se.poll()


if __name__ == '__main__':
    with Manager() as manager:
        bindings = manager.dict(deserialize('bindings.json'))
        resolve = Process(target=run_davinci, args=(bindings,))

        resolve.start()
        app.run(host='127.0.0.1', port=5005)
        resolve.join()
