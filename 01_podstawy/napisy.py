""
''
""""""
''''''

napis1 = "Napis" \
"ma" \
"wiele" \
"linii"

napis2 = (
    "Napis"
    "ma"
    "wiele"
    "linii"
)


napis3 = """
Napis
ma
wiele
linii
"""


napis4 = '''
Napis
ma
wiele
linii
'''

## laczenie napisow
a = "a"
b = "b"

n1 = a + " " + b 

## formatowanie napisow
n2 = "%s %s" % (a, b)
n3 = "{} {}".format(a, b)

n4 = "{x} {y}".format(x=a, y=b)

n5 = f"{a} {b}"


## przyklad z liczbami
a = 11
b = 10000.223

## formatowanie napisow
n2 = "%.2f\n%.2f" % (a, b)
n3 = "{:.2f}\n{:.2f}".format(a, b)

n4 = "{x:.2f}\n{y:.2f}".format(x=a, y=b)

n5 = f"{a:^10.2f}\n{b:^10.2f}"


# ogolnie - po zmiennej dajemy :
# ^ - centrowanie
# < - wyrownanie do lewej
# > - wyrownanie do prawej
# mozemy okreslic szerokosc -  podajac liczbe
# w tym przypadk 10
# d - decimal
# f - float
# w przypadku float dajemy precyzje .2


print(n5)


# https://pyformat.info/