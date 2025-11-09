from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        # La fonte della connessione
        self.connection = ConnessioneDB.get_connection()

    def dividi_per_epoche(self):
        conn= self.connection
        epoche=[]

        if conn is None:
            print("Errore di connessione")
            return []
        try:
            cursor = conn.cursor()
            query = 'SELECT DISTINCT epoca FROM musei_torino.artefatto ORDER BY epoca'
            cursor.execute(query)

            for (epoca,) in cursor:
                if epoca is not None:
                    epoche.append(epoca)

                cursor.close()
                conn.close()
                return epoche
                # La funzione ritornerà una lista che contiene tutte le epoche (senza ripetizioni) presenti nel database
        except Exception as e:
            print(f'Errore di connessione: {e}')
            if conn:
                conn.close()
            return []

    def estrai_artefatto(self, museo_input:str, epoca_input:str):
        conn=self.connection
        risultato=[]

        if conn is None:
            print("Errore di connessione")
            return []

        try:
            cursor = conn.cursor()
            query=""" 
            SELECT a.id, a.nome, a.tipologia, a.epoca, a.id_museo
            FROM musei_torino.artefatto a, musei_torino.museo m 
            WHERE a.id_museo=m.id
            """ # Con questa prima query selezioniamo gli artefatti facendo un join tra l'id della tabella museo e l'id della tabella artefatto

            if museo_input is not None:
                # Se l'input del nome del museo non è nullo, allora possiamo procedere ad aggiungere alla query il nome del museo da ricercare
                query += 'AND m.nome=%s' # Il nome del museo in cui vogliamo cercare l'artefatto è dato in input tramite l'app

            if epoca_input is not None:
                query += 'AND COALESCE(%s, epoca)' # L'epoca dell'artefatto selezionate nell'interfaccia

            query += 'ORDER BY a.nome'

            cursor.execute(query, (museo_input, epoca_input))

            # Finalmente dopo aver fatto queste selezioni, possiamo creare l'oggetto artefatto
            for row in cursor:
                artefatto=Artefatto(
                    id=row['id'],
                    nome=row['nome'],
                    tipologia=row['tipologia'],
                    epoca=row['epoca'],
                    id_museo=row['id_museo']
                )
                risultato.append(artefatto)

            cursor.close()
            conn.close()
            return risultato

        except Exception as e:
            print(f'Errore di connessione: {e}')
            if conn:
                conn.close()
            return []

    # TODO