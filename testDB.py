import mysql.connector

cnx = mysql.connector.connect(user='user', password='passowrd',
                              host='127.0.0.1',
                              database='dbname')
cursor = cnx.cursor()
query = ("SELECT name,id FROM db.table")
cursor.execute(query)
for (name) in cursor:
	print("{}".format(name))
cursor.close()
cnx.close()
