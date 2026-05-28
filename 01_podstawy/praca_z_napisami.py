dane = """Galaretka;23.32;3.38
Kisiel;21.24;0.75
Tofu;84.35;2.9
Mleko kokosowe;43.85;3.94
Ryż basmati;73.15;1.03
Kasza jaglana;10.98;2.21
Soczewica;39.56;2.39
Makrela;66.29;3.4
Śledź;88.6;0.58
Krewetki;37.73;1.76
Mozzarella;77.89;1.32
Parmezan;19.14;2.3
Bagietka;39.41;1.46
Croissant;24.36;4.62
Pączek;41.27;4.32
Drożdżówka;50.65;0.35
Chałka;89.93;4.2"""

data = []

for raw_data in dane.split("\n"):
    raw_row = raw_data.split(";")
    row = {
        "nazwa": raw_row[0],
        "cena": float(raw_row[1]),
        "waga": float(raw_row[2])
    }
    data.append(row)

print(data)


print("-".join(map(str, [1, 2, 3, 4])))