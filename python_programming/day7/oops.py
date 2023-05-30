#Example1:
#
# class MyClass:
#     def myfunction(self):   #defalt argument is self
#         # this particular method is belongs th this particular class that's the meaning of self
#         # self는 클래스를 의미하므로 지우지 않는다.
#         pass #simply san pass pass is nothing but none
#     def display(self, name):
#         print(name)
#
# #mc1,mc2 is object
# mc1=MyClass()
# mc2=MyClass()
#
# mc1.myfunction()
# mc1.display("scott")

#Example2:
# class MyClass:
#     def m1(self):
#         print("this is instance method...")
#
#     def m2(self, num):
#         print(num + " also instance method..")
#                         #in instance method, self is not parameter
#     @staticmethod   #annotation
#     def m3(self, num):  #정적메소드에서 slef또한 하나의 인수를 기대하게 된다.
#         print(self, num)
#         #print(num)
# mc=MyClass()
# mc.m1()
# #mc.m3(100)  #argument not enough
# mc.m3(100, 200) #100,200
#
# MyClass.m3(10,20)   #10, 20 #here calling static method directly using class not through object
# MyClass.m2(300) #Type error, same result also 2 parameter in there

#Example3:  calss variables
# class Myclass:
#     a,b=10,20   #class variables bcoz created inside of class
#     def add(self):
#         print(self.a +self.b)
#         # print(a,b)  #can not access a,b boz they are not Global variables
#
#     def mul(self):
#         print(self.a * self.b)
#
# mc=Myclass()
# mc.add()    #30
# mc.mul()    #200

#Examople4:
# i,j=15,25   #Global variables
#
# class MyClass:
#     a, b=10,20  #class variables
#     def add(self,x,y):
#         print(x+y)  #x, y are Local variables
#         print(self.a+self.b)    #a, b are class variables
#         print(i+j)  #i, j are Global variables
#
# mc = MyClass()
# mc.add(100,200)

#Example 5:
# a,b=15,25   #Global variables
#
# class MyClass:
#     a, b=10,20  #class variables
#     def add(self,a,b):
#         print(a+b)  #local
#         print(self.a+self.b)    #class
#         print(globals()['a']+globals()['b'])    #how to access global variables
#
# mc = MyClass()
# mc.add(100,200)

#Example6: one class can have multiple objects
# class MyClass:
#     def display(self,name):
#         print("this is display method...")
#         print((name))
#
# obj1=MyClass()
# obj1.display("jhon")
#
# obj2=MyClass()
# obj2.display("scott")

# #Example7: constructor example
# class MyClass:
#     def __init__(self):
#         print("this is consturctor..")
#     def m1(self):
#         print("hello")
#     def m2(self, x,y):
#         return(x,y)
#
# mc=MyClass()    #invoke constructor automatically this is consturctor..
# mc.m1() #method we have call explicitely by using object
# res=mc.m2(10,20)
# print(res)  #30

# #Example8
#
# class MyClass:
#     name="john"
#     def __init__(self, name):   # constructor expecting one argument
#         print(name)
#         print(self.name)
#
# mc=MyClass("David") #passing parameter to the constructor

# #Example9
#
# #Req: Emplyee_EMP
#     # constructor : eid, ename, sal
#     # display() : print eid, ename & sal
#
# class Emp:
#     eid=""
#     ename=""
#     sal=""
#     def __init__(self, eid, ename, sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#
#     def display(self):
#         print(self.eid,self.ename,self.sal)
#
# e1=Emp(101, "John", 500000) #101 John 500000
# e1.display()
#
# e2=Emp(102, "scott", 700000) #101 John 500000
# e2.display()

#Example10

#Req: Emplyee_EMP
    # constructor : eid, ename, sal
    # conctructor : print eid, ename & sal
class Emp:

    def __init__(self, eid, ename, sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal

    def __str__(self):
        return(self.ename,self.sal)    #TypeError: __str__ returned non-string (type tuple)
        #invalid becoz __str__() returns only string data
e1=Emp(101, "John", 500000) #101 John 500000
print(e1)









