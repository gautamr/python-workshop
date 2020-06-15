n = int(input('Enter a number: '))

if n < 0:
    raise ValueError('The value must be positive')

fact = 1
i = 2

while i <= n:
    fact *= i
    i += 1

print(fact)