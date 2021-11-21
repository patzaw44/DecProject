"""
Zadanie 25

Użyj biblioteki psutil (https://pypi.org/project/psutil/) i napisz funkcję, która sprawdzi, ile procesorów ma komputer,
 na którym właśnie uruchamiany jest ten program.

Dokumentacja psutil dostępna pod https://psutil.readthedocs.io/en/latest/
"""
import psutil


def sprawdz_cpu():
    print(f"Zwraca czasy procesora systemowego - krotka: \n{psutil.cpu_times()}\n")
    print(f"Zwraca wykorzystanie procesora w całym systemie jako procent : \n{psutil.cpu_percent()}\n")
    print(f"Zwraca liczbę logicznych procesorów w systemie: \n{psutil.cpu_count()}\n")
    print(f"Zwraca różne statystyki procesora jako krotkę: \n{psutil.cpu_stats()}\n")
    print(f"Zwraca częstotliwość procesora: \n{psutil.cpu_freq()}")


sprawdz_cpu()
