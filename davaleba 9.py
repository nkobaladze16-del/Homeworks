#1
def print_ticket(passenger, destination, ticket_class):
    print("--- TICKET ---")
    print("Passenger:", passenger)
    print("Destination:", destination)
    print("Class:", ticket_class)


print_ticket("Nika", "Batumi", "Economy")
print_ticket("Mari", "Kutaisi", "Business")
print_ticket("Luka", "Batumi", "Economy")

#2
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


print("37C =", celsius_to_fahrenheit(37))
print("0C =", celsius_to_fahrenheit(0))
print("100C =", celsius_to_fahrenheit(100))


def is_warm(celsius, limit=20):
    return celsius > limit


print(is_warm(25))
print(is_warm(25, 30))
print(is_warm(limit=10, celsius=15))

#3

def add_student(name, group=None):
    if group is None:
        group = []

    if name not in group:
        group.append(name)

    return group

#3
def analyze_numbers(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


numbers = [12, 7, 25, 3, 18]

minimum, maximum, average = analyze_numbers(numbers)

print("Min:", minimum)
print("Max:", maximum)
print("Average:", average)





#4
group_a = add_student("Ana")
group_b = add_student("Nika")

group_a = add_student("Mari", group_a)
group_a = add_student("Ana", group_a)

print("Group A:", group_a)
print("Group B:", group_b)

#5
def check_password(password):
    if len(password) < 6:
        return "Too short"

    if password.isdigit():
        return "Weak"

    if password.isalpha():
        return "Medium"

    return "Strong"


passwords = ['abc', '1234567', 'qwerty', 'python3', 'Tbilisi2024']

for password in passwords:
    print(password, "->", check_password(password))

