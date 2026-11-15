#Nawili2

try :
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    number = int(input('Enter a number to divide 100 by: '))

    print('100 /', number, '=', 100 / number)
    print('Hello, ' + name + '! Next year you will be ' + str(age + 1) + ' years old.')

except ValueError :
    print('Invalid input')
except ZeroDivisionError :
    print('Cannot divide by zero')
except TypeError:
    print('cannot join text and number')
except Exception as e:
    print('Other error:',e)

#3 Nawili

