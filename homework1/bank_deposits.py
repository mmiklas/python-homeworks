# Napisz skrypt pozwalający zasymulować zyski z lokat bankowych przy następujących założeniach:
# - własne środki 30 tys. zł,
# - roczna lokata kapitału,
# - kwartalna kapitalizacja odsetek (saldo będzie aktualizowane co 3 miesiące),
# - oprocentowanie roczne dla 3 wariantów: 7,5%, 8% oraz 8,25%,
# - pokazać salda po każdym kwartale,
# - wyliczyć roczny zysk.

own_funds = 30_000

# wariant 1 (7,5%)
annual_interest = 7.5  # oprocentowanie roczne
quarterly_interest = annual_interest / 4  # oprocentowanie kwartalne
balance = own_funds
print("Oprocentowanie roczne " + str(annual_interest) + "%")
print("Saldo początkowe ", balance, "zł")

balance *= (1 + quarterly_interest / 100)
print("Saldo po I kwartale", round(balance, 2), "zł")
balance *= (1 + quarterly_interest / 100)
print("Saldo po II kwartale", round(balance, 2), "zł")
balance *= (1 + quarterly_interest / 100)
print("Saldo po III kwartale", round(balance, 2), "zł")
balance *= (1 + quarterly_interest / 100)
print("Saldo po IV kwartale", round(balance, 2), "zł")
print("Zysk po roku", round(balance - own_funds, 2), "zł")

print()

# wariant 2 (8%)
annual_interest = 8  # oprocentowanie roczne
quarterly_interest = annual_interest / 4  # oprocentowanie kwartalne
balance = own_funds
print("Oprocentowanie roczne " + str(annual_interest) + "%")
print("Saldo początkowe ", balance, "zł")

balance *= (1 + quarterly_interest / 100)
print("Saldo po I kwartale", round(balance, 2), "zł")
balance *= (1 + quarterly_interest / 100)
print("Saldo po II kwartale", round(balance, 2), "zł")
balance *= (1 + quarterly_interest / 100)
print("Saldo po III kwartale", round(balance, 2), "zł")
balance *= (1 + quarterly_interest / 100)
print("Saldo po IV kwartale", round(balance, 2), "zł")
print("Zysk po roku", round(balance - own_funds, 2), "zł")

print()

# wariant 3 (8,25%)
annual_interest = 8.25  # oprocentowanie roczne
quarterly_interest = annual_interest / 4  # oprocentowanie kwartalne
balance = own_funds
print("Oprocentowanie roczne " + str(annual_interest) + "%")
print("Saldo początkowe ", balance, "zł")

balance *= (1 + quarterly_interest / 100)
print("Saldo po I kwartale", round(balance, 2), "zł")
balance *= (1 + quarterly_interest / 100)
print("Saldo po II kwartale", round(balance, 2), "zł")
balance *= (1 + quarterly_interest / 100)
print("Saldo po III kwartale", round(balance, 2), "zł")
balance *= (1 + quarterly_interest / 100)
print("Saldo po IV kwartale", round(balance, 2), "zł")
print("Zysk po roku", round(balance - own_funds, 2), "zł")
