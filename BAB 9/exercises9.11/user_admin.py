class User:
    def __init__(self, first_name, last_name, username, email, location):
        """Menginisialisasi atribut profil pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

class Privileges:
    def __init__(self):
        """Menyimpan daftar kemampuan admin."""
        self.privileges = ["bisa menambah postingan", "bisa menghapus postingan", "bisa blokir pengguna"]

    def show_privileges(self):
        """Menampilkan hak akses."""
        print("Hak akses yang dimiliki:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        """Menginisialisasi atribut induk, lalu memasukkan Class Privileges sebagai atribut."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()
