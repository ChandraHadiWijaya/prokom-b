#glosarium 2

glossary = {
    'dictionary': 'Koleksi pasangan kunci-nilai (key-value pairs).',
    'list': 'Koleksi item dengan urutan tertentu.',
    'string': 'Serangkaian karakter atau teks.',
    'loop': 'Menjalankan blok kode secara berulang untuk sekumpulan item.',
    'variable': 'Label yang dikaitkan dengan suatu nilai.',
    # Lima istilah tambahan baru:
    'boolean': 'Nilai ekspresi logika yang hanya bernilai True atau False.',
    'key': 'Bagian pertama dari pasangan kunci-nilai dalam dictionary untuk memanggil nilai.',
    'value': 'Bagian kedua dari pasangan kunci-nilai yang berisi data sebenarnya.',
    'comment': 'Catatan dalam kode yang diabaikan oleh penerjemah Python.',
    'float': 'Jenis tipe data untuk angka desimal atau pecahan.',
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")
