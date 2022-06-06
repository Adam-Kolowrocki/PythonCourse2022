# Wykorzystaj plik zawierający fragment Pana Tadeusza.
# Znajdź najdłuższe słowo występujące w zadanym fragmencie.

with open('inwokacja.txt') as fopen:
    content = fopen.read()
    content = content.replace(',', '')
    content = content.replace('!', '')
    content_list = content.split()
    for word in content_list:


