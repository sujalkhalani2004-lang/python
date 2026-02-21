# string function 

# # endwith
# str1 = "hello my name is sujal hello"
# print(str1.endswith("hello"))

# # # capitalize
# print(str1.capitalize())
# print(str1)

# # # replace 
# print(str1.replace("a","A"))

# # #find 
# print(str1.find("a"))

# # # count
# print(str1.count("hello"))

# exersice

# input name and chack len
Name = input("Enter your name:")
print("Your name len is :",len(Name))

# count a word in sentence

Name = "this is my name is sujal and i willl work in microsoft compny than 5 lakh per month sallry"
print(Name.count("i"))

# student mark give gread
marks =int( input("Enter marks:") )

if(marks >=90):
    gread = "A"
elif(marks >= 80 and marks < 90):
    gread = "B"
elif(marks >= 70 and marks < 80):
    gread = "C"
else:
    gread = "D"

print("The gread is a",gread)

# trafic light
light = input("Enter light:")
if(light == "Green"):
    print("Go Go")
elif(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Wornig")
else:
    print("wrong light re-enter light")

# user input odd ya even
# n= int(input("enter number:"))

# if(n%2==0):
#     print("Even number")
# else:
#     print("odd number")

# user enter 3 number gretest number print
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))

# if(a>=b and a>=c):
#     print("First is largest")
# elif(b>=c):
#     print("Second is largest")
# else:
#     print("third is largest ")

# multi 7 
# x = int(input("Enter number"))
# if(x%7==0):
#     print("multipal of 7")
# else:
#     print("not a multipal")
