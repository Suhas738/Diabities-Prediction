n=int(input("Enter the number"))
sum=0

ori=n
while n!=0:
    a=n%10
    sum=sum+a**3
    n=n/10
if ori==sum:
    print("The number is Armstrong Number")
else:
    print("The number is not an Armstrong Number")

