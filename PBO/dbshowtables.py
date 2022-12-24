import mysql.connector

mydb = mysql.connector.connect(
  host="172.0.0.1",
  port=23306,
  user="root",
  password="p455w0rd",
  database="garden"
)

db = mydb.cursor()

db.execute("SHOW TABLES")

for x in db:
  print(x)