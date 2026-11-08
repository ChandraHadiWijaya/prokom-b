class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Kuliner: {self.cuisine_type}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Es Krim dan Teh"):
        """Menginisialisasi atribut dari induk, lalu menambah atribut rasa es krim."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanila", "Cokelat", "Stroberi", "Macha"]

    def display_flavors(self):
        """Mencetak semua varian rasa es krim yang tersedia."""
        print(f"\nVarian rasa yang tersedia di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- Rasa {flavor}")

kedai_eskrim = IceCreamStand("Mixue Indonesia")

kedai_eskrim.describe_restaurant()

kedai_eskrim.display_flavors()
