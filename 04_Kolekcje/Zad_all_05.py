# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
# Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce.
#
# Zadbaj o sposób wyświetlania np.:
#
#     szybko : 5
#     zbudź : 1

poet = 'Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce'
poet = poet.replace(',', '')
poet_lo = poet.lower()

poet_list = poet_lo.split()
poet_list_counter = {}

for word in poet_list:
    if word in poet_list_counter:
        poet_list_counter[word] += 1
    else:
        poet_list_counter[word] = 1

for k, v in poet_list_counter.items():
    print(f'- {k} : {v}')
