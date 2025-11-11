from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    def get_musei(self):
        conn=ConnessioneDB.get_connection()
        musei=[]

        if conn is None:
            print('Errore nella connessione')
            return []
        cursor=conn.cursor(dictionary=True)
        query="""
        SELECT *
        FROM musei_torino.museo 
        ORDER BY nome
        """
        cursor.execute(query)

        # Creo l'oggetto museo
        for row in cursor:
            museo=Museo(
                id=row['id'],
                nome=row['nome'],
                tipologia=row['tipologia'],
            )
            musei.append(museo)

        cursor.close()
        conn.close()
        return musei # Questa funzione, come dividi_per_epoche(), restituisce una lista. In questo caso contiene oggetti relativi a ciascun museo
    # TODO
