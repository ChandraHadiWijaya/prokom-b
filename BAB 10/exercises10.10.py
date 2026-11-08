from pathlib import Path

path = Path(__file__).parent / 'cerita.txt'

try:
    contents = path.read_text()
except FileNotFoundError:
    print("File cerita.txt belum dibuat!")
else:
    # Menghitung kata 'the' secara umum (termasuk di dalam kata 'then', 'there')
    jumlah_the_biasa = contents.lower().count('the')
    print(f"Jumlah kata 'the' (kasar): {jumlah_the_biasa}")

    # Menghitung kata 'the ' menggunakan spasi agar hanya kata utuh yang terhitung
    jumlah_the_spasi = contents.lower().count('the ')
    print(f"Jumlah kata 'the ' (dengan spasi): {jumlah_the_spasi}")
