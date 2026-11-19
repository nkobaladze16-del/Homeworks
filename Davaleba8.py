#1 dublikantebis moshoreba

numbers = [4, 8, 15, 8, 16, 23, 4, 42, 15, 8]
unique_numbers = set(numbers)
print('Unique numbers:', unique_numbers)
print('Count:', len(unique_numbers))
print('Is 23 in set?', 23 in unique_numbers)

#2 set operaciebi

ana = {'python','java','c','sql'}
nika = {'python', 'javascript', 'sql','go'}

print('Union', ana.union(nika))

print('Intersection', ana.intersection(nika))
print('Difference', ana.difference(nika))
print('Symmetric difference', ana.symmetric_difference(nika))

#3 kenchisyra

votes =['Ana', 'Nika', 'Ana', 'Mari', 'Nika', 'Ana', 'Mari','Ana']

results = {}

for name in votes :
    results[name] = votes.count(name)

for name, count in results.items():
    print(name +':', count)

#4 magazia

inventory = {
    'laptop': {'price': 2500, 'quantity': 5},
    'mouse': {'price': 40, 'quantity': 0},
    'keyboard': {'price': 120, 'quantity': 12},
    'monitor': {'price': 800, 'quantity': 0}
}

# 1. maragis saerto girebuleba
total = 0

for product in inventory.values():
    total += product['price'] * product['quantity']

print("Total value:", total)

# 2. amowuruli produqtebi
for name, product in inventory.items():
    if product['quantity'] == 0:
        print("Out of stock:", name)

# 3. momxmareblis shekveta
name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))

if name not in inventory:
    print("Product not found")
elif inventory[name]['quantity'] < quantity or quantity <= 0:
    print("Not enough stock")
else:
    total_price = inventory[name]['price'] * quantity
    inventory[name]['quantity'] -= quantity
    print("Total price:", total_price)
    print("Remaining stock:", inventory[name]['quantity'])

    #5

    words = ['python', 'java', 'ai', 'sql', 'go', 'python']

    # 1. kvadratebi 1-dan 10-de
    squares = [x ** 2 for x in range(1, 11)]
    print("Squares:", squares)

    # 2. sityvebi da mati sigrdzeebi
    word_lengths = {word: len(word) for word in words}
    print("Word lengths:", word_lengths)

    # 3. unikaluri pirveli asoebi
    first_letters = {word[0] for word in words}
    print("First letters:", first_letters)
