print("--- PROGRAM PENJUMLAHAN ---")

angka1 = input("Masukkan angka pertama: ")
angka2 = input("Masukkan angka kedua: ")

try:
    hasil = int(angka1) + int(angka2)
except ValueError:
    print("Error: Mohon masukkan angka yang valid, jangan memasukkan huruf atau teks!")
else:
    print(f"Hasil penjumlahan: {hasil}")
