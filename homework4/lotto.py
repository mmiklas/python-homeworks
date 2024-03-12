# Napisz kolejną wersję programu do gry w lotto uwzględniając:
# - zasady programowania zorientowanego obiektowo,
# - możliwość podawania typowanych przez użytkownika liczb jako lista,
# - możliwość grania systemem (6-12 liczb).


from random import sample


class Lotto:
    def __init__(self, user_numbers):
        self.__user_numbers = user_numbers
        self.__lucky_numbers = self.__draw_numbers()
        self.__result = self.__check_numbers()
        self.__show_result()

    def __draw_numbers(self):
        lucky_numbers = [i for i in range(1, 50)]
        numbers = sample(lucky_numbers, 6)
        numbers.sort()
        return numbers

    def __check_numbers(self):
        counter = 0
        for number in self.__user_numbers:
            if number in self.__lucky_numbers:
                counter += 1
        return counter

    def __show_result(self):
        print("Podane liczby to: ", self.__user_numbers)
        print("Wylosowano liczby:", self.__lucky_numbers)
        print()
        if self.__result == 6:
            print("GRATULACJE!!!", "Jesteś milionerem!")
        elif self.__result == 5:
            print("BRAWO!", "Trafiono piątkę!", "Zgarniesz sporą sumkę!")
        elif self.__result == 4:
            print("Hurra!", "Trafiono czwórkę!", "To całkiem niezły wynik!")
        elif self.__result == 3:
            print("Trafiono trójkę!", "Przysługuje Ci minimalna wygrana!")
        elif self.__result == 2 or self.__result == 1:
            print("Trafiono {} liczbę. Było bardzo blisko!".format(self.__result))
        else:
            print("To nie jest Twój dzień!")


if __name__ == "__main__":
    Lotto([1, 2, 3, 4, 5, 6])
