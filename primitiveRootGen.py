from math import sqrt

# Returns True if n is prime
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to find primitive roots of n
def findPrimitive(n):
    if not isPrime(n):
        return -1

    phi = n - 1
    prime_factors = set()
    findPrimeFactors(prime_factors, phi)

    primitive_roots = []
    for r in range(2, phi + 1):
        is_primitive = True
        for it in prime_factors:
            if power(r, phi // it, n) == 1:
                is_primitive = False
                break
        if is_primitive:
            primitive_roots.append(r)
            if len(primitive_roots) == 2:
                break

    return primitive_roots

# Utility function to store prime factors of a number
def findPrimeFactors(s, n):
    while n % 2 == 0:
        s.add(2)
        n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            s.add(i)
            n //= i
    if n > 2:
        s.add(n)

# Iterative Function to calculate (x^n)%p in O(log y)
def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y >>= 1
        x = (x * x) % p
    return res

# Driver Code
n = 13
primitive_roots = findPrimitive(n)

if len(primitive_roots) < 2:
    result = f"No second primitive root found for {n}."
else:
    result = [primitive_roots[0], primitive_roots[1]]



g1= result[0]
g2= result[1]

print(g1, g2)
