#1Luwi ricxvebi

number = 1
while number <=50 :
    if number % 2 == 0 :
        print(number)
    number += 1

#2 jami 1-dan N-mde

n = int(input('Enter N: '))
total = 0
number = 1
while number <= n:
    total += number
    number += 1
    print('Sum:', total)

#3 n = int(input('Enter n: '))
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f'{n}! = {factorial}')

#4 sashualo aritmetikuli

total = 0
count = 0
while True :
    number = int(input('Enter a number :'))
    if number == 0 :
        break
        total += number
        count += 1

print('Count:', count)
print('Sum:', total)

if count > 0 :
    print('Avarage :', total / count)
else:
    print('Avarage : 0')


#5 gamocnobana

secret = 5
for i in range(5) :
     guess = int(input('Guess :'))
     if guess > secret :
         print('Too high')
     elif guess < secret :
         print('Too low')
     else :
         print('You win!')
         break
else :
    print('You lose! The number was 5')