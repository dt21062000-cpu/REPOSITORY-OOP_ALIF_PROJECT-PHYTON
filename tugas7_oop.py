kbps=float(input("masukan jaringan mbps:"))
mbps = kbps/1000
if mbps>=50:
  kategori="sangat cepat (A)"
elif mbps>=20:
  kategori="cepat (B)"
elif mbps>=5:
  kategori="sedang (C)"
else:
  kategori="kurang (D) - memerlukan pembenaran"
  
print("hasil evaluasi:",kategori)