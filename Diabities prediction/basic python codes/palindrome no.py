n=int(input("Enter the number"))
t=n
R=0
while n!=0:
    d=n%10
    R=R*10+d
    n=n//10
    
if t==R:
    print("The number is a Palindrome number")
else:
    print("The number is not a palindrome number")
    
