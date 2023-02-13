# Napisz skrypt pomagający oszacować ile godzin potrzeba na pobranie danych z sieci o rozmiarze 13 TB jeżeli wiesz,
# że plik o rozmiarze 194 MB udało się pobrać w 5 sekund. Wynik zaokrąglij do pełnych godzin.

# 1 TB = 1024 GB
# 1 GB = 1024 MB
# 1 godz. = 60 min.
# 1 min. = 60 sec.

data_size_tb = 13
data_size_mb = data_size_tb * 1024 * 1024
result_time_sec = data_size_mb / 194 * 5
result_time_hour = result_time_sec / 3600

print("Dane o rozmiarze 13 TB można pobrać w ", int(round(result_time_hour, 0)), "godzin.")
