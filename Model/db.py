import sqlite3
import pandas as pd

class Database:
    db_name = "Model/DataBase/db.sqlite"
    def __init__(self):
        """Constructor del objeto Database
        """        
        try:
            self.conn = sqlite3.connect(Database.db_name)
            self.cursor = self.conn.cursor()
        
        #Excepcion si la base de datos no se ha podido conectar
        except sqlite3.OperationalError:
            print("No se puede conectar a la base de datos")
        
        
    def insert_dataframe(self, df:pd.DataFrame, table_name: str):
        """Función para insertar un Dataframe en la base de datos

        Args:
            df (pd.DataFrame): DataFrame a insertar
            table_name (str): Nombre de la tabla
        """        
        try:
            df.to_sql(table_name,con=self.conn, if_exists='replace', index=False)
        # Si no ha podido insertarlo salta una excepcion
        except sqlite3.Error:
            raise sqlite3.Error("Error: No se han podido insertar los datos")


    def close(self):
        if self.conn:
            self.conn.close()