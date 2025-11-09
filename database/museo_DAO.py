from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        self.connection=ConnessioneDB().get_connection()

    def get_musei(self):
        conn=self.connection
        risultato=[]

        if conn is None:
            print('Errore nella connessione')
            return []

        try:
            cursor=conn.cursor()
            query="""
            SELECT *
            FROM musei_torino.museo 
            """
            cursor.execute(query)

            # Creo l'oggetto museo
            for row in cursor:
                museo=Museo(
                    id=row['id'],
                    nome=row['nome'],
                    tipologia=row['tipologia'],
                )
                risultato.append(museo)

            cursor.close()
            conn.close()
            return risultato
        except Exception as e:
            print(f'Errore di connessione: {e}')
            if conn:
                conn.close()
            return []
    # TODO
