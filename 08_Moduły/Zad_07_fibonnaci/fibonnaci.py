n = 5


def fibo(n):
    sequence = {'F0': 0, 'F1': 1}
    for i in range(2, n + 1):
        for key, val in sequence:
            key =
        sequence.append((i - 1) + (i - 2))       #  F{i}=(i + (i - 1))
        print(sequence)
    return sequence


fibo(n)
