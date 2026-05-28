"""
Zadanie — Paragon ze sklepu

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

nazwa_1 = "Ser żółty"
cena_1 = 32.50
waga_1 = 0.45
naleznosc_1 = cena_1 * waga_1

nazwa_2 = "Szynka"
cena_2 = 41.9
waga_2 = 0.3
naleznosc_2 = cena_2 * waga_2

nazwa_3 = "Chleb"
cena_3 = 5.99
waga_3 = 2
naleznosc_3 = cena_3 * waga_3


nazwa_4 = "Pomidory"
cena_4 = 8.4
waga_4 = 0.75
naleznosc_4 = cena_4 * waga_4


linia_1 = f"{nazwa_1:25} {waga_1:.2f} kg x {cena_1:5.2f} zł = {naleznosc_1:5.2f} zł"
linia_2 = f"{nazwa_2:25} {waga_2:.2f} kg x {cena_2:5.2f} zł = {naleznosc_2:5.2f} zł"
linia_3 = f"{nazwa_3:25} {waga_3:.2f} kg x {cena_3:5.2f} zł = {naleznosc_3:5.2f} zł"
linia_4 = f"{nazwa_4:25} {waga_4:.2f} kg x {cena_4:5.2f} zł = {naleznosc_4:5.2f} zł"

suma = naleznosc_1 + naleznosc_2 + naleznosc_3 + naleznosc_4

raport = f"""
============ PARAGON ============
{linia_1}
{linia_2}
{linia_3}
{linia_4}
---------------------------------
SUMA:{suma:>47.2f} zł
=================================
"""

print(raport)