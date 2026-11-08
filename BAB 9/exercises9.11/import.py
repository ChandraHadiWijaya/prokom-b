from user_admin import Admin

admin_sultan = Admin("Sultan", "alamsyah", "sultan_admin", "sultan@email.com", "Serang")

print(f"Mengakses profil Admin: {admin_sultan.first_name}")
admin_sultan.privileges.show_privileges()
