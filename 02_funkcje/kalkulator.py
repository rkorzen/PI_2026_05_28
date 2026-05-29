"""
Stworz kalkulator

musisz stworzyc kilka funkcji

add, sub, mul, div,

get_data - pobiera dane od uzytkownika

main - ta funkcja spina w calosc. podejmuje decyzje jaka funkcje arytmetyczna wywolac na podstawie tego
co zwroci get_data

$ - tzn uruchamiamy w command line

$ python kalkulator.py
Podaj rodzaj operacji (+-/*): +
Podaj arg a: 10
Podaj arg b: 5
Wynik a + b = 15

"""

def get_data():
    operacja = input(...)
    a = input(...)
    b = input(...)

    return operacja, int(a), int(b)

def add(a, b): ...

...


def main():
    print("Kalkulator v1.0")
    op, a, b = get_data()
    # tutaj logika kalkulator



if __name__ == "__main__":
    main()