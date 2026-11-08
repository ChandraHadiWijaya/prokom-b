class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Menginisialisasi atribut nama dan jenis kuliner."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Mencetak ringkasan informasi restoran."""
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Kuliner: {self.cuisine_type}")

    def open_restaurant(self):
        """Mencetak pesan yang menunjukkan bahwa restoran telah buka."""
        print(f"{self.restaurant_name} sekarang sudah buka! Yuk silakan mampir.")

restaurant = Restaurant("pagi sore", "masakan padang")

print(f"Atribut Nama: {restaurant.restaurant_name}")
print(f"Atribut Kuliner: {restaurant.cuisine_type}")
print()

restaurant.describe_restaurant()
restaurant.open_restaurant()
