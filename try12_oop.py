#contoh struktur pencabangan if
#input data dari pengguna
nilai_ujian = float(input("masukan nilai ujian siswa:"))
#struktur kontrol percabangan majemuk
if nilai_ujian >= 90:
  predikat="sangat baik (A)"
elif nilai_ujian>=75:
  predikat="baik (B)"
elif nilai_ujian>=60:
  predikat="cukup (C)"
else :
  predikat ="kurang (D) - memerlukan remedial"

print("hasil evaluasi :",predikat)
