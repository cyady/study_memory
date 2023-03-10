#Example4:
#
# x=100
#
# def cool():
#     global x
#     x=500
#     print(x)
#
# #cool() #500
# print(x)
#

#   Example5
#There is no need to declare global variables outside the function.
#You can declare them global inside the function    -global

def cool():
    global x    #함수 내부에서도 전역변수를 만들 수 있지만 global을 참고해야함
    x=100
    print(x)

cool()
print(x)    #able to access x bcoz it is global variable






