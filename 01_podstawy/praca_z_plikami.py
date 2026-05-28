# try:
#     f = open("danexxxx.csv", encoding='utf-8-sig')
#     for line in f:
#         print(line)
#     1/0
# except:
#     print("Brak pliku")
#     asas
# finally:
#     f.close()

import sys

print(sys.argv)
nazwa = sys.argv[1]

with open(nazwa) as f:
    for line in f:
        ...
        # print(line)

