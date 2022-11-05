CREATE TABLE mhsiswa(
id INT AUTO_INCREMENT,
nama_mhs VARCHAR(255),
nim_mhs VARCHAR(255),
jenis_kelamin VARCHAR(255),
PRIMARY KEY (id)
);

CREATE TABLE Dosen(
id INT AUTO_INCREMENT,
kd_dosen VARCHAR(255),
nama_dosen VARCHAR(255),
PRIMARY KEY (id)
);

CREATE TABLE matakuliah(
id INT AUTO_INCREMENT,
kd_mk VARCHAR (255),
nama_mk VARCHAR (255),
sks INT (11),
PRIMARY KEY (id)
);

CREATE TABLE fakultas(
id INT AUTO_INCREMENT,
nama_fakultas VARCHAR (255),
PRIMARY KEY (id)
);

CREATE TABLE akreditasi(
id INT AUTO_INCREMENT,
akreditasi INT (11),
PRIMARY KEY (id)
);


INSERT INTO mhsiswa (nama_mhs, nim_mhs, jenis_kelamin) VALUES ('Haechan', '127', 'Laki-laki'), ('Mark lee', '128', 'Laki-Laki'), ('Kim jungwoo', '129', 'Laki-laki')
INSERT INTO akreditasi (akreditasi) VALUES ('A'),('B'),('C')
INSERT INTO fakultas (nama_falkutas) VALUES ('Teknik Informatika'),  ('Manajemen'), ('Teknik Sipil')


-- Jawaban no 1

SELECT
mhsiswa.id,
mhsiswa.nama_mhs,
mhsiswa.nim_mhs,
mhsiswa.jenis_kelamin,
Dosen.kd_dosen,
Dosen.nama_dosen,
fakultas.nama_falkutas,
akreditasi.akreditasi
FROM
mhsiswa
INNER JOIN fakultas,Dosen,akreditasi
WHERE 
mhsiswa.ref_to_fakultas = fakultas.id and mhsiswa.ref_to_dos = Dosen.id and mhsiswa.ref_to_akreditasi = akreditasi.id

-- Jawaban no 2

SELECT
mhsiswa.id,
mhsiswa.nama_mhs,
mhsiswa.nim_mhs,
mhsiswa.jenis_kelamin,
fakultas.nama_falkutas
FROM
mhsiswa
INNER JOIN fakultas WHERE mhsiswa.ref_to_fakultas=fakultas.id

-- Jawaban Nomor 3

SELECT 
	mhsiswa.id,
	mhsiswa.nama_mhs,
	mhsiswa.jenis_kelamin,
	fakultas.nama_falkutas,
	akreditasi.akreditasi
from 
	mhsiswa
inner join fakultas,akreditasi
where mhsiswa.ref_to_fakultas = fakultas.id and mhsiswa.ref_to_akreditasi = akreditasi.id

-- Jawaban nomor 4

SELECT 
Dosen.id,
Dosen.kd_dosen,
Dosen.nama_dosen,
mhsiswa.nama_mhs,
mhsiswa.nim_mhs,
mhsiswa.jenis_kelamin
FROM
Dosen
INNER JOIN mhsiswa WHERE Dosen.ref_to_mhs = mhsiswa.id

-- Jawaban Nomor 5

SELECT
Dosen.id,
Dosen.kd_dosen,
Dosen.nama_dosen,
fakultas.nama_falkutas,
akreditasi.akreditasi
FROM
Dosen
INNER JOIN fakultas,akreditasi
WHERE Dosen.ref_to_fakultas = fakultas.id AND Dosen.ref_to_akreditasi = akreditasi.id