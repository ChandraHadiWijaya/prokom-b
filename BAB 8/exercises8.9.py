#pesan

def show_messages(messages):
    """Mencetak semua pesan teks di dalam list."""
    for message in messages:
        print(message)


pesan_singkat = [
    "Halo, apa kabar?",
    "Jangan lupa belajar Python hari ini!",
    "Kode kamu sudah berhasil dijalankan.",
]

show_messages(pesan_singkat)
