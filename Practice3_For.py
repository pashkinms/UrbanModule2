numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:
    print(i)
    counter = 0
    for k in range(1, i+1):
       if i % k == 0:
           counter+=1
    if counter > 2:
        not_primes.append(i)
    else:
        primes.append(i)

print("Primes are: ", primes)
print("Not rimes are: ", not_primes)