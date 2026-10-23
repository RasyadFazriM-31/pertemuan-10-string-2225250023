# Latihan 6 - Pencarian Kata
# Input  : teks dan kata yang dicari
# Proses : ubah ke huruf kecil agar pencarian tidak peka kapitalisasi,
#          lalu gunakan in, count, dan find
# Output : ada/tidaknya kata, jumlah kemunculan, dan posisi pertama

teks = "Python untuk data. Python untuk pendidikan."
teks = teks.lower()
kata = "python"
print(kata in teks)
print(teks.count(kata))
print(teks.find(kata))
