l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pos=0
even=0
odd=0
for a in l:
    if l[pos]%2==0:
        even=even+l[pos]
    else:
        odd=odd+l[pos]
    pos=pos+1
print(even)
print(odd)
