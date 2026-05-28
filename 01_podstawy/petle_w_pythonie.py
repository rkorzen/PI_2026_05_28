napis = "Ala ma kota"

# while
i=0
while i < len(napis):
    znak = napis[i]
    print(znak)
    i += 1

print("po petli")

dane = 0
while True:
    znak = input("Podaj liczbe lub wcisnij cokolwiek innego by zakonczyc program. Zatwierdze enterem ")
    if znak.isdecimal():
        dane += int(znak)
    else:
        break


# for

for znak in napis:
    print(znak)

print("po petli")