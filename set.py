# set is the collection of the unordered item
# each elementin the set must be unique & inmmutable
# ---------------------------------------------------------------------------------------
# collection = {1,2,3,1,3,4,"sujal","sujal"} #set in the duplicate value are not store
# print(collection)
# print(type(collection))
# print(len(collection)) #can you print set len but dulicate value len not store
# collection = set() #empty set syntx
# print(type(collection))

# -----------------------------------------------------------------------------------------
# collection ={1,2,3,3,4,5}
# collection2={3,4,5,7,8,9}

# collection.add(1) add a value
# collection.add(2)
# collection.clear() clear a all element 
# print(collection.pop()) #remove a rendome value
# print(collection.remove("hello"))
# print(collection.union(collection2))  combilne both set value & return new
# print(collection2.intersection(collection2))  combilne common values & return values

# --------------------------------------------------------------------------------------------
# practice
# 1.you are given a list of subject for student assume one classroom is reuquried for 1 subject .
# how many classroom are needed by all student

subject = {"python","java","c++","python","js","java","python","java","c++","c"}
print(subject)
print(len(subject))