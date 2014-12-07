import dbeng

db = dbeng.getcon()
cursor = db.cursor()
sql = """
INSERT INTO vals (id, val) VALUES (%(id)s, %(val)s)
        ON DUPLICATE KEY UPDATE id = %(id)s, val = %(val)s
"""

ans = "100011100000001000111101010111110000101111101100001001101101000100010000111"

ans = "".join( ["1" for e in range(497)] ) 

def sign( x ):
    ret = 0
    if x > 0:
        ret = 1
    return ret

def get_ans_from_file( filename ):
    f = open( filename )
    l = f.readline()
    vals = [str( sign( int( e ) ) ) for e in l.split(" ") if int(e) != 0]
    print( vals )
    return "".join( vals )


def load_vals_to_vals():
    for (i, e) in enumerate(ans):
        v = int(e)
        print( i+1, v )
        cursor.execute( sql, { "id" : (i + 1), "val" : v } )
        db.commit()
        cursor.execute( sql, { "id" : (i + 1) * (-1), "val" : 1 - v } )
        db.commit()
    
ans = get_ans_from_file( "examp\\ex1.ans" )
load_vals_to_vals()
print( ans )
print("yes")