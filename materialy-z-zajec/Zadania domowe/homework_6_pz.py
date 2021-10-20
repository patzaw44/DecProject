"""Zadanie 6

Zapytaj użytkownika o wynik meczu. Oczekiwany format odpowiedzi to np. 2:0 albo 1:1 albo 1:4.
Program na podstawie podanego wyniku powinien opisać wynik meczu

Przykładowo
2:0 => gospodarze wygrali dwoma bramkami

1:1 => padł remis

1:4 => goście wygrali trzema bramkami

Program powinien oczywiscie obsługiwać wyniki również poza tymi, które zostały wymienione."""

score = input("Podaj wynik meczu, w formacie x:x  -> ")
team_a = int(score[0])
team_b = int(score[-1])
# print(team_a)
# print(team_b)
# print(score)

if team_a > team_b:
    print(f"{score} -> gospodarze wygrali {team_a} bramkami")
elif team_a == team_b:
    print(f"{score} -> padł remis")
else:
    print(f"{score} -> goście wygrali {team_b} bramkami")
