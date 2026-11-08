class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Menginisialisasi atribut nama dan jenis kuliner (dari 9-1)."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
        self.number_served = 0

    def describe_restaurant(self):
        """Mencetak ringkasan informasi restoran (dari 9-1)."""
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Kuliner: {self.cuisine_type}")

    def open_restaurant(self):
        """Mencetak pesan restoran buka (dari 9-1)."""
        print(f"{self.restaurant_name} sekarang sudah buka! Yuk silakan mampir.")

    def set_number_served(self, number):
        """Mengatur jumlah pelanggan yang telah dilayani ke nilai tertentu."""
        self.number_served = number

    def increment_number_served(self, additional_served):
        """Menambah jumlah pelanggan yang dilayani dengan angka tertentu."""
        self.number_served += additional_served

restaurant = Restaurant("Rumah Makan Sederhana", "Masakan Padang")

print(f"Jumlah pelanggan awal yang dilayani: {restaurant.number_served}")

restaurant.number_served = 15
print(f"Jumlah setelah diubah langsung: {restaurant.number_served}")

restaurant.set_number_served(35)
print(f"Jumlah setelah set_number_served(): {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"Jumlah setelah increment_number_served(): {restaurant.number_served}")
