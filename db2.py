import psycopg2


#Creating table
def createtable():
    conn=psycopg2.connect("dbname='data' user='postgres' password='poorna1999' port='5432' host='localhost' ")
    cur=conn.cursor()
    cur.execute("CREATE TABLE data( rollno INTEGER,name TEXT,marks REAL) ")
    conn.commit()
    conn.close()
    
createtable()