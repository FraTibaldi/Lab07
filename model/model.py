from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

        self._Libri = self.get_libri_filtrati("nessun filtro", "nessun filtro")
        self._biblioteche = self.get_biblioteche()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        id_biblio = None
        if biblioteca != "nessun filtro":
            id_biblio = int(biblioteca)
        if genere == "nessun filtro":
            lista_libri_filtrati = self._libro_dao.filtra_libri_per_genere_e_biblioteca(None, id_biblio)
        else:
            lista_libri_filtrati = self._libro_dao.filtra_libri_per_genere_e_biblioteca(genere, id_biblio)
        return lista_libri_filtrati

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.leggi_generi_da_db()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.leggi_biblioteche_da_db()
