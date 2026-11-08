from random import randint

class Die:
    def __init__(self, sides=6):
        """Menginisialisasi jumlah sisi dadu, defaultnya 6 sisi."""
        self.sides = sides

    def roll_die(self):
        """Mencetak angka acak antara 1 dan jumlah sisi dadu."""
        return randint(1, self.sides)

# Membuat dadu 6 sisi dan mengocoknya 10 kali
dadu_6 = Die()  # Menggunakan nilai default 6
print("Mengocok dadu 6 sisi sebanyak 10 kali:")
for _ in range(10):
    print(dadu_6.roll_die(), end=" ")
print("\n")

# Membuat dadu 10 sisi dan mengocoknya 10 kali
dadu_10 = Die(sides=10)
print("Mengocok dadu 10 sisi sebanyak 10 kali:")
for _ in range(10):
    print(dadu_10.roll_die(), end=" ")
print("\n")

# Membuat dadu 20 sisi dan mengocoknya 10 kali
dadu_20 = Die(sides=20)
print("Mengocok dadu 20 sisi sebanyak 10 kali:")
for _ in range(10):
    print(dadu_20.roll_die(), end=" ")
print()
