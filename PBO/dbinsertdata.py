import mysql.connector

mydb = mysql.connector.connect(
  host="172.0.0.1",
  port=23306,
  user="root",
  password="p455w0rd",
  database="garden"
)

db = mydb.cursor()

sql = "INSERT INTO Anggrek (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("2", "1", "Benih")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO Anggrek (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("1", "1", "Tunas")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO anggrek (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("2", "1", "Tanaman Kecil")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO anggrek (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("2", "1", "Tanaman Dewasa")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO Anggrek (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("4", "2", "Berbunga")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO Mawar (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("2", "1", "Benih")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO Mawar (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("3", "1", "Tunas")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO Mawar (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("1", "1", "Tanaman Kecil")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO Mawar (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("1", "1", "Tanaman Dewasa")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO anggrek (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("1", "2", "Berbunga")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO Melati (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("1", "1", "Benih")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO Melati (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("1", "1", "Tunas")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO Melati (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("2", "1", "Tanaman Kecil")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO Melati (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("2", "1", "Tanaman Dewasa")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

sql = "INSERT INTO Melati (Beri_Air, Beri_Pupuk, Status_Tumbuh) VALUES (%s, %s , %s)"
val = ("2", "3", "Berbunga")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")