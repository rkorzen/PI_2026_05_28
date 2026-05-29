"""
przerob to tak, by skorzystac ze slownika zamiast z ifow w main

"""
OPERATIONS = "+-/*"

def _get_operation():
    while True:
        operacja = input(f"Podaj rodzaj operacji ({OPERATIONS})")
        if operacja not in OPERATIONS:
            print("Niepoprawna wartosc. Sproboj ponownie")
            continue
        return operacja

def _get_argument(label="a", exclude=None):
    """
    exclude: lista niedozwolonych wartosci
    """
    while True:
        x = input(f"Podaj {label}: ")

        if x.isdecimal():
            x = int(x)
            if exclude and x in exclude:
                continue
            return x


def get_data():

    operacja = _get_operation()
    a = _get_argument(label="a")
    if operacja == "/":
        b = _get_argument(label="b", exclude=[0])
    else:
        b = _get_argument(label="b")

    return operacja, int(a), int(b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def main():
    print("Kalkulator v1.0")
    op, a, b = get_data()
    # tutaj logika kalkulator

    if op == "+":
        wynik = add(a, b)
    elif op == "-":
        wynik = sub(a, b)
    elif op == "*":
        wynik = mul(a, b)
    elif op == "/":
        wynik = div(a, b)
    else:
        print("Nieznana operacja")
        return

    print(f"Wynik: {a} {op} {b} = {wynik}")

if __name__ == "__main__":
    main()