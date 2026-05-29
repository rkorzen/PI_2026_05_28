# import sys
# # sys.path.insert(0, "c:\\")
# print(sys.path)
#
# import hello_world
#
# print(dir(hello_world))
#
# hello_world.wypisz_zawartosc_pliku("hello_world.py")
#
# from hello_world import wypisz_zawartosc_pliku
#
# wypisz_zawartosc_pliku()
#
#
# from hello_world import wypisz_zawartosc_pliku as rf
#
# rf()

#  from hello_world import *    - tak nie robimy, chyba ze bardzo chcem i wiemy co robimy

# import hello_world
# import inny_modul
# import pandas as pd  # zastosowanie aliasu dla calego modudlu
#
# hello_world.foo()
# inny_modul.foo()


from hello_world import foo as foo1
from inny_modul import foo as foo2

foo1()