


number = int(input('Give an integer from 3 to 20: '))
password = ''

for i in range(1, (number // 2 + 1)):
    for j in range(i, number):
        if number % (i + j) == 0:
            password += str(i)
            password += str(j)

print(password)
