import sys
sys.path.append(r"C:\Users\cyady\Desktop\project\Python\study_python\python_programming\Day9\packA")
sys.path.append(r"C:\Users\cyady\Desktop\project\Python\study_python\python_programming\Day9\packB")

# # Approach1
# import emp
#
# empobj=emp.Employee(101, "JOHN", 5000000)
# empobj.displayemp()
#
# import stu
# stuobj=stu.Student(1122, "Scott", 'B')
# stuobj.displaystu()

#Approach2

from emp import Employee
empobj=Employee(101, "John", 50000)
empobj.displayemp()

from stu import Student
stuobj=Student(1122, "David", 'B')
stuobj.displaystu()

