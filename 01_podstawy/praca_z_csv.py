import csv

with open("dane2.csv") as f:
    reader = csv.reader(f, delimiter=";", quotechar='"')
    for line in reader:
        print(line)



with open("dane2.csv") as f:
    reader = csv.DictReader(f, delimiter=";", quotechar='"')
    for line in reader:
        print(line)


with open("dane.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=";", quotechar='"')
    for line in reader:
        print(line)


dane = [
    ["A", "B", "C"],
    [1, 2, 3]
]

with open("dane3.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(dane)

