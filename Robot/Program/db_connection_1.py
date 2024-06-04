import cx_Oracle
import os
from Utility.python_utils import Utils


query = Utils.yaml_parser("../Config/data.yaml")
conn = cx_Oracle.connect("test_db","test_db","localhost/xe")
cur = conn.cursor()
cur.execute(query['data']['select_query'])
a = cur.fetchall()
for i in a:
    print(i)
cur.close()
conn.close()