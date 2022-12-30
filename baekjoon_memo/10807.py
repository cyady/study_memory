#N=int(input())
# try:
#     mylist=list(input().strip().replace(" ", ""))
#
#     # print("a", mylist)
#     # print(mylist)
#     W=input()
#     mylist=list(mylist[0:N])
#     # print(mylist)
#     ans=mylist.count(W)
#     print(ans)
# except:
#     EOFError

N=int(input())
mylist=list(map(int, input().split()))
mylist1=[]
# print(mylist)


mylist1=list(mylist[0:N])
# print(mylist1)


W=int(input())

cot=mylist1.count(W)
print(cot)

# N=int(input())
# try:
#     mylist=list(input().replace(" ", ""))
#
#     # print("a", mylist)
#     # print(mylist)
#     W=input()
#     print(mylist)
#     print("W", W)
#     mylist=list(mylist[0:N])
#     # print(mylist)
#     ans=mylist.count(W)
#     print(mylist)
#     print(ans)
# except:
#     EOFError


