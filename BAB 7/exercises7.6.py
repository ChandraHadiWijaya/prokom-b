# tiga cara keluar

#Menggunakan tes kondisi langsung pada pernyataan while
topping = ""
while topping.lower() != 'quit':
    topping = input("\nMasukkan toping pizza (atau ketik 'quit'): ")
    
    if topping.lower() != 'quit':
        print(f"Oke, saya akan menambahkan {topping} ke pizza kamu!")

# Menggunakan variabel aktif (flag) untuk mengontrol perulangan
active = True
while active:
    topping = input("\nMasukkan toping pizza (atau ketik 'quit'): ")
    
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Oke, saya akan menambahkan {topping} ke pizza kamu!")

#Menggunakan pernyataan break untuk langsung keluar
while True:
    topping = input("\nMasukkan toping pizza (atau ketik 'quit'): ")
    
    if topping.lower() == 'quit':
        break
    print(f"Oke, saya akan menambahkan {topping} ke pizza kamu!")

