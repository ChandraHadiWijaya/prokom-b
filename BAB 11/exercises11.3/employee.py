class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        """Menginisialisasi atribut profil karyawan dan gaji tahunan."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Menaikkan gaji sebesar 5000 secara default, atau sesuai jumlah kustom."""
        self.annual_salary += amount
