S=str(input("Enter any sentence"))
U=0
L=0
for item in S:
    if item=='A' or item=='B' or item=='C' or item=='D' or item=='E' or item=='F' or item=='G' or item=='H' or item=='I' or item=='J' or item=='K' or item=='L' or item=='M' or item=='N' or item=='O' or item=='P' or item=='Q' or item=='R' or item=='S' or item=='T' or item=='U' or item=='V' or item=='W' or item=='X' or item=='Y' or item=='Z':
        U=U+1
        
    else:
        L=L+1
        
print("There are "+str(U)+" Upper case letters in this Sentence")
print("There are "+str(L)+" Lower case letters in this Sentence")
