from EncuestasDatabase import EncuestasDatabase

db = EncuestasDatabase('encuestas.db')
db.load_classification_into_db('data-encuestas.csv', 'encuestas')
db.close_connection()
