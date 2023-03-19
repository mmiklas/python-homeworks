number = int(input("Podaj liczbę całkowitą: "))
print(bin(number))
print("W ciągu bitów reprezentujących liczbę", number, end=" ")

n = 0
while number:
    n += number & 1
    number = number >> 1

if n == 1:
    print("znajduje się", n, "jedynka.")
elif n > 1 and n < 5:
    print("znajdują się", n, "jedynki.")
else:
    print("znajduje się", n, "jedynek.")
