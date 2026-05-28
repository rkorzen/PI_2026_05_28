"""
Zadanie - przepisz to z wykorzystanie slownika

Poszedłeś do sklepu i kupiłeś kilka produktów na wagę.

Produkty:
Ser żółty — 32.50 zł/kg — kupiłeś 0.45 kg
Szynka — 41.90 zł/kg — kupiłeś 0.30 kg
Chleb — 5.99 zł/kg — kupiłeś 2kg
Pomidory — 8.40 zł/kg — kupiłeś 0.75 kg

Zadanie
Utwórz zmienne dla:
nazw produktów
cen
ilości / wagi
Oblicz koszt każdego produktu.
Oblicz łączną kwotę zakupów.
Wyświetl raport w formie paragonu.
Oczekiwany efekt

============ PARAGON ============

Ser żółty      0.45 kg x 32.50 zł = 14.63 zł
Szynka         0.30 kg x 41.90 zł = 12.57 zł
Chleb          2.00 kg x  5.99 zł = 11.98 zł
Pomidory       0.75 kg x  8.40 zł =  6.30 zł

---------------------------------
SUMA:                               45.48 zł
=================================
"""

pr_1 = dict(
    nazwa = "Ser żółty",
    cena = 32.50,
    waga = 0.45,
)

pr_2 = dict(
    nazwa = "Szynka",
    cena = 41.9,
    waga = 0.3,
)

pr_3 = dict(
    nazwa = "Chleb",
    cena = 5.99,
    waga = 2,
)

pr_4 = {
    "nazwa": "Pomidory",
    "cena": 8.4,
    "waga": 0.75
}

pr_5 = {
    "nazwa": "Ogorki",
    "cena": 8.1,
    "waga": 0.75
}

produkty = [pr_1, pr_2, pr_3, pr_4, pr_5]

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

suma = 0
for p in produkty:
    suma += policz_naleznosc(p)

linie = []  # append

linia_1 = utworz_linie(pr_1)
linia_2 = utworz_linie(pr_2)
linia_3 = utworz_linie(pr_3)
linia_4 = utworz_linie(pr_4)



raport = f"""
============ PARAGON ============
{"\n".join(linie)}
---------------------------------
SUMA:{suma:>47.2f} zł
=================================
"""

print(raport)