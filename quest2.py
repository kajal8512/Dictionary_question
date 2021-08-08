# dict={"name":"Rishabh","marks":45}
# x=input("enter the key")
# if x in dict:
#     print("exist")
# else:
#     print("not exist")

a=["Name","work","age"]
b=["Neha","studend","20"]
i=0
k={}
while i<len(a):
    k[a[i]]=b[i]
    i+=1
print(k)
