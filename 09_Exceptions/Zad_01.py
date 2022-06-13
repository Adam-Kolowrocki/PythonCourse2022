# Stwórz listę składającą się z kilku elementów różnego typu
# np. [13, ‘string’, 2.45] itp. W pętli spróbuj wykonać dzielenie 10
# przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.
test_list = [12233, 123.133, 'text', 101001110, 0b10, 5j, True, False]

for i in test_list:
    try:
        resoult = 10 / i
        print(resoult)
    except (TypeError, ZeroDivisionError):
        print(f'10/{i} Nie mogę wykonać')
