temp = input("Enter the temperature you want to convert (e.g., 45F, 102C): ")

value = float(temp[:-1])      # get the number
unit = temp[-1].upper()      # get the unit (C or F)

if unit == "F":
    celsius = (value - 32) * 5 / 9
    print("The temperature in Celsius is", round(celsius), "degrees.")
elif unit == "C":
    fahrenheit = (value * 9 / 5) + 32
    print("The temperature in Fahrenheit is", round(fahrenheit), "degrees.")
else:
    print("Invalid unit. Please use C or F.")



    
