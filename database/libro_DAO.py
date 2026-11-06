from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def leggi_tutti_i_libri(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            raise ConnectionError("Errore nella connessione al database")
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM libro")
        result = []
        for row in cursor:
            libro = Libro(*row)
            result.append(libro)
        cursor.close()
        cnx.close()
        return result