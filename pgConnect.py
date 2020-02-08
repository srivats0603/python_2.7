import sys
import psycopg2
import pgpasslib

myList = []

try:
    conn = psycopg2.connect("dbname=xyz2 user=xplore_xyz host=xyz.com port=4000 password=xyz!")
except psycopg2.OperationalError as e:
    print e

sql = """SELECT * FROM aoms_grid_componententity WHERE type_def_id = 2"""
sql1 = """SELECT count(*) FROM aoms_grid_componententity WHERE type_def_id = 2"""

cur = conn.cursor()

cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    myDict = {}
    myDict["def_id"] = row[0]
    myDict["entity_id"] = row[1]
    myDict["type_def_id"] = row[2]
    myDict["component_name"] = row[3]
    myList.append(myDict)

cur.execute(sql1)
numBuses = cur.fetchall()[0][0]

print "total buses =",numBuses

conn.close()
