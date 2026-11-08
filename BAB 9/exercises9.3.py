class User:
    def __init__(self, first_name, last_name, username, email, location):
        """Menginisialisasi atribut profil pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        """Mencetak ringkasan informasi pengguna dengan rapi."""
        print(f"\nProfil Pengguna: {self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email:    {self.email}")
        print(f"  Lokasi:   {self.location}")

    def greet_user(self):
        """Mencetak salam personal untuk pengguna."""
        print(f"Halo, {self.first_name}! Selamat datang kembali di dasbor Anda.")

user_1 = User("Neejad", "muhammad faqih", "neejad_kotbum", "neejad@email.com", "Tangerang")
user_2 = User("Sulaiman", "al hajj", "sulaiman_ah", "sulaiman@email.com", "Surabaya")
user_3 = User("Sultan", "alamsyah", "sultan_almsyh", "sultan@email.com", "Serang")


user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
