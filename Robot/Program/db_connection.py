import cx_Oracle
import os
from Config import TestData

#data = TestData.Test_Data()

os.environ['PATH'] = "E:\\instantclient\\instantclient_21_13"

conn = cx_Oracle.connect("test_db","test_db","localhost/xe")

cur = conn.cursor()
cur.execute(TestData.Test_Data.query)

cur.close()
conn.commit()
conn.close()












