even_sum = 0
odd_sum = 0

while True:
    str = input("Podaj liczbę całkowitą: ")
    if str == "":
        break
    number = int(str)
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

print("Suma liczb parzystych:", even_sum)
print("SUma liczb nieparzystych:", odd_sum)
