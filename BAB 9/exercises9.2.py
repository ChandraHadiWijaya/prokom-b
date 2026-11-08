class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Menginisialisasi atribut nama dan jenis kuliner (Sama seperti 9-1)."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Mencetak ringkasan informasi restoran (Sama seperti 9-1)."""
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Kuliner: {self.cuisine_type}")

    def open_restaurant(self):
        """Mencetak pesan restoran buka (Sama seperti 9-1)."""
        print(f"{self.restaurant_name} sekarang sudah buka! Yuk silakan mampir.")


restaurant_1 = Restaurant("Warteg Bahari", "Masakan Rumahan khas Tegal")
restaurant_2 = Restaurant("Mie Gacoan", "Mie Pedas Kekinian dan Dimsum")
restaurant_3 = Restaurant("Solaria", "Menu Hidangan Keluarga dan Chinese-Indonesian Food")

restaurant_1.describe_restaurant()
print() 
restaurant_2.describe_restaurant()
print()
restaurant_3.describe_restaurant()
