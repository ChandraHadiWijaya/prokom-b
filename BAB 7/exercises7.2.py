#kapasitas restoran

group_size = input("Ada berapa orang dalam kelompok makan malam Anda? ")
group_size = int(group_size)

if group_size > 8:
    print("Maaf, Anda harus menunggu beberapa saat sampai ada meja kosong yang siap.")
else:
    print("Silakan masuk, meja Anda sudah siap!")
