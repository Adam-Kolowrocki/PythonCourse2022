# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""
#
# Zadbaj o sposób wyświetlania np.:
#
#     szybko : 5
#
#     zbudź : 1

poet = 'Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce'
poet = poet.replace(',', '')
poet_lo = poet.lower()

poet_list = poet.split()
words

for word in poet_list:
    print(poet_list)
