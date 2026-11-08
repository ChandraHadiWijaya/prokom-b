from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'
contents = path.read_text()

print("--- Kode yang Lebih Sederhana dan Ringkas ---")
# Langsung melakukan looping pada fungsi splitlines() tanpa variabel bantuan
for line in contents.splitlines():
    print(line)
