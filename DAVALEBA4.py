#kinoteatri(and)

age = int(input('Enter your age'))
money = int(input('Enter money'))

if age >= 12 and money >= 15 :
    print('enjoy the movie')
else:
    print('access denied')


    #2 Nakiani weliwadi

    year = int(input( 'Enter year'))

    if(year % 4==0 and year % 100 != 0) or year % 400 == 0:
        print('leap year')
    else:
        print('not a leap year')


    #3 Bankomati

pin = int(input('Enter your pin'))
balance = 500

if (pin != 1234) :
        print('wrong pin')
else:
        amount = int(input('Enter amount:'))
        if amount <=0:
            print('Invalid amount')
        elif amount > balance:
            print('not enough money')
        else:
            balance = balance - amount
            print('Take your money', amount)
            print('New balance',balance)

            #shecdomebis damushaveba
#nawili1

            name = input('Enter name: ')
            age = int(input('Enter age: '))
            number = int(input('Enter a number to divide 100 by: '))

            print('100 /', number, '=', 100 / number)
            print('Hello, ' + name + '! Next year you will be ' + (age + 1) + ' years old.')


#1-shi Typeerror
#2-shi Valueerror
#3-shi ZeroDivisionError

#Nawili2

try :
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    number = int(input('Enter a number to divide 100 by: '))

    print('100 /', number, '=', 100 / number)
    print('Hello, ' + name + '! Next year you will be ' + (age + 1) + ' years old.')

except ValueError :
    print('Invalid input')
except ZeroDivisionError :
    print('Cannot divide by zero')
except TypeError:
    print('cannot join text and number')
except Exception as e:
    print('Other error:',e)