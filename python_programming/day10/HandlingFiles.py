# #Example1 : Writing data in to text file
# file=open(r"C:\Users\cyady\Desktop\project\Python\study_python\python_programming\day10\myfile.txt", 'w')
#  #write mode
# file.write("This is my first statement...\r\n")
# file.write("This is my second statement...\r")
# file.write("This is my third statement...\r")
# file.write("This is my forth statement..\n\r")
# file.write("This is my fifth statement...\n")
# file.close()
# print("program completed...")

# #Example2 : reading data from text file
#
# file=open(r"C:\Users\cyady\Desktop\project\Python\study_python\python_programming\day10\myfile.txt", 'r')
# # read mode
# # print(file.read())
# # print(file.readline())  #read first line
# file.close()

#Example3 : appending data into text file
file=open(r"C:\Users\cyady\Desktop\project\Python\study_python\python_programming\day10\myfile.txt", 'a')
#append mode
file.write("This is my sixth line\n")
file.write("This is my seventh line\n")
file.close()


