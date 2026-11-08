from pathlib import Path

files = [
    Path(__file__).parent / 'cats.txt',
    Path(__file__).parent / 'dogs.txt'
]

for file_path in files:
    try:
        konten = file_path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\n--- Isi dari berkas {file_path.name} ---")
        print(konten.strip())
