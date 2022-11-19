l=["Venom","Carnage","Riot","Menace"]
print(l)
l[3]="Scream"
for x in l:
    print(x)
if "Menace" in l:
    print("Menace is in the Venomverse")
else:
    print("Menace is in the Venomverse")
l.remove("Scream")
for x in l:
    print(x)
print(len(l))
l.insert(2,"Menace")
for x in l:
    print(x)
print("Hello menace")
l.pop()
for x in l:
    print(x)
del l
print("Hello Friends")

