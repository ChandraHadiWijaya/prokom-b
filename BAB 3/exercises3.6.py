# tamu tambahan

daftar_tamu = ["irfan", "nayva", "angga"]
print(f"halo {daftar_tamu[0]}, anda diundang makan malam bersama esok hari.")
print(f"halo {daftar_tamu[1]}, anda diundang makan malam bersama esok hari.")
print(f"halo {daftar_tamu[2]}, anda diundang makan malam bersama esok hari.")
print("<========================>")

print(f"{daftar_tamu[2]}, berhalangan hadir")

daftar_tamu[2] = "eshal"
print(f"halo {daftar_tamu[0]}, kamu di undang makan malam esok hari")
print(f"halo {daftar_tamu[1]}, kamu di undang makan malam esok hari")
print(f"halo {daftar_tamu[2]}, kamu di undang makan malam esok hari")

print("<========================>")

print("kabar baik, kami menemukan adanya meja yang lebih besar!")
daftar_tamu.insert(0, 'jeje')
daftar_tamu.insert(len(daftar_tamu) // 2, "ami")
daftar_tamu.append("nazirah")

print("<========================>")

print(f"halo {daftar_tamu[0]}, kamu di undang makan malam esok hari")
print(f"halo {daftar_tamu[1]}, kamu di undang makan malam esok hari")
print(f"halo {daftar_tamu[2]}, kamu di undang makan malam esok hari")
print(f"halo {daftar_tamu[3]}, kamu di undang makan malam esok hari")
print(f"halo {daftar_tamu[4]}, kamu di undang makan malam esok hari")
print(f"halo {daftar_tamu[5]}, kamu di undang makan malam esok hari")
