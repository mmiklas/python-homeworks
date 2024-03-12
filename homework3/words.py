# Napisz grę polegającą na zapamiętywaniu słów. Wylosowany gracz podaje pierwsze słowo a kolejny powtarza słowo i dodaje swoje.
# Następny w kolejce gracz musi podać wszsytkie wcześniejsze słowa w tej samej kolejności i także dodać swoje.
# Rozgrywka kończy się gdy, któryś z graczy popełni błąd. Na ekranie komputera przy każdej turze należy wymazać ekran np. przez wyświetlenie 100 pustych wierszy.

import random


def clear_screen():
    print("\n" * 100)


def define_player(player_number):
    return input("Podaj imię gracza " + str(player_number) + ": ")


def define_players():
    players = []
    number_of_players = int(input("Podaj liczbę graczy: "))
    for i in range(number_of_players):
        players.append(define_player(i + 1))
    return players


def draw_starting_player_no(players):
    return players[random.randint(0, len(players) - 1)]


def show_round_message(words, player):
    print(player + "! Podaj", end=" ")
    if len(words) != 0:
        print("wszystkie wcześniejsze słowa w takiej samej kolejności a na końcu", end=" ")
    print("dodaj nowe słowo:")


def show_losing_message(words, player):
    print("POMYŁKA!", player, "przegrywa! Poprawna sekwencja słów:", words)


def get_words(words, player):
    clear_screen()
    show_round_message(words, player)
    for word in words:
        given_word = input()
        if given_word != word:
            show_losing_message(words, player)
            exit()
    new_word = input()
    words.append(new_word)


def get_next_player_no(players, current_player):
    current_player_no = players.index(current_player)
    if current_player_no >= len(players):
        return players[1]
    else:
        return players[current_player_no + 1]


def start_game():
    words = []
    players = define_players()
    current_player = draw_starting_player_no(players)
    while True:
        get_words(words, current_player)
        current_player = get_next_player_no(players, current_player)


start_game()
