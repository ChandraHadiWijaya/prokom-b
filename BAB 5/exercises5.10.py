#Memeriksa Nama Pengguna

pengguna_saat_ini = ['ara', 'dea', 'admin', 'muthia', 'della']
pengguna_saat_ini_versi_huruf_kecil = [user.lower() for user in pengguna_saat_ini]

pengguna_baru = ['neejad', 'DEA', 'sultan', 'kennard', 'sulaiman']

for penggunabaru in pengguna_baru:
    if penggunabaru.lower() in pengguna_saat_ini_versi_huruf_kecil:
        print(f"Sorry, the username '{penggunabaru}' is already taken. Please enter a new username.")
    else:
        print(f"Great! The username '{penggunabaru}' is available.")
