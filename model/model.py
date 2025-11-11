from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO
from model.museoDTO import Museo
from database.DB_connect import ConnessioneDB as db
'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        artefatti_db=self._artefatto_dao.estrai_artefatto(museo, epoca)
        return artefatti_db
        # TODO

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        epoche_db=self._artefatto_dao.dividi_per_epoche() # Recupero le epoche
        return epoche_db
        # TODO

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        museo=self._museo_dao.get_musei()
        return museo
        # TODO

