import sys
list1=[]
sol=0
cycle=1
N=sys.stdin.readline().strip()
#0<=N and N<=99
def num(N, list1):
    if int(N)<10 and int(N)>=0:
        list1.insert(0,'0')
        list1.insert(1,N)
    else:
        list1=list(N)
    return list1

def mylist(A,B):#make new number
    A=int(A)
    B=int(B)
    sum=A+B
    mlist=[]
    mlist.insert(0,str(B))
    templist=[]
    templist=list(num(str(sum),templist))
    mlist.insert(1,templist[1])
    return mlist

list1 = list(num(N, list1))
# print(list1)
list2 = list(list1)
# print(list2)
# print(type(N))
list2 = list(mylist(list2[0], list2[1]))
# print(list2)
while int(N) != int(sol):
    list2 = list(mylist(list2[0], list2[1]))
    cycle += 1
    sol = list2[0]+list2[1]
    # print("a",list2)

print(cycle)

