a=int(input("Enter the number of your choice"))
if a>0 and a<=9:
    print("This is a Single Digit number")
elif a>9 and a<=99:
    print("This is a 2 Digit number")
elif a>99 and a<=999:
    print("This is a 3 Digit number")
else:
    print("This number is more than three digit")
