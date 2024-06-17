#ques23": Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
temp_celsius=float(input("Enter the temperature in Celsius: "))
temp_fahrenheit=float(input("Enter the temperature in Fahrenheit: "))
#celsius to fahrenheit
fahrenheit=(temp_celsius*9/5) + 32
#fahrenheit to celsius
celsius=(temp_fahrenheit-32)*5/9
print("Temperature in Fahrenheit: ",fahrenheit,"°F")
print("Temperature in Celsius: ",celsius,"°C")