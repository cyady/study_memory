cash_sum = int(input())
item = int(input())
sum =0
for i in range(0,item):
    cash, n = map(int, input().split())
    sum=sum+cash*n
if cash_sum==sum:
    print("Yes")
else:
    print("No")