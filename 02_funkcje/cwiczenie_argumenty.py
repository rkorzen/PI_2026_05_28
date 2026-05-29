"""

Stworz funkcje hello, ktora zachowa sie nastepujaco:

hello() -> "Hello World"
hello("Rafal") -> "Hello Rafal"
hello("Welcome", "Rafal") -> "Welcome Rafal"
hell(greeting="Welcome") -> "Welcome World"




"""

def hello(): ...


if __name__ == "__main__":
    assert hello() == "Hello World", "zly tekst"
    assert hello("Rafal") == "Hello Rafal"
    assert hello("Welcome", "Rafal") == "Welcome Rafal"
    assert hello(greeting="Welcome") == "Welcome World"