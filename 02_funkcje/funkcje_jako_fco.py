
def mean(lista):
    return sum(lista)/len(lista)

functions = [sum, min, max, mean]

dane = [1, 2, 3, 4, 5]

print(dir(mean))

for func in functions:
    print(func.__name__, func(dane))