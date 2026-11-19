#1sayidlebis sia

shopping = ['milk', 'bread', 'eggs']

shopping.append('cheese')
print(shopping)

shopping.insert(0, 'apples')
print(shopping)

shopping[2] = 'butter'
print(shopping)

shopping.extend({'tea', 'coffee', 'cake'})
print(shopping)

shopping.remove('tea')
print(shopping)

shopping .pop(1)
print(shopping)

#2gamocdis qulebi

scores = [85, 92, 78, 92, 65, 88, 92]
print('count of 92:', scores.count(92))
print('Index of 78:', scores.index(78))

asc_scores = sorted(scores)
print('ascending:', asc_scores)
desc_scores = sorted(scores,reverse = True)
print('Descending:', desc_scores)
print('Highest:', max(scores), 'Lowest', min(scores))
print('Original', scores)

#3 matrica

matrix = [[1,2,3], [4,50,6], [7,8,9]]

print(matrix[0])
print(matrix[1])
print(matrix[1][2])
print(matrix[2][0])
matrix[1][1] = 50

print(matrix)

#4 siis shevseba

numbers = []
while True :
    number = input('Enter a number:')
    if number == 'stop' :
        break
    numbers.append(int(number))

print('List', numbers)
print('Count:', len(numbers))
print('First:', numbers[0], 'Last:', numbers[-1])

descending =sorted(numbers, reverse=True)
print('Descending:', descending)