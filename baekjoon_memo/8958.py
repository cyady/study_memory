N=int(input()) # number of line
mylist=[]
for i in range(N):
    mylist.append(input().split())
print(mylist)

count=0
for i in range(len(mylist)):
    mylist2=mylist[i]
    print(mylist2)
    #쪼개서 임시저장
