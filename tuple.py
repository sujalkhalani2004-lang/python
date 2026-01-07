# tuple is inmutable just like string you can creat a tuple than not chnag a value
# tup = (1,2,3,4)
# print(type(tup))

# tuple 2 method

# tup = (1,2,3,4,2,2)
# print(tup.index(4))
# print(tup.count(2))

# practices
# 1. wap ask the user the 3 fav movie and print in list 
# movies=[]
# mov1 = input("Enter first fav movie:")
# mov2 = input("Enter second fav movie:")
# mov3 = input("Enter third fav movie:")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# 2. wap list contains a plaindrome of elements
# list = [1,2,1,3,4]
# copy_list = list.copy()
# copy_list.reverse()
# if(copy_list == list):
#     print("palindrome")
# else:
#     print("not palindrome")

# 3.wap count number of student with the 'a' greade in the following tuple
# tup = ("c","d","a","a","b","b","a")
# print(tup.count("a"))

list=["c","d","a","a","b","b","a"]
list.sort()
print(list)