from user import User

class Privileges:
    def __init__(self):
        self.privileges = ["bisa menambah postingan", "bisa menghapus postingan", "bisa blokir pengguna"]

    def show_privileges(self):
        print("Hak akses yang dimiliki:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
    
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()
