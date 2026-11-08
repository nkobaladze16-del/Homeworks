#Indexebi da slicing

word = 'programming'

print(word[0])
print(word[-1])
print(word[-3])
print(word[:4])
print(word[7:])
print(word[::2])
print(word[::-1])


#El postis dashla


Email ='student@mail.example.com'
print('Email')
print(Email.index("@"))
print(Email[0:7])

domain = Email [Email.index("@") +1:]
print(domain)
print(Email[8:12])

#Telefonis nomris gasuftaveba


print('+995 555 11-12-13'.replace('-','') .replace(' ',''))

#URL misamartis generatori

text = '  My First Python   Program '

print(text .lower() .split())
s







text = f'I\'m (name), I\'m (age) years old, I\'m from(city)my favourite languageis(programming)'
name = input('enter your name')
age = input('enter your age')
city = input('enter your birthplace')
programming = input('enter the programmname')
