numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
prime_status = True
for i in numbers:
    for k in range(2, i // 2 + 1):
        if (i % k == 0) and (i != k) and (i != 1):
            prime_status = False
            break
        else:
            prime_status = True
    if prime_status and i != 1:
        primes.append(i)
    elif i != 1:
        not_primes.append(i)

print("Primes are: ", primes)
print("Not rimes are: ", not_primes)