temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").strip().upper()
if unit == "C":
    print(f"{temp}°C is {(temp * 9/5) + 32:.2f}°F")
elif unit == "F":
    print(f"{temp}°F is {(temp - 32) * 5/9:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
