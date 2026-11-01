# Polling 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_poll = ['jen', 'budi', 'phil', 'vanda', 'dinda', 'alesha']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Terima kasih, {person.title()}, karena sudah berpartisipasi dalam polling!")
    else:
        print(f"Halo {person.title()}, kami mengundang Anda untuk mengikuti polling bahasa favorit Anda.")
