"""#Object oriented programming
# Class : class is a blueprint of an object 
# object : Instance of class , (anything we make out of class is called object )
#self : the object is pointing to the self
#basic syntax
class Student :
    print("Hey this is the first class!!")
s1 = Student()
print(s1)
# Constructor : it is a function automatically gets called when a object is made 
# two types are default and parametirised
# attributes : data and variables stored in class or object
#two types of attributes : class attribute and object attribute 
#methods : functions which are related to objects 
#static method: they r for class
#normal method :they r for object
class Student:
    def __init__(self):
        print("This is our constructor")

s1 = Student()
print(s1)

class Student:
    def __init__(self):
        self.name = 'Rahul'
s1 = Student()
print(s1.name)

class Student:
    def __init__(self, Fullname):
        self.name = Fullname
s1 = Student("Meena")
print(s1.name)

class Student:
    def __init__(self,Fullname,Marks):
        self.name = Fullname
        self.scored = Marks
s1 = Student("Meena",85)
s2 = Student("Manju",77)
print(s1.name , s1.scored)
print(s2.name , s2.scored)

class Car:
    def __init__(self,Modelnum , colour):
        self.color = colour
        self.modelnum = Modelnum
c1 = Car("R676","Black")
c2 = Car("K234","Cherry red")
print(c1.modelnum,c1.color)
print(c2.modelnum,c2.color)

#class Student:
#    college = "ABC College"   # class attribute
#    def __init__(self, name):
#        self.name = name      # object attribute

class Student:
    college = "LPU"
    def __init__(self,Fullname,Marks):
        self.name = Fullname
        self.scored = Marks
s1 = Student("Meena",85)
s2 = Student("Manju",77)
print(s1.name , s1.scored , s1.college)
print(s2.name , s2.scored , s2.college)
print(Student.college)

class Company:
    company_name = "TCS"
    def __init__(self,Employee_name , Employee_id , Salary):
        self.employee_name = Employee_name
        self.employye_id = Employee_id
        self.salary = Salary
comp1 = Company("Meenakshi",17865,50000)
comp2 = Company("Manju",54243,50000)
print(comp1.employee_name , comp1.employye_id, comp1.salary , comp1.company_name)
print(comp2.employee_name , comp2.employye_id, comp2.salary , comp2.company_name)

class Car:
    showroom_name = "Renault"
    def __init__(self,Model_name , Car_price):
        self.model_name = Model_name
        self.car_price = Car_price
c1 = Car("Kwid",800000)
c2 = Car("Jumper",500000)
print(c1.showroom_name , c1.model_name , c1.car_price)
print(c2.showroom_name , c2.model_name , c2.car_price)

class Student:
    n_college_name = "Sandip university"
    s_college_name = "SRM univeristy"
    h_college_name = "Ramachnadra college of engineering"
    def __init__(self,Name , Marks):
        self.name = Name
        self.marks = Marks
s1 = Student("Naeem",89)
s2 = Student("Shivani",88)
s3 = Student("Harika",87)
print(s1.name , s1.marks , s1.college_name)
print(s2.name , s2.marks , s2.college_name)
print(s3.name , s3.marks , s3.college_name)
Student.n_college_name = "LPU"
Student.s_college_name = "LPU"
Student.h_college_name = "LPU"
print(Student.college_name)

class Company:
    company_name = "TCS"
    def __init__(self,Employee_name , Employee_id , Salary):
        self.employee_name = Employee_name
        self.employye_id = Employee_id
        self.salary = Salary
comp1 = Company("Meenakshi",17865,50000)
comp2 = Company("Manju",54243,50000)
print(comp1.employee_name , comp1.employye_id, comp1.salary , comp1.company_name)
print(comp2.employee_name , comp2.employye_id, comp2.salary , comp2.company_name)
comp1.salary = 60000
comp2.salary = 60000
print(comp1.salary)
print(comp2.salary)

# create a class Student where total stud is a class attribute and we have to increase this count whenever the object is created
class Student:
    total_student = 89
    def __init__(self,Student_name ,Student_branch):
        self.name = Student_name
        self.brach = Student_branch
        Student.total_student += 1
s1 = Student("Meena","CSE(DS)")
s2 = Student("Manju","CSE(DS)")
print(s1.name,s1,branch)
print(s2.name,s2.branch)
print("Total students:",Student.total_student)

#------Method-------
#methods are the functions which are related to the objects 
#static method are for class 
class Student:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print("Hello",self.name)
s1=Student("Meenakshi")
s1.hello()

class Student:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print("Hello",self.name)
    @staticmethod
    def college_name():
        print("This is LPU")        # class static method
Student.college_name()

#create a class student such that the object attribute name and marks and there is normal method we have to make which will display --> name , marks
class Student:
    def __init__(self,Name , Marks):
        self.name = Name
        self.marks = Marks
    def Display(self):
        print("Hi",self.name,"you scored",self.marks)
s1 = Student("Meenaskhi",88)
s2 = Student("Manju",89)
s1.Display()
s2.Display()

#mutable data structures
# 1) list 
# 2) set 
# 3) dictionaries
#immutable data structures
# 1) int
# 2) float
# 3) string
# 4) tuple
# 5) boolean(subpart of int )

# Q1) create a class student and show name in the normal method and college name in the static method 
class Student:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print(self.name)
    @staticmethod
    def college_name():
        print("College name: LPU")        
s1 = Student("Meenakshi")
s2 = Student("Manju")
s1.hello()     
Student.college_name()

#------Four pillars of OOPS-------
# 1) Encapsulation = data hiding + control acess 
# 2) Abstraction = hiding the process
# 3) Inheritance
# 4) Polymorphism

# Encapsulation
# in excapsulation we hide data (variables) and methods (functions) together into a single unit (class) and restricting direct access to data to protect it.
# we have to use double underscore in front of variables to hide it --> self.__marks = marks , __ means cannot be accessed directly outside the class
class Student:
    def __init__(self , marks):
        self.__marks = marks # private variable
s1 = Student("89") # this doent work coz we r trying to change the data of marks where the variable marks was declared and hide them using underscores 
print(s1.marks)

# get_marks() → door to access data (method) , get_marks --> to read the value
class Student:
    def __init__(self , marks):
        self.__marks = marks
    def get_marks(self): 
        return self.__marks
s1 = Student(89)  #()--> int
print(s1.get_marks())
# Q) we have to create a class bank where balance is hidden adnd we have to access the bank
class Bank:
    def __init__(self, balance):
        self.__balance = balance   # hidden (private)
    def get_balance(self):
        return self.__balance      # access balance
b1 = Bank(5000)
print(b1.get_balance())
"""
#set_marks --> to change the values 
class Student:
    def __init__(self , marks):
        self.__marks = marks
    def get_marks(self): 
        return self.__marks
    def set_marks(self,new_marks):
        self.__marks = new_marks
s1 = Student(89)  
s1.set_marks(95)
print(s1.get_marks())

class Bank:
    def __init__(self, balance):
        self.__balance = balance   

    def get_balance(self):
        return self.__balance 

    def deposit(self, deposited_money):
        if deposited_money > 0:
            self.__balance += deposited_money
        else:
            print("Invalid amount")

b1 = Bank(5000)
b1.deposit(1000)
print(b1.get_balance())
