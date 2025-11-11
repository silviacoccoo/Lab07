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
    def popola_dropdown(self,e=None):
        musei=self._model.get_musei() # Otteniamo i musei

        option_musei=[ft.dropdown.Option(key=None, text='Nessun filtro')] # Inizializzo la lista di opzioni con l'opzione Nessun filtro
        # A nessun filtro corrisponde la chiave None

        # Successivamente aggiungiamo a quetsa lista di opzioni tutti gli altri musei del database
        if musei: # Se esiste la lista di musei
            for museo in musei:
                option_musei.append(ft.dropdown.Option(key=museo.nome, text=museo.nome)) # Aggiungo il museo ai musei attraverso il comando ft.dropdown.Option

        # Una volta che è stata completata la lista di opzioni
        self._view.dropdown_musei.options=option_musei # Aggiungo la lista di opzioni di musei al controllo dropdown
        self._view.dropdown_musei.value=None # Questa è l'opzione di default

        epoche=self._model.get_epoche() # Otteniamo le epoche
        option_epoche=[ft.dropdown.Option(key=None, text='Nessun filtro')]
        if epoche:
            for epoca in epoche:
                    option_epoche.append(ft.dropdown.Option(key=epoca, text=epoca))

        self._view.dropdown_epoche.options=option_epoche
        self._view.dropdown_epoche.value=None

        # Dopo aver fatto tutte le operazioni si deve aggiornare l'interfaccia
        self._view.update()
    # TODO

    # CALLBACKS DROPDOWN
    def seleziona_museo(self,e):
        self.museo_selezionato = e.control.value
        print('Museo selezionato: ',self.museo_selezionato)

    def seleziona_epoca(self,e):
        self.epoca_selezionata = e.control.value
        print('Epoca: ',self.epoca_selezionata)
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
