from flask import Flask, jsonify
from EncuestasDatabase import EncuestasDatabase

app = Flask(__name__)
db = EncuestasDatabase('encuestas.db')


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(mensaje='que onda bigoton')


@app.route('/get_encuestas', methods=['GET'])
def get_encuestas():
    rows = db.find_all()
    column_names = db.get_columns()

    return jsonify(list(map(lambda row: dict(zip(column_names, row)), rows)))


if __name__ == '__main__':
    app.run()
