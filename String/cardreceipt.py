cardno = input('Enter the card number: ')
lastdigit = cardno[15: ]
four = 'X' * 4 + ' '
disp = four * 3 + lastdigit
print(disp)