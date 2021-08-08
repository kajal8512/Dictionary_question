# user=int(input("enter the num"))
# b=user**2
# if user**2==b:
#     print(b)
# else:
#     pass

# def name():
#     user=int(input("enter the no."))
#     print(user**2)
# name()


dict =  {
    'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
c=0
for x in dict.values():
    for i in range(len(x)):
         c+=1
print(c)


