#coding: utf_8


import mysql.connector
import json
from scraping import get_data




mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="password",
	database="pfa"
)
mycursor = mydb.cursor()

#db fill
f = open("companies_scraped_data.json")
data = json.load(f)

for d in data:
	sql = "INSERT INTO company (name, top_tools, tools, logo, description) VALUES (%s, %s, %s, %s, %s)"
	val = (d["name"], str(d["top tools"]), json.dumps(d["tools"]), d["logo"], d["desc"])
	mycursor.execute(sql, val)
	
f.close()


mydb.commit()

