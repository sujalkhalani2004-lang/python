# 1. Count total number of words in a string
# s = input("Enter string:")
# word = s.split()
# print("Total word",len(word))

# 2. Reverse a string using range
# s = input("Enter string")
# rev = ""
# for i in range(len(s)-1):
#     rev=rev +s[i]
#     print("rebserse string",rev)


# 62.	Create a dictionary of employees where empId will be the key and value will be the name of an employee
# 1.	Display how many employees are there in the dictionary.
# 2.	Display all empID and add them in a separate list.
# 3.	Display all employee names and take them to a separate list
# 4.	Take an empId from the user and check if that employee is there in the dictionary or not.
# 5.	If an empID is there in the dictionary then display the name of that employee or if not available then add an ID and Name of the employee in the dictionary
# # 6.	Change the name of the employee of empID taken by the user
# 7.	Remove an employee whose ID is provided by the user

# emp = {
#     101 :  "amit",
#     102 : "sujal",
#     103 : "mandip"
# }
# # 1
# print("This dict in the employee is ",len(emp))

# # 2
# list = []
# for i in emp:
#     # print(i)
#     list.append(i)
# print("empid list:",list)

# # 3
# list = []
# for i in emp:
#     # print(emp[i])
#     list.append(emp[i])
# print("name in list",list)

# # 4
# eid = int(input("enter empid to chack:"))
# if eid in emp:
#     print("emoloye exite")
#     print("name:",emp[eid])
# else:
#     print("not exited")

# #5
# name = input("enter name")
# emp[eid]= name
# print("employe add")

# #6
# eid = int(input("Enter empid to change name"))

# if eid in emp:
#     new_name = input("enter new name")
#     emp[eid] =new_name
#     print("name add")
# else:
#     print("not found")

# #7
# eid = int(input("Enter empid to remove name"))

# if eid in emp:
#     emp.pop(eid) 
#     print("name reomve")
# else:
#     print("not found")

# #
# print("final dict",emp)

# prime numbbr
# n = int(input("Enter a number"))
# count = 0
# for i in range(2,n+1):
#     if n % i ==0:
#         count = count+1
# if count ==1:
#     print("prime number")
# else:
#     print("not prime")


#amstron
n = int(input("Enter a number: "))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit * digit * digit)
    temp //=10

if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

num = 121

if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

s="madam"

if s==s[::-1]:
    print("palindrom")
else:
    print("not")

n = int(input("enter number"))
temp = n
sum  = 0 
while temp > 0:
    digit = temp %10
    sum = sum + digit*digit*digit
    temp //10
if sum ==n:
    print("arm")
else:
    print("onot")