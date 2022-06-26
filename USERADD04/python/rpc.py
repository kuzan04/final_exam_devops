import MySQLdb
from nameko.rpc import rpc

def connect():
    DBconnect = MySQLdb.connect(host='db',
                                user='devops',
                                passwd='devops101',
                                db='devops_db',
                                port=3306)
    return DBconnect

def insert(name04, password04, email04):
    DBconnect = connect()
    cur = DBconnect.cursor()
    cur.execute("INSERT INTO login04 (name04, pass04, email04) VALUES (%s, %s, %s);", 
            (name04, password04, email04))
    id = cur.lastrowid
    DBconnect.commit()
    DBconnect.close()
    return id

class Service:
    name = "useradd"

    @rpc
    def insert(self, name04, password04, email04):
        result = insert(name04, password04, email04)
        return result
