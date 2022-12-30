board = []
for i in range(42):
    board.append(i)
# print(board) #remainder list

# slist=[]
for i in range(10):
    A=int(input())
    # slist.append(A)
    if A%42 in board: board.remove(A%42)

# print(slist) #input list

ans = len(board)
print(42-ans)