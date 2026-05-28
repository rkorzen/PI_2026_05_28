# tuple - niemutowalna

#     0  1     2       3 to sa indexy
t1 = (1, "sd", "2323", 1 )
print(t1)
print(dir(t1))
help(t1.count)
print(t1.count(1))
print(t1.count("xyz"))

print(t1.index("sd"))
print(t1[2])
print(t1[-1])
#     0  1  2  3  4  5  6  7    8
t2 = (1, 2, 3, 4, 5, 6, 7, "a", "5")

print(t2[3:6])  # z lewej strony przedzial domkniety, z prawej otwarty

print(t2[-6:-3])  # z lewej strony przedzial domkniety, z prawej otwarty

print(t2[-3:-6])  # z lewej strony przedzial domkniety, z prawej otwarty
# [poczatek:koniec:krok]

t2[0], t2[7]

print(t2[::2])

# list


t1 = [1, "sd", "2323", 1 ]
print(t1)
print(dir(t1))
help(t1.count)
print(t1.count(1))
print(t1.count("xyz"))

print(t1.index("sd"))
print(t1[2])
print(t1[-1])
#     0  1  2  3  4  5  6  7    8
t2 = [1, 2, 3, 4, 5, 6, 7, "a", "5"]

print(t2[3:6])  # z lewej strony przedzial domkniety, z prawej otwarty

print(t2[-6:-3])  # z lewej strony przedzial domkniety, z prawej otwarty

print(t2[-3:-6])  # z lewej strony przedzial domkniety, z prawej otwarty
# [poczatek:koniec:krok]

t2[0], t2[7]

print(t2[::2])

## roznice - lista jest modyfikowalna
### append, insert, pop, remove

t2.append(20)

t2.extend([1, 2, 3])

# t2.remove()


###

x = [1, 2, 3]
y = x

y.append(4)

print(id(x), id(y))
print(x)  # tutaj x i y wskazuja na to samo. zmiana x zmienia y i odwrotnie

x = [2, 3, 4]
print(id(x), id(y))



x = [1, 2, 3]
y = x.copy()  # shallow copy

print(id(x), id(y))

a = [1, 2]
x = [1, 2, 3, a]
y = x.copy()  # shallow copy

print(a, x, y, sep="\n")

x.append(10)

print(a, x, y, sep="\n")

a.append(11230)

print(a, x, y, sep="\n")

### deep copy
import copy


a = [1, 2]
x = [1, 2, 3, a]
y = copy.deepcopy(x)  # shallow copy

print(a, x, y, sep="\n")

x.append(10)

print(a, x, y, sep="\n")

a.append(11230)

print(a, x, y, sep="\n")

### mozemy w liscie nadpisywac elementy

x[0] = "Ala ma kota"
print(x)

tx = tuple(x)
print(tx[0])
# tx[0] = "kot ma ale"

# dict
# klucze - unikalne, hashowalne

d = {
    1: ["a", "b"],
    2: "b",
    "c": {"x": "y"}
}


pr_1 = {
    "nazwa": "Ser",
    "cena": 1.23,
    "waga": 2.45
}

pr_1["waga"]

print(pr_1.keys())
print(pr_1.values())
print(pr_1.items())

d = [('nazwa', 'Ser'), ('cena', 1.23), ('waga', 2.45)]
print(type(d[1]))

print(dict(d))

print(
    dict(nazwa="x", cena=1.23)
)



print("nazwa" in pr_1)
pr_1["nazwa"] = "Ser korycinski"
pr_1["alergeny"] = ["xsxs"]

print(pr_1)

### pod gorke

zamowienie = {
    "nazwy": ["Ser", "szynka"],
    "ceny": [1.23, 4.56]
}

zamowienie["nazwy"].append("mleko")
zamowienie["ceny"].append(1.62)

print(zamowienie)

del zamowienie["nazwy"][1]
del zamowienie["ceny"][1]
# set (frozenset)

produkty = [
    {"nazwa": "Ser", "cena": 1.23},
    {"nazwa": "Szynka", "cena": 17.23},
]


testowe_dane = []

for i in range(100):
    pr = {
        "nazwa": f"produkt_{i}",
        "cena": i+100
    }

    testowe_dane.append(pr)

wybrane = []
for produkt in testowe_dane:
    nazwa = produkt["nazwa"]
    suffix = int(nazwa.split("_")[1])
    if suffix % 2 == 0:
        wybrane.append(produkt)




produkt_1 -> produkt, 1
