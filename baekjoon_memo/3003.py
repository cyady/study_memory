mylist1=[1,1,2,2,2,8]
a,b,c,d,e,f=map(int, input().split())
mylist2=[]
mylist3=[]
mylist2.insert(0,f)
mylist2.insert(0,e)
mylist2.insert(0,d)
mylist2.insert(0,c)
mylist2.insert(0,b)
mylist2.insert(0,a)
#print(mylist2)
for i in range(6):
    mylist3.insert(i, mylist1[i]-mylist2[i])
#print(mylist3)
print(mylist3[0], mylist3[1], mylist3[2], mylist3[3], mylist3[4], mylist3[5])