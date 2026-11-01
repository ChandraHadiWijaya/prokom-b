#halo admin

users = ['ara', 'dea', 'admin', 'muthia', 'della']

for user in users:
    if user == 'admin':
        print("Halo admin, apakah Anda ingin melihat laporan status?")
    else:
        print(f"Halo {user.title()}, terima kasih telah masuk kembali.")
