#import MySQLdb
import dbeng

def cleartable():
    db = dbeng.getcon()
    cursor = db.cursor()
    sql = "delete from polinoms where id <> 0"
    cursor.execute( sql )
    db.commit()
    
def line_to_db( strline, index ):
    vl = [ int(e) for e in strline.split(" ") if int(e) != 0 ]
    db = dbeng.getcon()
    for ( i, e ) in enumerate( vl ):
        cursor = db.cursor()
        sql = """INSERT INTO polinoms (id, np, val) VALUES (%(id)s, %(np)s, %(val)s)
        ON DUPLICATE KEY UPDATE id = %(id)s, np = %(np)s, val = %(val)s"""
        cursor.execute( sql, {"id" : index, "np" : i, "val" : e} )
        db.commit()
        cursor.close()

cleartable()
f = open("examp\\ex1.cnf")
#f = open("C:\\Program Files (x86)\\University of Southampton\\WinSAT\\sample CNF files\\aim-100-1_6-no-2.cnf")
l = f.readline()
i = 0
load = False
while (l != ""):
    if load :
        line_to_db( l, i )
    i += 1
    if i % 100 == 0:
        print( i )
    if (l[ :5 ] == "p cnf" ):
        load = True
    l = f.readline()

print("End")