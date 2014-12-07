import mysql.connector
cred = {"host" : "localhost", "user" : "root", "passwd" : ""}

def getcon():
    db = mysql.connector.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], db = "sat", charset = 'utf8')
    return db
