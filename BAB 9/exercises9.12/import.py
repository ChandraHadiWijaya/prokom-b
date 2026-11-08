from admin import Admin

admin_sulaiman = Admin("Sulaiman", "al hajj", "sulaiman_admin", "sulaiman@email.com", "Surabaya")

print(f"Mengakses profil Admin: {admin_sulaiman.first_name}")
admin_sulaiman.privileges.show_privileges()
