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