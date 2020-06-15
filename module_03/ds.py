xs = ["apple", "banana", "cherry"]
xs.reverse()
print(xs)
xs.sort()
print(xs)
print(xs[1:2])
print(xs[1:])

for x in xs:
    print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
