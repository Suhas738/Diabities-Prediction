S=str(input("Enter any sentence"))
v=0
c=0
for item in S:
    if item=='a' or item=='e' or item=='i' or item=='o' or item=='u' or item=='A' or item=='E' or item=='I' or item=='O' or item=='U':
        v=v+1
        
    else:
        c=c+1
        
print("There are "+str(v)+" Vovels in this Sentence")
print("There are "+str(c)+" Consonents in this Sentence")
