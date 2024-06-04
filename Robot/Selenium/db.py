import pyodbc

conn=pyodbc.connect('Driver=SQL Server;'
                    'Server=192.168.0.17;'
                    'Database=DB1;'
                    'Trusted Connection=YEs;'
                    )
cursor=conn.cursor()
cursor.execute("select * from DB.tab1")

for r in cursor:
    print(r)
