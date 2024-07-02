from database.DB_connect import DBConnect
from model.connessione import Connessione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct g.Chromosome as crom 
from genes g 
where g.Chromosome !=0 """

        cursor.execute(query)

        for row in cursor:
            result.append(row["crom"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getConnessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t1.c1 as v1,t2.c2 as v2, sum(i.Expression_Corr) as peso
from (select distinct g.GeneID as g1, g.Chromosome as c1
from genes g) as t1,
(select distinct g.GeneID as g2, g.Chromosome as c2
from genes g) as t2,
interactions i 
where i.GeneID1 =t1.g1 and i.GeneID2 =t2.g2
and t1.c1!=t2.c2 and t1.c1!=0 and t2.c2!=0
group by t1.c1,t2.c2"""

        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result
