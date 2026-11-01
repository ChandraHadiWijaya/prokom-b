#tidak ada pengguna

users = ['ara', 'dea', 'admin', 'muthia', 'della']

if users:
    for user in users:
        if user == 'admin':
            print("Halo admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {user.title()}, terima kasih telah masuk kembali.")
else:
    print("We need to find some users!")

users.clear()  

if users:
    for user in users:
        print(f"Hello {user.title()}")
else:
    print("We need to find some users!")
