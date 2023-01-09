import mysql.connector

mydb = mysql.connector.connect(
  host="172.0.0.1",
  port=23306,
  user="root",
  password="p455w0rd",
  database="garden"
)

db = mydb.cursor()

db.execute("CREATE TABLE Anggrek (id INT AUTO_INCREMENT PRIMARY KEY, Beri_Air VARCHAR(255), Beri_Pupuk VARCHAR (255), Status_Tumbuh VARCHAR(255))")
# db.execute("CREATE TABLE Mawar (id INT AUTO_INCREMENT PRIMARY KEY, Beri_Air VARCHAR(255), Beri_Pupuk VARCHAR (255), Status_Tumbuh VARCHAR(255))")
# db.execute("CREATE TABLE Melati (id INT AUTO_INCREMENT PRIMARY KEY, Beri_Air VARCHAR(255), Beri_Pupuk VARCHAR (255), Status_Tumbuh VARCHAR(255))")