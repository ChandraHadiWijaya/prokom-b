#Pizza Saya, Pizza Anda

pizzas = ['pepperoni', 'margherita', 'meat lover']
friend_pizzas = pizzas[:]
pizzas.append('supreme')
friend_pizzas.append('hawaiian')

print("pizza favorit saya adalah:")
for pizza in pizzas:
    print(f"- {pizza}")

print("pizza favorit teman saya adalah:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
