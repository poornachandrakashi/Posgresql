import psycopg2


#Creating table
def createtable():
    conn=psycopg2.connect("dbname='data' user='postgres' password='poorna1999' port='5432' host='localhost' ")
    cur=conn.cursor()
    cur.execute("CREATE TABLE data( rollno INTEGER,name TEXT,marks REAL) ")
    conn.commit()
    conn.close()
    
def inserttable(roll,name,marks):
    conn=psycopg2.connect("dbname='data' user='postgres' password='poorna1999' port='5432' host='localhost' ")
    cur=conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)",(roll,name,marks))
    conn.commit()
    conn.close()
    
# inserttable(54,"poorna",100)
# inserttable(44,"Navya",98)
def display():
    conn=psycopg2.connect("dbname='data' user='postgres' password='poorna1999' port='5432' host='localhost' ")
    cur=conn.cursor()
    cur.execute("SELECT * FROM data")
    row=cur.fetchall()
    conn.commit()
    conn.close()
    return row

print(display())

def delete(roll):
    conn=psycopg2.connect("dbname='data' user='postgres' password='poorna1999' port='5432' host='localhost' ")
    cur=conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=%s",(roll,))
    conn.commit()
    conn.close()
delete(44)