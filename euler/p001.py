# problem 1
ns = range(1000)
print(ns)
s = 0
for n in ns:
    if n % 3 == 0 or n % 5 == 0:
        s += n

print(s)

f = lambda x : x % 3 == 0 or x % 5 == 0

print(filter(f, ns))

print(sum(filter(f, ns)))