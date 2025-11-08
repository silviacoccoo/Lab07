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
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, e):
        # Recupero la lista di artefatti (per il museo e l'epoca selezionati) attraverso la funzione definita all'interno di Model
        lista_artefatti = self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)

        # Pulisce dai vecchi risultati
        self._view.lista_artefatti.controls.clear()

        if lista_artefatti: # Se esiste una lista di artefatti per quel museo ed epoca selezionati allora...
            for artefatto in lista_artefatti:
                # Aggiungo ciascun artefatto alla ListView
                self._view.lista_artefatti.controls.append(ft.Text(str(artefatto)))

            self._view.show_alert(f'Sono stati trovati {len(lista_artefatti)} artefatti')
        else: # Se non c'è una lista
            self._view.lista_artefatti.controls.append(ft.Text('Non è stato trovato alcun artefatto'))
            self._view.show_alert('Non è stato trovato alcun artefatto')

        # Ricordarsi di aggiornare la pagina
        self._view.update()
    # TODO
