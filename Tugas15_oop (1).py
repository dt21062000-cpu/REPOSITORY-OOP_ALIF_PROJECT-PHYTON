print("=== KALKULATOR SEDERHANA ===") 

angka1 = int(input("Masukkan angka pertama : ")) 
angka2 = int(input("Masukkan angka kedua : ")) 

print("1. Penjumlahan") 
print("2. Pengurangan") 
print("3. Perkalian") 
print("4. Pembagian")

pilihan = input("Pilih operasi : ") 

if pilihan == "1": 
    hasil = angka1 + angka2 
    print("Hasil =", hasil)
   
elif pilihan == "2": 
      hasil = angka1 - angka2 
      print("Hasil =", hasil) 
      
elif pilihan == "3": 
      hasil = angka1 * angka2 
      print("Hasil =", hasil) 
    
elif pilihan == "4": 
      hasil = angka1 / angka2 
      print("Hasil =", hasil)
     
else: 
    print("Pilihan tidak tersedia")