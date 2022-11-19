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