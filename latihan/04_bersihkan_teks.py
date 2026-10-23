# Latihan 4 - Membersihkan Teks
# Input  : teks dengan spasi berlebih di awal, akhir, dan di antara kata
# Proses : strip() lalu ganti dua spasi dengan satu spasi sampai tidak ada lagi
# Output : teks bersih dengan huruf kapital pada karakter pertama

teks = "   belajar   python   untuk    pendidikan  "
teks = teks.strip()
while "  " in teks:
    teks = teks.replace("  ", " ")
print(teks.capitalize())
