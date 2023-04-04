from collections import Counter

def prime_factorization(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return Counter(factors)

# prime factorize each given number
A = prime_factorization(5100)
B = prime_factorization(33462)
C = prime_factorization(17150)
D = prime_factorization(1)
E = prime_factorization(1)
F = prime_factorization(1)
G = prime_factorization(5100)

# create equations for each variable based on the prime factorization of the numbers
for p in A:
    if p in B and p in G:
        A[p] -= 2
        B[p] -= 1
        C[p] -= 2
        G[p] -= 1
a = 1
for p, exp in A.items():
    a *= p**exp

for p in B:
    if p in A and p in C and p in D and p in E:
        B[p] -= 2
        A[p] -= 3
        C[p] -= 1
        D[p] -= 1
        E[p] -= 2
b = 1
for p, exp in B.items():
    b *= p**exp

for p in C:
    if p in A and p in B and p in D:
        C[p] -= 2
        A[p] -= 1
        B[p] -= 2
        D[p] -= 3
c = 1
for p, exp in C.items():
    c *= p**exp

for p in D:
    if p in A and p in B and p in C:
        D[p] -= 3
        A[p] -= 3
        B[p] -= 3
        C[p] -= 1
d = 1
for p, exp in D.items():
    d *= p**exp

for p in E:
    if p in A and p in B and p in C and p in D:
        E[p] -= 2
        A[p] -= 3
        B[p] -= 3
        C[p] -= 1
        D[p] -= 1
e = 1
for p, exp in E.items():
    e *= p**exp

for p in F:
    if p in B and p in E:
        F[p] -= 2
        B[p] -= 2
        E[p] -= 1
f = 1
for p, exp in F.items():
    f *= p**exp

for p in G:
    if p in A and p in C and p in E:
        G[p] -= 1
        A[p] -= 3
        C[p] -= 2
        E[p] -= 2
g = 1
for p, exp in G.items():
    g *= p**exp

# print the solutions
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")
print(f"e = {e}")
print(f"f = {f}")
print(f"g = {g}")
