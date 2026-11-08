class User:
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

class Admin(User):
    def __init__(self, first_name, last_name, username):
        """Menginisialisasi atribut induk, lalu menambah daftar hak akses."""
        super().__init__(first_name, last_name, username)
        self.privileges = ["bisa menambah postingan", "bisa menghapus postingan", "bisa blokir pengguna"]

    def show_privileges(self):
        """Menampilkan apa saja hak akses yang dimiliki oleh admin."""
        print(f"\nHak akses untuk Admin ({self.username}):")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin_sultan = Admin("Sultan", "alamsyah", "sultan_admin")
admin_sultan.show_privileges()
