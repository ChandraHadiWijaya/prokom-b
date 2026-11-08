import openpyxl as pyxl
# Path, Nama file, dan sheet
file_path = "files/Nilai_KelasA.xlsx"
wb = pyxl.load_workbook(file_path, data_only=True)
sheet = wb["Sheet1"]

for row in sheet.iter_rows(min_row=15, max_row=20, min_col=2, max_col=7):
    print([cell.value for cell in row])