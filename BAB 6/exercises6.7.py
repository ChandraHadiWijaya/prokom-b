#orang orang

person_1= {'first_name': 'tiara','last_name': 'harya putri','age': 19, 'city': 'Jakarta',}
person_2 = {'first_name': 'neejad', 'last_name': 'muhammad faqih', 'age': 18, 'city': 'Tangerang'}
person_3 = {'first_name': 'putri', 'last_name': 'maharani', 'age': 27, 'city': 'Wonogiri'}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nNama Lengkap: {full_name}")
    print(f"Usia: {person['age']} tahun")
    print(f"Kota: {person['city']}")
