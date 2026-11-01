#prasmanan

menu_buffet = ('nasi goreng', 'mie ayam', 'soto bogor', 'rendang', 'ketoprak')

print("Menu Asli:")
for makanan in menu_buffet:
    print(f"- {makanan}")

# "Mencoba mengubah item (ini akan menyebabkan error):")
menu_buffet[0] = 'bakso'

menu_buffet = ('nasi goreng', 'mie ayam', 'soto bogor', 'bakso', 'pempek')
print("Menu Baru:")
for makanan in menu_buffet:
    print(f"- {makanan}")
