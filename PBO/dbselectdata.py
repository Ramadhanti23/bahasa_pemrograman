import mysql.connector

mydb = mysql.connector.connect(
  host="172.0.0.1",
  port=23306,
  user="root",
  password="p455w0rd",
  database="garden"
)

db = mydb.cursor()

db.execute("SELECT * FROM Anggrek")

res = db.fetchall()

for x in res:
  print(x)  
  
db.execute("SELECT * FROM Mawar")

res = db.fetchall()

for x in res:
  print(x)
  
db.execute("SELECT * FROM Melati")

res = db.fetchall()

for x in res:
  print(x)
