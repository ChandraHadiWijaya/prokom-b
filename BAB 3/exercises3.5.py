# perubahan daftar tamu
    #daftar sebelum perubahan
daftar_tamu = ["irfan", "nayva", "angga"]
print(f"halo {daftar_tamu[0]}, anda diundang makan malam bersama esok hari.")
print(f"halo {daftar_tamu[1]}, anda diundang makan malam bersama esok hari.")
print(f"halo {daftar_tamu[2]}, anda diundang makan malam bersama esok hari.")

    # daftar setelah perubahan
print(f"{daftar_tamu[2]}, berhalangan hadir")
daftar_tamu[2] = "eshal"
print(f"halo {daftar_tamu[0]}, kamu di undang makan malam esok hari")
print(f"halo {daftar_tamu[1]}, kamu di undang makan malam esok hari")
print(f"halo {daftar_tamu[2]}, kamu di undang makan malam esok hari")
