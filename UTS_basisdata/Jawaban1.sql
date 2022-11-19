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
