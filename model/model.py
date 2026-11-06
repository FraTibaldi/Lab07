from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''
# da migliorare con la apertura unica del dao
class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()
        # creo liste e dizionari che mi servono per memorizzare i dati
        self._listaLibri = []
        self._dictLibri = {}
        self._listaBiblioteche = []
        # chiamo le funzioni che popolano le liste delle biblioteche e dei libri
        self._listaLibri = self._libro_dao.leggi_tutti_i_libri()
        self._listaBiblioteche = self.get_biblioteche()

        for libro in self._listaLibri:
            if libro.genere not in self._dictLibri:
                self._dictLibri[libro.genere] = [libro]
            else:
                self._dictLibri[libro.genere].append(libro)
    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        if biblioteca == "nessun filtro" and genere == "nessun filtro":
            return self._listaLibri
        elif biblioteca == "nessun filtro" and genere != "nessun filtro":
            return self._dictLibri[genere]
        elif biblioteca != "nessun filtro" and genere == "nessun filtro":
            lista_libri = []
            for genere in self._dictLibri:
                for libro in self._dictLibri[genere]:
                    if libro.id_biblioteca == int(biblioteca):
                        lista_libri.append(libro)
            return lista_libri
        else:
            lista_libri = []
            for libro in self._dictLibri[genere]:
                if libro.id_biblioteca == int(biblioteca):
                    lista_libri.append(libro)
            return lista_libri

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return list(self._dictLibri.keys()) # prende la lista delle chiavi del dizionario

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.leggi_biblioteche_da_db()