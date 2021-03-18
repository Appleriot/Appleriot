
try:
    num = int(input(""))
    num2 = int(input(""))
    result = num + num2
except ValueError:
    print("Please enter a number")
else:
    print(f"{result}")
