#hewan peliharaan

pet_1 = {'kind': 'harimau', 'owner': 'tiara'}
pet_2 = {'kind': 'gorilla', 'owner': 'neejad'}
pet_3 = {'kind': 'rubah', 'owner': 'putri'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Hewan peliharaan milik {pet['owner'].title()} adalah seekor {pet['kind']}.")
