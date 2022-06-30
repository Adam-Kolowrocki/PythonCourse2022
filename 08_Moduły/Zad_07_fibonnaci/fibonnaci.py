n = 5


def fibo(n):
    if n == 0:
        sequence = {'F0': 0}
        return sequence
    elif n == 1:
        sequence = {'F0': 0, 'F1': 1}
        return sequence
    elif n > 1:
        sequence = {'F0': 0, 'F1': 1}
        for i in range(2, n + 1):
            for key, val in sequence:
                key = 'F'[i], val = F[i -1] + F[i - 2]


        sequence.append((i - 1) + (i - 2))       #  F{i}=(i + (i - 1))
        print(sequence)
        return sequence


fibo(n)
