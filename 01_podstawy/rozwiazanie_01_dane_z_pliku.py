"""
Zadanie - przepisz to z wykorzystanie slownika

"""

produkty = []

def policz_naleznosc(produkt):
    cena = produkt["cena"]
    waga = produkt["waga"]
    naleznosc = cena * waga
    return naleznosc

def utworz_linie(produkt, max_len=25):
    nazwa = produkt["nazwa"]
    cena = produkt["cena"]
    waga = produkt["waga"]
    naleznosc = policz_naleznosc(produkt)
    return f'{nazwa:{max_len}} {waga:7.2f} kg x {cena:7.2f} zł = {naleznosc:7.2f} zł'

def najdluzsza_dlugosc(products):
    max_len = 0
    for p in products:
        new_len = len(p["nazwa"])
        if new_len > max_len:
            max_len = new_len
    return max_len

### dodaj odczyt z pliku
### zignoruj 1 wiersz
### if line.startswith("nazwa;"):
###     continue
with open("dane.csv", encoding="utf-8-sig") as f:
    for line in f:
        if line.startswith("nazwa"):
            continue
        raw_row = line.split(";") # to jest lista
        if len(raw_row) != 3:
            continue
        try:
            product = {
                "nazwa": raw_row[0],
                "cena": float(raw_row[1]),
                "waga": float(raw_row[2])
            }
            produkty.append(product)
        except ValueError:
            print("Ignorujemy linie: ", line)

max_len = najdluzsza_dlugosc(products=produkty)

suma = 0
for p in produkty:
    suma += policz_naleznosc(p)

linie = []  # append
for p in produkty:
    linie.append(utworz_linie(p, max_len))

raport = f"""
============ PARAGON ============
{"\n".join(linie)}
---------------------------------
SUMA:{suma:>47.2f} zł
=================================
"""

print(raport)