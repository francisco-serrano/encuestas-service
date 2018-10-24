import sqlite3
import pandas as pd


class EncuestasDatabase:

    def __init__(self, db_dir):
        self.connection = sqlite3.connect(db_dir, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.query_consulta = 'select * from encuestas;'
        self.query_consulta_columnas = 'pragma table_info(encuestas)'

    def find_all(self):
        self.cursor.execute(self.query_consulta)
        return self.cursor.fetchall()

    def get_columns(self):
        return list(map(lambda x: x[1], self.cursor.execute(self.query_consulta_columnas)))

    def load_classification_into_db(self, csv_file, table_name):
        df = pd.read_csv(csv_file, sep='\t')
        df.to_sql(table_name, self.connection, if_exists='replace')
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
