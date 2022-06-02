# Kolejnym warunkiem, aby dostać “żółte tablice”, jest to,
# aby samochód posiadał co najmniej 75% oryginalnych części.
# W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
#     Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
#             dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
#             ponownie wyświetl zmieniony słownik
#     Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również
#     od jego oryginalności. Dopisz odpowiednie komunikaty.

car_dict = {'marka' : 'Audi',
            'model' : 'Q7',
            'rocznik' : 1997,
            'czy-oryginalny' : False}
print(car_dict)

if 2022 - car_dict['rocznik'] < 25 and car_dict['czy-oryginalny'] == False:
    print(f'Twój samochód {car_dict["marka"]} jest jeszcze zbyt młody i ma za mało oryginalnych części.')
elif 2022 - car_dict['rocznik'] < 25 and car_dict['czy-oryginalny'] == True:
    print(f'Twój samochód {car_dict["marka"]} ma wystarczająco dużo oryginalnych części ale jest jeszcze zbyt młody.')
elif 2022 - car_dict['rocznik'] >= 25 and car_dict['czy-oryginalny'] == False:
    print(f'Twój samochód {car_dict["marka"]} jest już bardzo stary, ale ma za mało oryginalnych części')
else:
    print(f'Gratulacje! Twój samochód {car_dict["marka"]} może być zarejestrowany jako zabytek.')