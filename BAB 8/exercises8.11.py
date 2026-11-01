#arsip pesan

def send_messages(messages, sent_messages):
    """Mencetak pesan dan memindahkannya ke list sent_messages."""
    print("--- Mengirim Pesan (Menggunakan Salinan) ---")
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim: {current_message}")
        sent_messages.append(current_message)

pesan_singkat = [
    "Halo, apa kabar?",
    "Jangan lupa belajar Python hari ini!",
    "Kode kamu sudah berhasil dijalankan.",
]
pesan_terkirim = []

send_messages(pesan_singkat[:], pesan_terkirim)

print("\n--- Verifikasi List Akhir ---")
print(f"List awal asli (pesan_singkat) TETAP UTUH: {pesan_singkat}")
print(f"List baru (pesan_terkirim): {pesan_terkirim}")
