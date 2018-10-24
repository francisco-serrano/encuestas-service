from flask import Flask, jsonify
from EncuestasDatabase import EncuestasDatabase
import json

app = Flask(__name__)
db = EncuestasDatabase('encuestas.db')


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(mensaje='que onda bigoton')


@app.route('/get_encuestas', methods=['GET'])
def get_encuestas():
    rows = db.find_all()
    column_names = db.get_columns()

    aux = list(map(lambda row: dict(zip(column_names, row)), rows))

    return json.dumps(aux, ensure_ascii=False).encode('utf-8')


if __name__ == '__main__':
    app.run()
