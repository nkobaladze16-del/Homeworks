
#Luwia tu kenti

number = int(input('Enter number:'))

if number % 2 == 0:
    print('Even')
else:
    print('odd')

    #2asakobrivi kategoria

    age = int(input('Enter your age:'))
    if 0 <= age <= 12:
        print('child')
    elif 13 <= age <= 17:
        print('teenager')
    elif 18 <= age <= 64:
        print('adult')
    elif age >=65:
        print('senior')
    else:
        print('invalid age')

    #3shefasebis sistema

    grade =int(input('enter your grade'))
    if 90 <= grade <= 100:
        print('A')
    elif  80 <= grade <= 89 :
        print('B')
    elif 70 <= grade <= 79:
        print('C')
    elif 60 <= grade <=69:
        print('D')
    elif 50 <= grade <=59 :
        print('E')
    elif grade < 50:
        print('F')
    elif grade < 0 or grade > 100:
        print('invalid grade')
    else:
        print('invalid grade')


        #4yes/no

answer = input('Do you like Python? (yes/no):')
answer = answer.lower()

if answer == 'yes' :
            print('Great')
elif answer == 'no':
            print('maybe you will like it later')
else:
            print('please, answer yes or no')


            #5 calculator
print('calculator start')
num1 = float(input('first number:'))
num2 = float(input('second number'))
operation = input('operation(+, -, *, /):')

if operation == '+':
                 print(num1 + num2)
elif operation == '-':
                 print(num1-num2)
elif operation == '*':
                 print(num1 * num2)
elif operation == '/':
                if num2 == 0:
                 print('cannot devide by zero')
                else:
                 print(num1/num2)
else:
                 print('Invalid operation')