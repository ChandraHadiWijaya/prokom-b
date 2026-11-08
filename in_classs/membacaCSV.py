import csv

FILE_NAME = 'files/nilaiKuliah.csv'
listNilai = []
kolom = []
with open(FILE_NAME) as csvfile: 
    readCSV = csv.reader(csvfile, delimiter=',')
    bariske = 0
    for baris in readCSV:
        if bariske == 0:
            kolom = baris
            bariske += 1
            continue
    listNilai.append(baris)
        
print(kolom)
print(listNilai)