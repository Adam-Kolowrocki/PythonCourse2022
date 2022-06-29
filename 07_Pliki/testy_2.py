with open('save.txt', 'w') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')
    f.write('Line 3\n')
    f.write('Line 4\n')
    f.write('Line 5\n')
    f.write('The End!')

print('-----------------------------------------------------------------------')
sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']
with open('save.txt', 'w') as fi:
    fi.write('\n'.join(sweets_list))
