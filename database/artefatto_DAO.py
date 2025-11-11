from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # QUESTO METODO SERVE PER OTTENERE UNA LISTA DI TUTTE LE EPOCHE CONTENUTE NEL DATABASE, OVVIAMENTE SENZA RIPETIZIONI
    def dividi_per_epoche(self):
        conn= ConnessioneDB.get_connection()
        epoche=[]

        if conn is None:
            print("Errore di connessione")
            return []
        cursor = conn.cursor()
        query = 'SELECT DISTINCT epoca FROM musei_torino.artefatto WHERE epoca IS NOT NULL ORDER BY epoca'
        cursor.execute(query)

        for (epoca,) in cursor:
            if epoca is not None:
                epoche.append(epoca)

        cursor.close()
        conn.close()
        return epoche
        # La funzione ritornerà una lista che contiene tutte le epoche (senza ripetizioni) presenti nel database

    # QUESTO METODO SERVE PER ESTRARRE UN ARTEFATTO DATO IN INPUT UN MUSEO E UN'EPOCA
    def estrai_artefatto(self, museo_input:str, epoca_input:str):
        conn=ConnessioneDB.get_connection()
        risultato=[]

        if conn is None:
            print("Errore di connessione")
            return []
        cursor = conn.cursor(dictionary=True)
        query=""" 
        SELECT a.id, a.nome, a.tipologia, a.epoca, a.id_museo
        FROM musei_torino.artefatto a, musei_torino.museo m 
        WHERE a.id_museo=m.id AND m.nome=COALESCE(%s, m.nome) AND a.epoca=COALESCE(%s, a.epoca)
        ORDER BY a.id 
        """ # Con questa query selezioniamo gli artefatti facendo un join tra l'id della tabella museo e l'id della tabella artefatto
        cursor.execute(query, (museo_input, epoca_input))

        # Dopo aver fatto queste selezioni, possiamo creare l'oggetto artefatto
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
        return risultato # La funzione restituisce una lista che contiene gli oggetti relativi a ciascun artefatto
    # TODO