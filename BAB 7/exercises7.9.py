#Kehabisan Pastrami

sandwich_orders = ['tuna', 'pastrami', 'telur', 'pastrami', 'ayam panggang', 'pastrami', 'keju']
finished_sandwiches = []

print("Maaf, toko kami saat ini kehabisan daging pastrami!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya sedang membuat {current_sandwich} sandwich Anda.")
    finished_sandwiches.append(current_sandwich)

print("\nSemua sandwich yang berhasil dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")
