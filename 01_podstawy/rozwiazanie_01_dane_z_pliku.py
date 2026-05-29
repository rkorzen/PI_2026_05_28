"""
Zadanie - przepisz to z wykorzystanie slownika

"""

produkty = []


def policz_naleznosc(produkt):
    cena = produkt["cena"]
    waga = produkt["waga"]
    naleznosc = cena * waga
    return naleznosc


def utworz_linie(produkt):
    nazwa = produkt["nazwa"]
    cena = produkt["cena"]
    waga = produkt["waga"]
    naleznosc = policz_naleznosc(produkt)
    return f'{nazwa:25} {waga:.2f} kg x {cena:5.2f} zł = {naleznosc:5.2f} zł'


### dodaj odczyt z pliku
### zignoruj 1 wiersz
### if line.startswith("nazwa;"):
###     continue


suma = 0
for p in produkty:
    suma += policz_naleznosc(p)

linie = []  # append
for p in produkty:
    linie.append(utworz_linie(p))

raport = f"""
============ PARAGON ============
{"\n".join(linie)}
---------------------------------
SUMA:{suma:>47.2f} zł
=================================
"""

print(raport)