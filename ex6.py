temp_Fahr = int(input("Informe a temperatura em Fahrenheit: "))

celsius = 5 / 9 + (temp_Fahr - 32)

kelvin = ((temp_Fahr - 32) / 1.8) + 273.15 

print("A coversão para Celsius é", celsius)

print("A coversão para Kelvin é", kelvin)
