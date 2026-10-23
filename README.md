# Pertemuan 10 - String dan Pengolahan Teks

Nama: Rasyad Fazri Mulyono
NIM: 2225250023
Kelas: 3A

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python: indeks, slicing, method string, `split`, `join`, dan pencarian.

## Struktur Program

```
pertemuan-10-string-2225250023/
|-- README.md
|-- .gitignore
|-- latihan/
|   |-- 01_dasar_string.py
|   |-- 02_indeks_slicing.py
|   |-- 03_method_string.py
|   |-- 04_bersihkan_teks.py
|   |-- 05_split_join.py
|   `-- 06_pencarian_kata.py
`-- tugas/
    |-- normalisasi_data_mahasiswa.py   Tugas 4
    `-- uji_test_case.py                pengujian test case wajib (assert)
```

## Cara Menjalankan

```
python3 tugas/normalisasi_data_mahasiswa.py
```

Untuk menguji test case wajib:

```
cd tugas
python3 uji_test_case.py
```

## Hasil Latihan

| Latihan | Hasil yang ditampilkan |
|---|---|
| 01 | `Algoritma`, `9`, `ALGORITMA`, `algoritma` |
| 02 | `P`, `n`, `Pemr`, `ograman`, `namargormeP` |
| 03 | `fATHIYYAH mUTHMAINNAH`, `Fathiyyah Muthmainnah`, `FATHIYYAH MUTHMAINNAH` |
| 04 | `Belajar python untuk pendidikan` |
| 05 | `['data', 'teks', 'perlu', 'dibersihkan']` dan `data-teks-perlu-dibersihkan` |
| 06 | `True`, `2`, `0` |

## Algoritma Tugas 4

1. Baca nama dan kode kelas sebagai string.
2. Normalisasi nama: `split()` memecah nama menjadi kata (spasi berlebih otomatis hilang), `join` menyatukan kembali dengan satu spasi, lalu `title()`.
3. Hitung jumlah kata dengan `len` pada hasil `split()` nama bersih.
4. Bentuk inisial dengan mengambil karakter pertama (`k[0]`) setiap kata.
5. Normalisasi kode kelas: `strip()`, `upper()`, `split()`, lalu `"-".join(...)`.
6. Tampilkan hasil dengan format rapi.

Fungsi yang dibuat: `normalisasi_nama`, `buat_inisial`, `normalisasi_kode`, dan `hitung_kata`.

## Test Case

| Input nama | Input kode | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|---|
| `  aan hendrayana` | `pmat a 2026` | Aan Hendrayana / PMAT-A-2026 / 2 / AH | sama | Lulus |
| `fATHIYYAH mUTHMAINNAH` | `kelas b` | Fathiyyah Muthmainnah / KELAS-B / 2 / FM | sama | Lulus |
| `BUDI` | `pmtk 01` | Budi / PMTK-01 / 1 / B | sama | Lulus |
| `  siti nur aisyah ` | `kelas c` | Siti Nur Aisyah / KELAS-C / 3 / SNA | sama | Lulus |

## Refleksi

Nama dari formulir sering memiliki spasi berlebih dan kapitalisasi acak, sehingga dua nama yang sama dianggap berbeda saat dibandingkan. Perbaikannya adalah menormalisasi lebih dulu dengan `strip`, `split`/`join`, dan `title` sebelum data dipakai.

## Sumber dan Bantuan

Bahan ajar Pertemuan 10 (Dr. Aan Hendrayana, S.Si., M.Pd.). Kerangka kode dan README dibantu oleh Claude (AI); seluruh kode telah dijalankan dan diuji.
