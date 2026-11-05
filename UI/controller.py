import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popolaBiblioteche(self):
        listaBiblioteche = self._model.get_biblioteche()
        for biblioteca in listaBiblioteche:
            self._view._ddBiblioteche.options.append(ft.DropdownOption(key=f"{biblioteca}", text=f"{biblioteca}"))
    def popolaGeneri(self):
        listaGeneri = self._model.get_generi()
        for genere in listaGeneri:
            self._view._ddGeneri.options.append(ft.DropdownOption(key=f"{genere}", text=f"{genere}"))

    # CALLBACKS DROPDOWN
    def seleziona_biblioteca(self):
        self.biblioteca_selezionata = self._view._ddBiblioteche.value
    def seleziona_genere(self):
        self.genere_selezionato = self._view._ddGeneri.value

    # AZIONE: MOSTRA LIBRI
    def hanlderButtonMostra(self, e):
        self._view._listaLibri.controls.clear()
        lista_libri_filtrati = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        for libro in lista_libri_filtrati:
            self._view._listaLibri.controls.append(ft.Text(str(libro)))
        self._view.update()

