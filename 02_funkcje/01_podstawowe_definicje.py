"""
def <nazwa_funkcji>([argumenty pozycyjne][argumenty nazwane]):
    [blok instrukcji]
    [return ...] - to konczy dzialanie funkcji
tu juz jeste poza funkca
"""
# definicja
def foo():
    pass

# obiekt funkcji
foo
print(type(foo))

# wywolanie
foo()


def funkcja_z_return():
    return 10
    print("xxx") # to sie nigdy nie wykonca

funkcja_z_return()
print(funkcja_z_return())


def czy_wieksze_niz(a, b):
    if a > b:
        return True
    return False

print(czy_wieksze_niz(a=3, b=5))
print(czy_wieksze_niz(b=5, a=3))
print(czy_wieksze_niz(5, 3))


def czy_wieksze_niz(a, b=0):
    if a > b:
        return True
    return False

czy_wieksze_niz(5)
czy_wieksze_niz(5, 10)