#tiket bioskop

prompt = "\nBerapa usia kamu? "
prompt += "\n(Ketik 'quit' untuk keluar) "

while True:
    age_input = input(prompt)
    
    if age_input.lower() == 'quit':
        break
        
    age = int(age_input)
    
    if age < 3:
        print("Tiket kamu GRATIS!")
    elif age <= 12:
        print("Harga tiket kamu adalah $10.")
    else:
        print("Harga tiket kamu adalah $15.")
