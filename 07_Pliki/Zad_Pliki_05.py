# Wykorzystaj plik zawierający fragment Pana Tadeusza.
# Znajdź najdłuższe słowo występujące w zadanym fragmencie.

with open('inwokacja.txt') as fopen:
    content = fopen.read()
    content = content.replace(',', '')
    content = content.replace('!', '')
    content = content.replace(';', '')
    content = content.replace('(', '')
    content = content.replace(')', '')
    content = content.replace('.', '')
    content_list = content.split()
    word_dict = {}  # {index słowa : długość słowa}
    for i in range(0, len(content_list)):
        word_dict[i] = len(content_list[i])
    longest_word_idx = max(word_dict, key=word_dict.get)
print('\n')
print(f'Najdłuższym słowem w pliku "inwokacja.txt" jest: "{content_list[longest_word_idx]}".')
print('\n')
print(f'I jest to {longest_word_idx + 1} słowo w tym tekście.')




