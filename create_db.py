import mysql.connector

cred = {"host" : "localhost", "user" : "root", "passwd" : ""}
db = mysql.connector.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], charset = 'utf8')
cursor = db.cursor()

sql = "CREATE DATABASE IF NOT EXISTS sat"
cursor.execute(sql)
db.commit()

db = mysql.connector.connect(host = cred["host"], user = cred["user"], passwd = cred["passwd"], db = "sat", charset = 'utf8')
cursor = db.cursor()

sql = """
        CREATE TABLE IF NOT EXISTS polinoms (
        id INT,
        np INT, 
        val INT,
        primary key (id, np)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
"""
cursor.execute(sql)

sql = """
        CREATE TABLE IF NOT EXISTS vals (
        id INT,
        val INT,
        primary key (id)
        ) ENGINE=INNODB CHARACTER SET utf8 COLLATE utf8_bin;
"""
cursor.execute(sql)

print("End")