import dbeng

db = dbeng.getcon()
cursor = db.cursor()
sql = """
select min(`tbl_and`.`res_or`) from 
(SELECT `tbl_or`.id, sum(sat.vals.val) as `res_or` FROM sat.polinoms as `tbl_or`
join sat.vals 
on tbl_or.val = sat.vals.id
group by tbl_or.id) as `tbl_and`
"""

cursor.execute( sql )

row = cursor.fetchone()

if row is not None:
    print( "Ans :", row[0] )