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
f = open("categoriesData.txt")
category_obj = f.read()
category_obj = json.loads(category_obj)
parent_id = 0
cat_id = 0
for gp in list(category_obj.keys()):
	for p in list(category_obj[gp].keys()):
		parent_id += 1
		sql = "INSERT INTO parent_category (name, parent) VALUES (%s, %s)"
		val = (p, gp)
		mycursor.execute(sql, val)
		for cat in category_obj[gp][p]:
			cat_id += 1
			sql = "INSERT INTO category (name, parent) VALUES (%s, %s)"
			val = (cat["name"], parent_id)
			mycursor.execute(sql, val)
			sql = "INSERT INTO tool (name, category_id, stacks_num, logo) VALUES (%s, %s, %s, %s)"
			values = get_data(cat["link"] , cat_id)
			mycursor.executemany(sql, values)
f.close()


mydb.commit()

