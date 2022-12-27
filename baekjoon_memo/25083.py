array = [[" " for col in range(15)] for row in range(6)]
# print(array)
array[0]=list("         ,r'\"7")
array[1]=list("r`-_   ,'  ,/")
array[2]=list(" \. \". L_r'")
array[3]=list("   `~\/")
array[4]=list("      |")
array[5]=list("      |")
# print(array[0])
# print(array[1])

for i in array:
    for j in i:
        print(j,end="")
    print()

#          ,r'"7
# r`-_   ,'  ,/
#  \. ". L_r'
#    `~\/
#       |
#       |
