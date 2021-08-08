my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
k=[]
b=[]
for x in my_dict.values():
    k.append(x)    
for i in range(3):
    m=max(k)
# print(m)
    k.remove(m)
    b.append(m)
print(b)

    
        
