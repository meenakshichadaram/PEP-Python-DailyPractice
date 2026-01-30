#-------Practise session-------
"""# Q1) create a list of numbers and print each element 
list1 = [1,2,3,4,5]
for i in list1: #looping through each element of list
    print(i)

#Q2) how to add a new element to a list
list1.append(6)
print(list1)
# with an empty list
fruit = []
fruit.append("apple")
fruit.append("banana")
fruit.append("grapes")
print(fruit)

#Q3) find the sum of all elements in a list 
total = 0
for i in list1:
    total += i
print("Sum is:",total)

#Q4) reverse a list 
rev_list = list1[::-1]
print("Reversed list is:",rev_list)

#Q5) find duplicate elements in a list
list2 = [1,2,3,4,5,6,5,4,3,2,1]
dup_list = []
for i in list2:
    if i not in dup_list:
        dup_list.append(i)
print(dup_list)

#Q6) create a tuple and access its 1st and 2nd elements
colors = ("red","blue","pink","yellow")
print(colors[1])
print(colors[2])

#Q7) Conversion of list into a tuple
num = [1,2,3,4,5]
print(type(num))
num_tuple = tuple(num)
print(num_tuple)
print(type(num_tuple))

#Q8) conversion of tuple to list 
colors = ("red","blue","pink","yellow")
colors_list = list(colors)
print(colors_list)
print(type(colors_list))

#Q9)conversion of list into a set 
num = [1,2,3,4]
num_set = set(num)               
print(num_set) 
num_list = list(num_set)
print(num_list)

#Q10) conversion of dictionary into a set
student = {'name':'John', 'age':25, 'city':'New York'}
student_set = set(student)
print(type(student_set))
print(student_set)  #prints only keys of dictionary

#Q11) conversion of set into a dictionary
sub = {'maths','science','english'}
sub_dict = dict.fromkeys(sub,0) #assigning default value 0 to each key, .fromkeys() is used to create a dictionary from a set
print(sub_dict)
print(type(sub_dict))
---end of practise session---

#Exception handling 
#1) ZeroDivisionError = when you divide any number with zero --> print(2/0)
#2) ValueError = when you give wrong value to a function --> num=int("hello")
#3) TypeError = when you perform operation between different datatypes -->print(5+"abc")
#4) IndexError = when you access a wrong index --> a = [10,20,30] , print(a[5])
#5) KeyError = when ypu access a missing key in a dictionary --> students={"name":"Rahul","age":20} , print(student{"marks"})
#6) FileNotFoundError = when python not able to find file in your pc 

#1) ZeroDivisionError = dividing by zero
#2) ValueError = wrong value
#3) TypeError = wrong datatype
#4) IndexError = wrong index
#5) KeyError = misisng key
#6) FileNotFoundError = file not found
'''
try:
    risky code
except:
    runs if error occurs

try = code that may fail
except = runs when error happen'''

#catching any specific error
try:
    x = int(input("enter number: "))
    print(10/x)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Enter only number")

#else block 
try:
    x = int(input("enter number: "))
    print(10/x)
except:
    print("An error occurred")
else:
    print("No error, program run successfully")

#finally block
try:
    x = open("movies.txt")
except:
    print("File not found")
finally:
    print("program finished")

age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("Age must be 18 or above to vote")
print("You can vote")

#custom errors
class LowBalanceError(Exception):
    #this line creates a custom exception named LowBalanceError
    pass
balance = 500
withdraw = int(input("enter amount: "))
if withdraw > balance :
    raise LowBalanceError("Insufficient balance")
print("Withdraw successful")

try:
    num = int(input("Enter a number: "))
    print(100/num)
except:
    print("error")

try:
    try:
        print(1/0)
    finally:
        print("inner finally")
except ZeroDivisionError:
    print("outer exception")
finally:
    print("outer finally")

def test():
    try:
        return 10
    except:
        return 15
    finally:
        return 20
print(test())  #prints 20 because finally block overrides the return value of try block

try:
    try:
        x=int("abc")
    except ValueError:
        print("inner handled")
    raise
except Exception:
    print("outer handled")

def test():
    try:
        return 10
    except:
        return 20
    finally:
        return 30 
print(test())

age = int(input("enter your age: "))
if age <18:
    raise ValueError("Age must be 18 or above")
print("You are eligible to vote")

age = int(input("enter ur age: "))
if age<18:
    raise ValueError("Age must be 18 or more")
print("you are eligible")

#take number input from user
num = int(input("enter num: "))
#if number is negative, we manuaaly raise an eroor
#python does not automatically treat negative numbersa as wrong
if num<0:
    raise ValueError("Number must be positive")
#this will run only if no exception occurs
print("you entered: ",num)

print(True+True+True)
print("5"+"4")
print("5"*10)

def change(x):
    x+=10
s=5
change(s)
print(s)

def update(lst):
    lst.append(10)
nums = [1,2,3]
update(nums)
print(nums)

t = (1,2,3)
t = t+(4,)
print(t)

s = {1,2,2,3,3}
print(len(s)) #it removes all the duplicates and returns 3 

i = 1
while i < 10:
    i *= 3
    print(i)

for i in range(3):
    print(i)
else:
    print("done")

try:
    print("A")
    10/0
    print("B")
except:
    print("C")
print("D")

try:
    print(1)
except:
    print(2)
finally:
    print(3)

def test():
    try:
        return 10
    finally:
        return 20
print(test())

# Q1) move all the zeros to end 
num = [0,1,0,3,12]
result = [] #we will store non zero elements
zero_count = 0
for a in num:
    if a==0:
        zero_count+=1
    else:
        result.append(a)
for i in range(zero_count):
    result.append(0)
print(result)

#palindrom in two pointer approach
text = "meena"
left = 0
right = len(text) - 1
isPalindrome = True
while left<right:
    if text[left]!= text[right]:
        isPalindrome = False
        break
    left+=1
    right -=1
print(isPalindrome)

#longest word in a sentence
sentence = "Python makes problem solving fun"
words = sentence.split()
longest=""
for i in words:
    if len(i)>len(longest):
        longest=i
print(longest)
"""
#two sum problem dsa
num = [1,2,3,2]
target = 5
count = 0
for i in range(len(num)):
    total = 0
    for i in range(i,len(num)):
        total+=num[i]
        if total==target:
            count+=1
print(count)

#q5 brute force approach it has nested for loops time complexity is more or worst
num = [2,7,11,15]
target = 9
for i in range(len(num)):
    for j in range(i+1,len(num)):
        #check if sum matches the target
        if num[i]+num[j]==target:
            print(num[i],num[j])

# we r using two pointer approach to reduce loops and time complexity
nums = [2,7,11,15]
target = 9
left = 0
right = len(nums)-1
while left<right:
    current_sum = nums[left]+nums[right]
    if current_sum == target:
        print(nums[left],nums[right])
        break
    elif current_sum<target:
        left+=1 
    else:
        right-=1

#fast and slow pointer approach
#fast moves 2 time and slow moves 1  time always remember if the fast pointer is the end slow pointer is at the between 

#tortoise and hare technique
nums = [10,20,30,40,50]
slow = 0;
fast = 0;
while fast<len(nums) and fast+1<len(nums):
    slow+=1
    fast+=2
print(nums[slow])
