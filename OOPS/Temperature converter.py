class TemperatureConverter:

  @staticmethod
  def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
  
  @staticmethod
  def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
  
  @staticmethod
  def celsius_to_kelvin(celsius):
    return celsius + 273.15
  
  @staticmethod
  def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
  
  @staticmethod
  def fahrenheit_to_kelvin(fahrenheit):
    celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
    return TemperatureConverter.celsius_to_kelvin(celsius)
  


if __name__ == "__main__":
  # f = TemperatureConverter.celsius_to_fahrenheit(100)
  # c = TemperatureConverter.fahrenheit_to_celsius(100)
  # k = TemperatureConverter.celsius_to_kelvin(100)
  # print(f'100°C to Fahrenheit:{f:.2f}')
  # print(f'100°F to Celsius:{c:.2f}')
  # print(f'100°C to kelvin: {k:.2f}')

  print("Temperature Converter")
  print("1. Celsius to Fahrenheit")
  print("2. Fahrenheit to Celsius")
  print("3. Celsius to Kelvin")
  print("4. Fahrenheit to Kelvin")

  choice  = input("Enter your choice (1-4): ")

  if choice == "1":
    c = float(input("Enter temperature in celsius: "))
    result = TemperatureConverter.Celsius_to_fahrenheit(c)
    print(f"{c}°C = {result:.2f}°F")

  elif choice == "2":
    f = float(input("Enter temperature in fahrenheit: "))
    result = TemperatureConverter.fahrenheit_to_celsius(f)
    print(f"{f}°F = {result:.2f} K")

  elif choice == "3":
        c = float(input("Enter temperature in Celsius: "))
        result = TemperatureConverter.celsius_to_kelvin(c)
        print(f"{c}°C = {result:.2f} K")

  elif choice == "4":
        f = float(input("Enter temperature in Fahrenheit: "))
        result = TemperatureConverter.fahrenheit_to_kelvin(f)
        print(f"{f}°F = {result:.2f} K")

  else:
        print("Invalid choice!")  