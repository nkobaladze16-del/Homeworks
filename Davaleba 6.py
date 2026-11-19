#1
for i in range (1, 11) :
    print(i, 'squared =', i**2)

for i in range(10, 0, -1):
    print(i)
    if i == 1 :
        print('Go')

total = 0
for i in range(1, 101, 2):
    total += i
print('Sum:', total)

#2

text = input('Enter text :')

count = 0

for letter in text.lower() :
    if letter in 'aeiou' :
        count += 1

print('Vowels :', count)

#3

total = 0
count = 0
while True :
    number = input('Enter a number :')
    if number =='Stop' :
        break
    number = input('Enter a number : ')
    if number == 'stop' :
        break
    number = int(number)
    if number < 0 :
        print('Negative number are not allowed')
        continue
    total += number
    count += 1

print('Sum:', total)
print('Count:', count)

#4

n = int(input('Enter a number:'))

# pirveli samkutxedi
for i in range(1, n+1) :
    for j in range(i) :
        print('*', end =' ')
        print()

print()

#meore samkutxedi

for i in range(n, 0, -1) :
    for j in range(i) :
        print('*', end = ' ')
    print()