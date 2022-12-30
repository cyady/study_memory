N, X=map(int, input().split())
mylist1=list(map(int, input().split()))
# print(mylist1)
mylist3=[]
for i in range(N):
    if mylist1[i]<X:
        mylist3.append(mylist1[i])

print(*mylist3)

