# Nama dengan spasi, tab (\t), dan baris baru (\n) di awal dan akhir
nama = "\n\t  nanadinoo  \t\n"

print("Tampilan Asli (Masih ada spasi/jarak):")
print(nama)

# Menghapus spasi di sebelah kiri saja
print("\nMenggunakan lstrip():")
print(nama.lstrip())

# Menghapus spasi di sebelah kanan saja
print("\nMenggunakan rstrip():")
print(nama.rstrip())

# Menghapus spasi di kedua sisi
print("\nMenggunakan strip():")
print(nama.strip())
