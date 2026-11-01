#glosarium

glossary = {
    'dictionary': 'Koleksi pasangan kunci-nilai (key-value pairs).',
    'list': 'Koleksi item dengan urutan tertentu.',
    'string': 'Serangkaian karakter atau teks.',
    'loop': 'Menjalankan blok kode secara berulang untuk sekumpulan item.',
    'variable': 'Label yang dikaitkan dengan suatu nilai.',
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")
