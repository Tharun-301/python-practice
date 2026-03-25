dayNo = int(input('Enter the day number: '))
match dayNo:
  case 0:
    print('Monday')
  case 1:
    print('Tuesday')
  case 2:
    print('Wednesday') 
  case 3:
    print('Thursday')    
  case 4:
    print('Friday')
  case 5:
    print('Saturday') 
  case 6:
    print('Sunday')
  case _:
    print('Invalid Day Number')
     