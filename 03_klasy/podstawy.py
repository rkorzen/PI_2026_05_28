class Product:

    def __init__(self, nazwa, cena, waga):
        self.nazwa = nazwa
        self.cena = cena
        self.waga = waga

    def naleznosc(self):
        return self.waga * self.cena


p = Product("Woda", 1.22, 1.5)

print(p.naleznosc())
