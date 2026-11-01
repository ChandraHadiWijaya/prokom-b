#profil pengguna

def build_profile(first, last, **user_info):
    """Membangun dictionary yang berisi semua informasi profil user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile(
    'chandra', 
    'hadi',
    location='jakarta',
    field='engineer',
    hobby='tidur dan kulineran'
)

print(my_profile)
