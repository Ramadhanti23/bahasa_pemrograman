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