numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = 0
    for j in range(1, i + 1):
        if i % j == 0:
            is_prime += 1
        if is_prime == 3:
            not_primes.append(i)
            break
    if is_prime == 2:
        primes.append(i)
print(f'Primes: {primes}\nNot Primes: {not_primes}')