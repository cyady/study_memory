mylist=[]
for i in range(9):
    mylist.append(int(input()))

MAX = max(mylist)
index = mylist.index(MAX)

print(MAX)
print(index+1)