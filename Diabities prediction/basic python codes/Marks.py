a=int(input("Enter the Marks of 1st Student"))
b=int(input("Enter the Marks of 2nd Student"))
c=int(input("Enter the Marks of 3rd Student"))
d=int(input("Enter the Marks of 4th Student"))
e=int(input("Enter the Marks of 5th Student"))
avg = (a+b+c+d+e)/5
print("The Average Marks Is "+str(avg))
if avg>75 and avg<=100:
    print("The student is Passed with 1st Class")
elif avg>60 and avg<=75:
    print("The student is Passed with 2nd Class")
elif avg>35 and avg<=60:
    print("The student is Passsed with Pass Class")
else:
    print("The student is Failed")
    
