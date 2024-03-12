# Chcemy ułożyć wieżę z puszek. Wieża składa się z poziomów, gdzie każdy wyższy poziom wymaga jednej puszki mniej niż poziom na którym go zbudowano.
# Korzystając z rekurencji napisz program, który pozwoli wyliczyć ilość potrzebnych puszek do wybudowania wieży o zadanym poziomie oraz ilość poziomów wieży jakie jesteśmy wstanie ułożyć z dostępnej liczby puszek.
# Przykład: jeżeli chcemy ułożyć 3 poziomową wieżę potrzebujemy 6 puszek a np. mając 10 puszek, ułożymy 4 poziomową wieżę.

# poziom 4      #
# poziom 3     # #
# poziom 2    # # #
# poziom 1   # # # #

# jeżeli liczymy poziomy od góry to zauważmy, że 1 poziom to 1 puszka, 2 poziom to 2 puszki, itd.
# zatem wylicznie liczby puszek to suma poziomów, np. 3 poziom to 3 + 2 + 1 = 6
def calculate_number_of_cans(level):
    if level == 1: # jeżeli poziom 1 to wiadomo, że wystarczy jedna puszka
        return 1
    return level + calculate_number_of_cans(level - 1) # rekurencja czyli bieżemy poziom i dodajemy do niego... i znowu wyznaczamy liczbę puszek, tym razem na poziomie wyższym

# wyliczamy poziom wieży podając liczbę puszek i bieżący poziom czyli na początku 1
# za każdą kolejną "iteracją" odejemujemy od liczby puszek bieżący poziom (patrz obserwacja wyżej) i zwiększamy bieżący poziom
# zagnieżdżanie trwa dopóki liczba puszek jest większa od bieżącego poziomu, bo tyle puszek trzeba, aby ułożyć cały rząd puszek na danym poziomie
def calculate_tower_level(number_of_cans, current_level=1):
    if number_of_cans < current_level:
        return 0
    else:
        return 1 + calculate_tower_level(number_of_cans - current_level, current_level + 1)

print("Ile potrzeba puszek:")
print("1 poziom -", calculate_number_of_cans(1), "puszek")
print("2 poziom -", calculate_number_of_cans(2), "puszek")
print("3 poziom -", calculate_number_of_cans(3), "puszek")
print("4 poziom -", calculate_number_of_cans(4), "puszek")

print()

print("Jak dużą zbudujemy wieżę:")
print("1 puszka - ", calculate_tower_level(1), "poziom")
print("5 puszek - ", calculate_tower_level(5), "poziom")
print("10 puszek - ", calculate_tower_level(10), "poziom")
print("100 puszek - ", calculate_tower_level(100), "poziom")