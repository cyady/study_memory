#Example1
#
# def func(i, j):
#     print(i,j)
#
# #func(10, 20) # positional arguments
# #func(j=20, i=10)    #10,20 keyword arguments not considering the position

#Example2 : defualt values assigned th positional arguments
#
# def func(i,j=10):
#     print(i,j)
#
# func(100,200)   #100,200
# func(100)       #100,10

# Example3: keyword arguments
# def greetings(name, greeting):
#     print(greeting + "    " + name)
#
# greetings(name='john', greeting="Hello") #Hello Jhon
# greetings(greeting="Hello", name='john')    #keyword parameter의 유연성
#

#Example4:
# def my_func(a,b,c):
#     print(a,b,c)
#
# my_func(10,20,30) #positional arguments
# my_func(a=10, b=20,c=30)    #Keyword arguments
# my_func(b=20, a=10,c=30)    #keyword arguments
#
# my_func(10,20,c=30)     #10 20 30
# my_func(10,b=20,c=30)   #10 20 30
# #my_func(10, b=20, 30)   #error/ This is wrong as positional argument must appear before any keyword argument
#
# my_func(10,30,b=20)     #TypeError: my_func() got multiple values for argument 'b'
# #logical error about parameters

#Example5: Function can return multiple values

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

# print(largest(100,200)) #(200, 100)
# print(largest(20,10))   #(20, 10)

res=largest(10,20)
print(res)
print(type(res))    # tuple   [list] {set} (tuple)
#tuple can return multiple values

