import pytest
from employee import Employee

# Membuat fixture untuk menyediakan objek contoh karyawan 
@pytest.fixture
def employee_contoh():
    """Membuat sebuah instance Employee yang bisa digunakan oleh semua fungsi tes."""
    return Employee("Chandra", "Hadi", 50000)

def test_give_default_raise(employee_contoh):
    """Menguji kenaikan gaji default (+5000) -> 50000 + 5000 = 55000."""
    employee_contoh.give_raise()
    assert employee_contoh.annual_salary == 55000

def test_give_custom_raise(employee_contoh):
    """Menguji kenaikan gaji kustom (misal +10000) -> 50000 + 10000 = 60000."""
    employee_contoh.give_raise(10000)
    assert employee_contoh.annual_salary == 60000
