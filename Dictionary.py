# dictionary 
# ----------------------------------------------------------------
# studnet = {
#     "name" : "sujal",
#     "age" : 21,
#     "cgpa" : 7.0
# }
# print(studnet)
# print(type(studnet))

# they are unrodered,mutable(changeble )& dont allow duplicte key   
# -----------------------------------------------------------------
# you store in a string,list,tuple,float,boolean +
# studnet = {
#     "name" : "sujal",
#     "subjct" : ["math","guj","eng"],
#     "topic" : ("dict","set"),
#     "age" : 34,
#     "its_adult" : True  
# }

# studnet["name"] = "sk",
# studnet["surname"] = "khalani"
# print(studnet)
# -------------------------------------------------------------------

# nested    dictiory
# student = {
#     "name" : "sujal",
#     "rollno" : 19,
#     "score" : {
#         "math" : 45,
#         "eng" : 40,
#         "guj" :67
#     }
# }
# print(student["name"    ])
# print(student["score"]["math"])
# -------------------------------------------------------------------
# dict method 
# 1.mydict.keys()  return all keys
# print(student.keys())

# 2.mydict.values() return all values
# print(student.values())

# 3.mydict.items() return all (key,val) pairs all tupls
# print(list(student.items()))

# 4.mydisct.get() return the key according to value
# print(student["name2"])
# print(student.get("name2")) 

# 5.mydict.update() insert a new value in dict
# print(student.update({"city":"surat"}))
# print(student)
# ------------------------------------------------------------------------

# practice
# 1.strore following word meanig in a python dictionary
# table:"a peace of furniture","listv of fact & fighrs"
# cat :"a small animal"

# dictiroy = {
#     "cat" : "A small animal",
#     "table" : ["a peace of furniture","list of fact & fighrs"]
# }
# print(dictiroy)
# -----------------------------------------------------------------------------------------
# 2 enter marks user and store data in dictiory
mark = {}

x = int(input("Enter phy "))
mark.update({"phy" : x})

x = int(input("Enter subject "))
mark.update({"chm":x})

x = int(input("Enter subject "))
mark.update({"math":x})

print(mark)
