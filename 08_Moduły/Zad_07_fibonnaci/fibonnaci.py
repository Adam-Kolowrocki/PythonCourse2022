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
        seq_list = []
        for i in range(2, n + 1):
            seq_list.append('F')
            seq_list.append(i)
            seq_list.append(())
            print(seq_list)



fibo(n)
