# Find a, b, c, d, e, f, and g, all positive integers greater than 1, that satisfy all equations:
#     a^2 × b × c^2 × g = 5100
#     a × b^2 × e × f^2 = 33462
#     a × c^2 × d^3 = 17150
#     a^3 × b^3 × c × d × e^2 = 914760
# in the fastest way possible, using your language of choice

def prime_factors(n):
    """Return the prime factors of n."""    
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.setdefault(i, 0)
            factors[i] += 1
    if n > 1:
        factors.setdefault(n, 0)
        factors[n] += 1
    return factors

# Find the prime factors of each number
equation_values = [5100, 33462, 17150, 914760]
equation_factors = []
for value in equation_values:
    factors = prime_factors(value)
    print(factors)
    equation_factors.append(factors)

# Powers of variables
a = [2, 1, 1, 3]
b = [1, 2, 0, 3]
c = [2, 0, 2, 1]
d = [0, 0, 3, 1]
e = [0, 1, 0, 2]
f = [0, 2, 0, 0]
g = [1, 0, 0, 0]

# Variables
vars = [a, b, c, d, e, f, g]

results = []
# Assumes that the answers are prime numbers
for var in vars:
    possible_values = {}
    for index, factors in enumerate(equation_factors):
        if var[index] == 0:
            continue
        for prime, power in factors.items():
            if power == var[index]:
                possible_values.setdefault(prime, 0)
                possible_values[prime] += 1
    results.append(possible_values)

print("RESULTS:")
print(results)

# Filter the results
results2 = []
for index, var in enumerate(vars):
    temp = []
    # count number of non-zero powers
    count = sum([1 for x in var if x != 0])
    print("count", count)
    for prime, num_matching_equations in results[index].items():
        if num_matching_equations == count:
            temp.append(prime)
    results2.append(temp)
print(results2)

results3 = []
for result in results2:
    if len(result) == 1:
        results3.append(result[0])
    else:
        results3.append(result)

