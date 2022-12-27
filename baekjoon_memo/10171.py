#
# 예제 출력 1

# \    /\
#  )  ( ')
# (  /  )
#  \(__)|
array = [[0 for col in range(8)] for row in range(4)]
# print(array)
array[0]=list("\    /\ ")
array[1]=list(" )  ( ')")
array[2]=list("(  /  ) ")
array[3]=list(" \(__)| ")
# print(array[0])
# print(array[1])

for i in array:
    for j in i:
        print(j,end="")
    print()
