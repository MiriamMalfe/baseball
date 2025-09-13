from database.DB_connect import DBConnect
from model.team import Team


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnno():
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        query = """SELECT DISTINCT(year) FROM teams WHERE year>1979"""
        listaAnni = []
        cursor.execute(query)
        for c in cursor:
            listaAnni.append(c["year"])
        db.close()
        cursor.close()
        return listaAnni

    @staticmethod
    def getSquadreAnno(anno):
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        query = """SELECT * FROM teams WHERE year=%s"""
        listaSquadre=[]
        cursor.execute(query, (anno, ))
        for c in cursor:
            listaSquadre.append(Team(**c))
        db.close()
        cursor.close()
        return listaSquadre

    @staticmethod
    def salariSquadra(teamCode, anno):
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        query = """SELECT SUM(salary) AS somma FROM salaries WHERE teamCode=%s AND year=%s"""

        cursor.execute(query, (teamCode, anno))
        somma=0
        for c in cursor:
            somma= c["somma"]
        db.close()
        cursor.close()
        return somma

