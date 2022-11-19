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
