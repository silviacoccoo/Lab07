from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO
from database.DB_connect import ConnessioneDB
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

        if museo and epoca:
            conn=None
            cursor=None

            conn=db.get_connection()

            if conn is None:
                print('Errore nella connessione con il database')
                return None

            # Else, quindi se si è stabilita la connessione
            cursor = conn.cursor(dictionary=True)
            query='SELECT * FROM musei_torino.artefatto'
            cursor.execute(query)

            query2='SELECT * FROM musei_torino.artefatto WHERE museo=COALESCE(%s, museo) AND epoca=COALESCE(%s, epoca)'
            cursor.execute(query2)

            result=[]
            for row in cursor:
                result.append(row)

        else:
            return None

        cursor.close()
        conn.close()

        # TODO

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""

        # TODO

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""

        # TODO

