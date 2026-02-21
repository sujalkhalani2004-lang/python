# # input name and chack len
# name = input("Enter name:")
# print("name length is a:",len(name))
# # count a word in sentence
# name1 = "this is very good person this is very coolthat is "
# print(name1.count("very"))
# # student mark give gread
# mark = int(input("Enter marks:"))
# if(mark >=90):
#     print("Grad A")
# elif(mark >=80 and mark <90):
#     print("Grad B")
# elif(mark >=70 and mark <80):
#     print("Grad c")
# else:
#     print("fail")
# # trafic light
# Light = input("Enter light:")
# if(Light == "Green"):
#     print("GO go go")
# elif(Light == "Yellow"):
#     print("warnig")
# elif(Light == "Red"):
#     print("stop")
# else:
#     print("wrong light enter ")
# # user input odd ya even
# Number = int(input("Enter number:"))
# if(Number%2==0):
#     print("EVEN")
# else:
#     print("ODD")
# # user enter 3 number gretest number print
# a=int(input("Enter number A:"))
# b=int(input("Enter number B:"))
# c=int(input("Enter number C:"))

# if(a>=b and a>=c):
#     print("first is large")
# elif(b>=c):
#     print("second is large")
# else:
#     print("third is large")

# # multi 7 
# x = int(input("Enter number:"))
# if(x%7==0):
#     print("this multila of 7")
# else:
#     print("not")
    
# n = int(input("enter number"))
# count = 0
# for i in range(2,n+1):
#     if n % i ==0:
#         count = count+1
#     if count == 1:
#         print("prime")
#     else:
#         print("not prime")

n = int(input("enter number"))
temp = n
sum =0

while temp > 0:
    digit = temp %10
    sum = sum+(digit*digit*digit)
    temp //=10

if sum == n:
    print("armstrong")
else:
    print("not")
