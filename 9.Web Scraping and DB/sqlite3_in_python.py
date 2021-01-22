import sqlite3
conn=sqlite3.connect('example1.db')
c=conn.cursor()

'''Insert query'''
# c.execute("""CREATE TABLE IF NOT EXISTS EMP(ID INT PRIMARY KEY,NAME TEXT,SALARY REAL)""")
# c.execute('INSERT INTO EMP(ID,NAME,SALARY) VALUES(101,"AKASH",1000)')
# c.execute('INSERT INTO EMP(ID,NAME,SALARY) VALUES(102,"SHUBH",5000)')
# c.execute('INSERT INTO EMP(ID,NAME,SALARY) VALUES(103,"OM",6000)')
# conn.execute('COMMIT')

'''Select query'''
# c.execute("""SELECT * FROM EMP""")
# for row in c:
#     print(row)


#update query
''''c.execute('UPDATE EMP SET NAME="OMKAR" WHERE NAME="OM"')
conn.execute('COMMIT')

c.execute("""SELECT * FROM EMP""")
for row in c:
    print(row)
    '''
#Delete query
'''c.execute("""DELETE FROM EMP WHERE ID=103""")

conn.execute('COMMIT')'''
c.execute("SELECT * FROM EMP")
for row in c:
    print(row)

