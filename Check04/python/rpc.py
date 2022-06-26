import MySQLdb
from nameko.rpc import rpc

def connect():
    DBconnect = MySQLdb.connect(host='db',
                                user='devops',
                                passwd='devops101',
                                db='devops_db',
                                port=3306)
    return DBconnect

def query(username, password):
    DBconnect = connect()
    cur = DBconnect.cursor()
    cur.execute("SELECT * FROM login04 WHERE name04=(%s) AND pass04=(%s);",
                (username, password))
    DBconnect.commit()
    result = cur.fetchall()
    DBconnect.close()
    if len(result) == 0:
        return 0
    else:
        return 1

class Service:
    name = "Check"

    @rpc
    def query(self, username, password):
        result = query(username, password)
        return result
