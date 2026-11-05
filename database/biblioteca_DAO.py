from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def leggi_biblioteche_da_db(self):
        # db = DBConnect()
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("connection established")

            query = ("SELECT * FROM biblioteca")
            cursor = cnx.cursor()
            cursor.execute(query)

            result = []
            for row in cursor:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)

            cursor.close()
            cnx.close()
            return result
        else:
            print(f"Errore nella connessione al database")