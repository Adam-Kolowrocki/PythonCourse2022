fule_cost = float(input('Podaj cenę litra paliwa: '))
fule_usage = float(input('Podaj spalanie na 100 km: '))
distance = float(input('Jaki dystans w km zamierzasz przejechać? '))

trip_cost = fule_cost * fule_usage * distance / 100

print('Koszt podróży na dystansie', distance, 'km wyniesie: ', round(trip_cost, 2), 'PLN')
