jarak_rumah=int(input("masukan jarak rumah (dalam satuan km): ") )
jarak=jarak_rumah*1000
if jarak < 3000:
  print("jarak aman")
else:
  print("jarak terlalu jauh")