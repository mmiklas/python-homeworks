# Napisz funkcję, która sprawdza, czy podany ciąg znaków jest palindromem (czy czyta się tak samo od przodu i od tyłu).
# Ignoruj wielkość liter oraz spacje.

def is_palindrom(string):
    string = string.lower().replace(" ", "") # zamieniamy na małe litery i usuwamy spacje
    reversed = string[::-1] # odwrócony ciąg znaków
    return string == reversed

print(is_palindrom("Ala ma kota"))
print(is_palindrom("Kobyła ma mały bok"))
print(is_palindrom("Kajak"))