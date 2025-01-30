list1=[18,52,76,3,79]
list2=[54,62,8,62,49]
r1=map(lambda x,y:x+y,list1,list2)
print(list(r1))
list3=[1,5,2,66,88,69,87]
def squre(a1):
    return a1*a1
a2=list(map(squre,list3))
print(a2)
