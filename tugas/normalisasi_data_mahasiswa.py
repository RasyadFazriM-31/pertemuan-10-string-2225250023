# Tugas 4 - Normalisasi Data Mahasiswa
# Input  : nama lengkap dan kode kelas dengan format tidak konsisten
# Proses : bersihkan spasi, ubah kapitalisasi, bentuk kode kelas dan inisial
# Output : nama bersih, kode kelas, jumlah kata, dan inisial


def normalisasi_nama(nama):
    """Hapus spasi berlebih (awal, akhir, tengah) lalu ubah ke title case."""
    return " ".join(nama.strip().split()).title()


def buat_inisial(nama):
    """Ambil huruf awal setiap kata pada nama yang sudah dinormalisasi."""
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata)


def normalisasi_kode(kode):
    """Huruf besar, lalu spasi antarkata diganti tanda hubung."""
    kata = kode.strip().upper().split()
    return "-".join(kata)


def hitung_kata(nama):
    return len(normalisasi_nama(nama).split())


if __name__ == "__main__":
    nama = input("Nama: ")
    kode = input("Kode kelas: ")

    nama_bersih = normalisasi_nama(nama)
    kode_bersih = normalisasi_kode(kode)
    inisial = buat_inisial(nama)
    jumlah_kata = hitung_kata(nama)

    print(f"Nama bersih : {nama_bersih}")
    print(f"Kode kelas  : {kode_bersih}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial}")
