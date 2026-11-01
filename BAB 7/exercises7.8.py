#toko roti

sandwich_orders = ['tuna', 'telur', 'ayam panggang', 'keju']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) 
    print(f"Saya sedang membuat {current_sandwich} sandwich Anda.")
    finished_sandwiches.append(current_sandwich)

print("\nSemua sandwich telah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")
