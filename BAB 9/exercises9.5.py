class User:
    def __init__(self, first_name, last_name, username, email, location):
        """Menginisialisasi atribut profil dan upaya login."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        
        self.login_attempts = 0

    def describe_user(self):
        """Mencetak ringkasan informasi pengguna."""
        print(f"\nProfil Pengguna: {self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")

    def greet_user(self):
        """Mencetak salam personal."""
        print(f"Halo, {self.first_name}! Selamat datang kembali.")

    def increment_login_attempts(self):
        """Menambah nilai login_attempts sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mereset nilai login_attempts menjadi 0."""
        self.login_attempts = 0

user_neejad = User("Neejad", "Muhammad Faqih", "neejad_Kotbum", "neejad@email.com", "Tangerang")

print("--- Mencoba login beberapa kali ---")
user_neejad.increment_login_attempts()
user_neejad.increment_login_attempts()
user_neejad.increment_login_attempts()
user_neejad.increment_login_attempts()

print(f"Jumlah upaya login saat ini: {user_neejad.login_attempts}")

print("--- Mereset upaya login ---")
user_neejad.reset_login_attempts()

print(f"Jumlah upaya login setelah di-reset: {user_neejad.login_attempts}")
