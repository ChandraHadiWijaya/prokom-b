class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def get_range(self):
        """Menghitung jarak tempuh berdasarkan ukuran baterai."""
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225
        print(f"Mobil ini dapat menempuh jarak sekitar {range_miles} mil dengan baterai penuh.")

    def upgrade_battery(self):
        """Mengecek ukuran baterai, jika belum 65 maka akan ditingkatkan ke 65."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Baterai berhasil ditingkatkan ke kapasitas 65 kWh!")
        else:
            print("Baterai Anda sudah berada di kapasitas maksimal.")

class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model, = model,
        self.year = year
        self.battery = Battery() 

mobil_listrik = ElectricCar("Wuling", "Air EV", 2024)

print("--- Kondisi Awal ---")
mobil_listrik.battery.get_range()

print("\n--- Melakukan Upgrade ---")
mobil_listrik.battery.upgrade_battery()

print("\n--- Kondisi Setelah Upgrade ---")
mobil_listrik.battery.get_range()
