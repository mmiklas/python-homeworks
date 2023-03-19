import random

min = int(input("Podaj minimum: "))
max = int(input("Podaj maksimum: "))


series_total = random.randint(min, max)
while series_total:
    series = []
    numbers_total = random.randint(min, max)
    while numbers_total:
        number = random.randint(min, max)
        series.append(number)
        numbers_total -= 1
    print(series)
    series_total -= 1
