
# List 

subject=["Mishuk","Maruf","Mefa","Marina"]

print(subject)
print(subject[1])
print("Mefa" in subject)
print(subject[-1])
print("Sheikh" not in subject)


#List function 

list=["Math","English","Bangla"]

print(len(list))
list.append("Mishuk")
print(list)
list.insert(4, "os")
print(list)
list.remove("os")
print(list)

list.sort()
print(list)

list.reverse()
print(list)

'''list.clear()
print(list)'''

list2=list.copy()
print(list2)

pos=list.index("Mishuk")
print(pos)
