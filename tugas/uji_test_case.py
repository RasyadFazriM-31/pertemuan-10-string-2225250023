# Pengujian test case wajib Tugas 4 (otomatis, memakai assert)
# Jalankan dari folder utama: python3 tugas/uji_test_case.py

from normalisasi_data_mahasiswa import (
    normalisasi_nama,
    normalisasi_kode,
    buat_inisial,
    hitung_kata,
)

KASUS = [
    # (input nama, input kode, nama, kode, jumlah kata, inisial)
    ("  aan hendrayana", "pmat a 2026", "Aan Hendrayana", "PMAT-A-2026", 2, "AH"),
    ("fATHIYYAH mUTHMAINNAH", "kelas b", "Fathiyyah Muthmainnah", "KELAS-B", 2, "FM"),
    ("BUDI", "pmtk 01", "Budi", "PMTK-01", 1, "B"),
    ("  siti nur aisyah ", "kelas c", "Siti Nur Aisyah", "KELAS-C", 3, "SNA"),
]

for nama, kode, exp_nama, exp_kode, exp_kata, exp_ini in KASUS:
    assert normalisasi_nama(nama) == exp_nama, nama
    assert normalisasi_kode(kode) == exp_kode, kode
    assert hitung_kata(nama) == exp_kata, nama
    assert buat_inisial(nama) == exp_ini, nama

print("Semua test case Tugas 4 LULUS")
