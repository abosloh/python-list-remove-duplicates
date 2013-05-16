

list  = ["a","a","a","b","b","b"]

list1 = []

for l in list:
    if l not in list1:
        list1.append(l)

print list1


# result : ['a', 'b']
