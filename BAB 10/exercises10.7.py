print("--- KALKULATOR PENJUMLAHAN TERUS-MENERUS ---")
print("(Ketik 'keluar' pada input angka jika ingin berhenti)\n")

while True:
    angka1 = input("Masukkan angka pertama: ")
    if angka1.lower() == 'keluar':
        break
        
    angka2 = input("Masukkan angka kedua: ")
    if angka2.lower() == 'keluar':
        break

    try:
        hasil = int(angka1) + int(angka2)
    except ValueError:
        print("Input salah! Tolong masukkan angka, bukan huruf. Silakan coba lagi.\n")
    else:
        print(f"Hasil: {hasil}\n")

print("Terima kasih telah menggunakan kalkulator!")
