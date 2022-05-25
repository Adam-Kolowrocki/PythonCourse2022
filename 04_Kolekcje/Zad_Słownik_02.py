# Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe.
# Przekształć ją w słownik dict_from_tuples.

tuples_to_dict = [
    ('apple', 'jabłko'),
    ('peer', 'gruszka'),
    ('chery', 'wiśnia')
]

dict_from_tuples = dict(tuples_to_dict)

print(dict_from_tuples)
print(type(dict_from_tuples))