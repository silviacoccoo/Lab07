import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self.dropdown_musei=ft.Dropdown(label='Museo', width=300, on_change=self.controller.seleziona_museo)
        self.dropdown_epoche=ft.Dropdown(label='Epoca', width=300, on_change=self.controller.seleziona_epoca)
        # TODO

        # Sezione 3: Artefatti
        btn_artefatti=ft.ElevatedButton(text="Mostra artefatti", on_click=self.controller.mostra_artefatti)
        self.lista_artefatti=ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)
        # TODO

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1: Titolo
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(controls=[self.dropdown_musei, self.dropdown_epoche], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),
            # TODO

            # Sezione 3: Artefatti
            btn_artefatti,
            self.lista_artefatti,
            # TODO
        )

        if self.controller:
            self.controller.popola_dropdown()

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
