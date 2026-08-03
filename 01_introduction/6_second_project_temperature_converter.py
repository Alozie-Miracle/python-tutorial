temperature_fahrenheit = input("Enter the temperature in Fahrenheit: ")

temperature_celsius = (float(temperature_fahrenheit) - 32) * 5/9
temperature_celsius = round(temperature_celsius, 2)
print(f"{temperature_fahrenheit}°F is equivalent to {temperature_celsius}°C")