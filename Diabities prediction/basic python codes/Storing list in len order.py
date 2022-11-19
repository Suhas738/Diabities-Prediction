l=["a","an","eat","b","in","on","but","cat"]
l1=[]
l2=[]
l3=[]
for item in l:
    if len(item)==1:
        l1.append(item)
    elif len(item)==2:
        l2.append(item)
    elif len(item)==3:
        l3.append(item)
    else:
        pass
print(l1)
print(l2)
print(l3)
