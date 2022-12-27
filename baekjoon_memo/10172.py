array = [[" " for col in range(12)] for row in range(5)]
# print(array)
array[0]=list("|\_/| ")
array[1]=list("|q p|   /}")
array[2]=list("( 0 )\"\"\"\ ")
array[3]=list("|\"^\"`    | ")
array[4]=list("||_/=\\\\__| ")
# print(array[0])
# print(array[1])

for i in array:
    for j in i:
        print(j,end="")
    print()

# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|
