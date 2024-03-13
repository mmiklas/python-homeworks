# Napisz program, zliczający wystąpienia danego słowa we wskazanym tekście, w tym celu:
# - analizowany tekst wczytaj z pliku tekstowego np. znachor.txt,
# - pobierz od użytkownika szukane słowo,
# - wyświetl liczbę wystąpień szukanego słowa.


file_path = "znachor.txt"
searched_word = input("Podaj słowo: ")
counter = 0

def remove_non_alpha(word):
    clean_word = ""
    for char in word:
        if char.isalpha():
            clean_word += char
    return clean_word

try:
    with open(file_path, "r") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if remove_non_alpha(word).lower() == searched_word:
                    counter += 1
except IOError as e:
    print("Błąd podczas przetwarzania pliku:", e)

print(f'Słowo "{searched_word}" wystąpiło {counter} razy.')
