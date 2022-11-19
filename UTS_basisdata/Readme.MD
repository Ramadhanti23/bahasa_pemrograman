-- Jawaban 1 
CREATE TABLE Mahasiswa(
id INT AUTO_INCREMENT,
nama_mahasiswa VARCHAR(255),
nim_mahasiswa VARCHAR(255),
jenis_kelamin VARCHAR(255),
PRIMARY KEY(id)
);

CREATE TABLE Dosen(
id INT AUTO_INCREMENT,
kd_dosen VARCHAR(255),
nama_dosen VARCHAR(255),
PRIMARY KEY(id)
);

CREATE TABLE Mata_kuliah(
id INT AUTO_INCREMENT,
nama_matkul VARCHAR(255),
PRIMARY KEY(id)
);

-- Jawaban 2
INSERT INTO Mahasiswa (nama_mahasiswa, nim_mahasiswa, jenis_kelamin) VALUES ('Lee Haechan', '12709', 'Laki-laki'), ('Mark Lee', '12708', 'Laki-Laki'), ('Irene', '12567', 'perempuan')
INSERT INTO Dosen (kd_dosen, nama_dosen) VALUES ('2324', 'Jonnhy Suh'), ('4563', 'Seulgi Rv'), ('1412', 'Jaehyun')
INSERT INTO Mata_kuliah (nama_matkul) VALUES ('Basis data'), ('Kalkulus 2'), ('Bahasa Inggris')

-- jawaban 3
SELECT
Mahasiswa.id,
Mahasiswa.nama_mahasiswa,
Mahasiswa.nim_mahasiswa,
Mahasiswa.jenis_kelamin,
Dosen.kd_dosen,
Dosen.nama_dosen,
Mata_kuliah.nama_matkul
FROM
Mahasiswa
INNER JOIN Dosen, Mata_kuliah
WHERE
Mahasiswa.rel_to_dos = Dosen.id and Mahasiswa.rel_to_matkul= Mata_kuliah.id

-- Jawaban 4
SELECT
Mahasiswa.id,
Mahasiswa.nama_mahasiswa,
Mahasiswa.nim_mahasiswa,
Mahasiswa.jenis_kelamin,
Mata_kuliah.nama_matkul
FROM
Mahasiswa
INNER JOIN Mata_kuliah
WHERE 
Mahasiswa.rel_to_matkul = Mata_kuliah.id

-- jawaban 5 
SELECT
Dosen.id,
Dosen.kd_dosen,
Dosen.nama_dosen,
Mata_kuliah.nama_matkul
FROM
Dosen
INNER JOIN Mata_kuliah
WHERE
Dosen.rel_to_matkul = Mata_kuliah.id

-- Jawaban 6 
SELECT
Dosen.id,
Dosen.kd_dosen,
Dosen.nama_dosen,
Mahasiswa.nama_mahasiswa,
Mahasiswa.nim_mahasiswa,
Mahasiswa.jenis_kelamin,
Mata_kuliah.nama_matkul
FROM
Dosen
INNER JOIN Mahasiswa, Mata_kuliah
WHERE 
Dosen.rel_to_mhs = Mahasiswa.id and Dosen.rel_to_matkul = Mata_kuliah.id