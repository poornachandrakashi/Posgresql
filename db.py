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
    conn.commit()
    conn.close()
    
inserttable(54,"poorna",100)

def display():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM data")
    row=cur.fetchall()
    conn.commit()
    conn.close()
    return row

print(display())

def delete(roll):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=?",(roll,))
    conn.commit()
    conn.close()
delete(54)