from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'

# CARA 1: Membaca seluruh isi file sekaligus

print("--- Cara 1: Membaca Seluruh Isi File ---")
contents = path.read_text()
print(contents)

# CARA 2: Menyimpan ke dalam list lalu di-looping per baris

print("\n--- Cara 2: Menyimpan ke List dan Di-looping ---")
lines = contents.rstrip().split('\n') 
for line in lines:
    print(line)
