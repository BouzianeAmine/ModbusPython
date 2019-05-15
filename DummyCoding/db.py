#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import mysql.connector as mysql
HOST="localhost"
USER="root"
PASS="admin"
DBNAME="amine"

class Mydb:

	def __init__(self):
		self.mydb=mysql.connect(host=HOST,user=USER,passwd=PASS,database=DBNAME)
		print("---Database connection done---")
	

	def insert(self,val1,val2):
		mycursor = self.mydb.cursor(prepared=True);
		sql = "INSERT INTO test (un, deux) VALUES (?, ?)";
		val = (val1,val2);
		mycursor.execute(sql, val);
		self.mydb.commit();
		print(mycursor.rowcount, "record inserted.");


