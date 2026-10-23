# Latihan 5 - split dan join
# Input  : kalimat
# Proses : split() memecah menjadi list kata, join() menggabungkan dengan tanda "-"
# Output : list kata dan hasil gabungan

kalimat = "data teks perlu dibersihkan"
kata = kalimat.split()
print(kata)
print("-".join(kata))
