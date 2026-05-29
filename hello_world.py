# () po nazwie funkcji oznaczaja wywolanie



x = 1
y = 2

def foo():
    print("foo z hello world")

def wypisz_zawartosc_pliku(nazwa_pliku):
    with open(nazwa_pliku) as f:
        print(f.read())


if __name__ == "__main__":

    print(dir())
    print("__name__ =", __name__)

    print()  # funkcja wbudowanana

    print

    print(x, y, "cos tam", sep="-")

    print("Hello\nWorld")
    print('Hello\n\tWorld')

    print(r"Hello\nWorld")
    print(r'Hello\n\tWorld')
    #input("WPisz cos")

    foo()
    wypisz_zawartosc_pliku("requirements.txt")
