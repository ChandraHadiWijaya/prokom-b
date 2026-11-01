#toping pizza

prompt = "\nMasukkan toping pizza yang kamu inginkan:"
prompt += "\n(Ketik 'quit' jika sudah selesai) "

while True:
    topping = input(prompt)
    
    if topping.lower() == 'quit':
        break
    else:
        print(f"Oke, saya akan menambahkan {topping} ke pizza kamu!")
