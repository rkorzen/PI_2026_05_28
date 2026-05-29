"""

Stworz funkcje hello, ktora zachowa sie nastepujaco:

hello() -> "Hello World"
hello("Rafal") -> "Hello Rafal"
hello("Welcome", "Rafal") -> "Welcome Rafal"
hell(greeting="Welcome") -> "Welcome World"
"""

def hello(name="World", greeting="Hello"):
    # if name!="World" and greeting != "Hello":
    #     greeting, name = name, greeting
    return f"{greeting} {name}"


if __name__ == "__main__":
    assert hello() == "Hello World", "zly tekst"
    assert hello("Rafal") == "Hello Rafal"
    assert hello("Rafal", "Welcome") == "Welcome Rafal"
    assert hello(greeting="Welcome") == "Welcome World"