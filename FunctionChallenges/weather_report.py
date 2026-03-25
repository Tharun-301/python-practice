def get_weather_report(temp):
  
  if temp < 22:
    report = 'Cold'
  elif temp >= 22 and temp < 35:
    report = 'Warm'  
  else:
    report = 'Hot'
  return report

temp = int(input('Enter the temperature: '))
result = get_weather_report(temp)  
print(result)