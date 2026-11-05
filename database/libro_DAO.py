from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def leggi_generi_da_db(self): # seleziona i vari generi dei libri
        #db = DBConnect()
        cnx = DBConnect.get_connection()
        if cnx is not None:
            query = ("SELECT DISTINCT genere FROM libro")
            cursor = cnx.cursor()
            cursor.execute(query)

            result = []
            for row in cursor:
                genere = row[0]
                result.append(genere)
            cursor.close()
            cnx.close()
            return result
        else:
            print(f"Errore nella connessione al database")

    def filtra_libri_per_genere_e_biblioteca(self, genere:str, id_biblioteca:int):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            query = ("SELECT * FROM libro "
                     "WHERE genere = COALESCE(%s, genere) "
                     "AND id_biblioteca = COALESCE(%s, id_biblioteca)")
            cursor = cnx.cursor()
            cursor.execute(query, (genere, id_biblioteca))

            result = []
            for row in cursor:
                libro = Libro(*row)
                result.append(libro)

            cursor.close()
            cnx.close()
            return result
        else:
            print(f"Errore nella connessione al database")

