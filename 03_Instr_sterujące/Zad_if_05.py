# Stwórz zmienną password. Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 małą literę, 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input('Podaj hasło, musi ono mieć długość conajmniej 8 znaków i zawierać conajmniej 1 wielką i conajmniej 1 małą literę:')

if len(password) < 8:
    print('Hasło jest za krótkie, powinno zawierać conajmniej 8 znaków')

if (password.isdigit() or password.isalpha()):
    print('Hasło musi zawierać conajmniej jedna cyfrę i conajmniej jedną literę')

if (password.islower() or password.isupper()):
    print('Hasło musi zawierać conajmiej jedną wielką literę i conajmniej jedną małą literę.')
