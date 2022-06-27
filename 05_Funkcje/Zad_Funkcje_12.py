# Napisz program, który będzie sprawdzał,
# czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
#     Program zacznie ze stworzonym słownikiem o trzech kluczach:
#             marka (str)
#             model (str)
#             rocznik (int)
#
#     Wypisze ten słownik na ekran (bez żadnego formatowania)
#     Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
#     “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#     Jeśli nie spełnia powyższego warunku, wypisze komunikat:
#         “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#     Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!),
#     aby zobaczyć, czy progam również zmienia swoje zachowanie.

car_dict = {'marka' : 'Audi',
            'model' : 'Q7',
            'rocznik' : 1997}
print(car_dict)

if 2022 - car_dict['rocznik'] < 25:
    print(f'Twój samochód {car_dict["marka"]} jest jeszcze zbyt młody.')
else:
    print(f'Gratulacje! Twój samochód {car_dict["marka"]} może być zarejestrowany jako zabytek.')