def get_speed_status(speed):
  if speed < 60 :
    status = 'Normal'
  elif speed >= 60 and speed < 80:
    status = 'Warning'
  else:
    status = 'Over Speed'
  return status  

speed = int(input('Enter the speed: '))
result = get_speed_status(speed)
print(result)


