import sqlite3


#Creating table
def createtable():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE data( rollno INTEGER,name TEXT,marks REAL) ")
    conn.commit()
    conn.close()
    
def inserttable(roll,name,marks):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)",(roll,name,marks))
    cur.commit()
    cur.close()
    
inserttable(54,"poorna",100)