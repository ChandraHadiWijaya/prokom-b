class User:
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

class Privileges:
    def __init__(self):
        self.privileges = ["bisa menambah postingan", "bisa menghapus postingan", "bisa blokir pengguna"]

    def show_privileges(self):
        print("Hak akses yang dimiliki:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = Privileges()

admin_baru = Admin("Sulaiman", "al hajj", "sulaiman_admin")

admin_baru.privileges.show_privileges()
