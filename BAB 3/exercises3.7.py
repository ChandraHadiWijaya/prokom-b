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

print("<==========================>")

print("kabar buruk, meja besar di pesan ternyata tidak datang tepat waktu sehingga hanya bisa mengundang 2 orang saja")

print("<==================================>")

tamu_batal= daftar_tamu.pop()
print(f"mohon maaf {tamu_batal}, kami tidak dapat mengundang kamu ke makan malam")
tamu_batal= daftar_tamu.pop()
print(f"mohon maaf {tamu_batal}, kami tidak dapat mengundang kamu ke makan malam")
tamu_batal= daftar_tamu.pop()
print(f"mohon maaf {tamu_batal}, kami tidak dapat mengundang kamu ke makan malam")
tamu_batal= daftar_tamu.pop()
print(f"mohon maaf {tamu_batal}, kami tidak dapat mengundang kamu ke makan malam")

print("<===========================>")
print(f"haloo {daftar_tamu[0]}, kamu tetap di undang makan malam ")
print(f"haloo {daftar_tamu[1]}, kamu tetap di undang makan malam ")

print("<========================>")
del daftar_tamu[0]
del daftar_tamu[0]
print (daftar_tamu)
