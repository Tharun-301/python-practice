temp = int(input('Enter the temperature: '))
if temp == 25:
  print('Normal')
else:                  #elif temp<25:                      
  if temp<25:             #print('cold')
    print('Cold')
  else:
    print('Hot')   
