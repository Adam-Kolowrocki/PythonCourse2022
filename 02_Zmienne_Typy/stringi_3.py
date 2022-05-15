#zadanie 3
quote = 'Honesty is the first chapter in the book of wisdom.'

print('Liczba liter w ciągu wynosi: ', len(quote))

print(quote[-7:-1])

id_half = len(quote)//2
print(quote[:id_half+1])
print(quote[50:])

print(quote[id_half::3])

print(quote[::2])

print(quote[::-1])

new_quote = quote.replace('wisdom', 'friendship')
print(new_quote)
