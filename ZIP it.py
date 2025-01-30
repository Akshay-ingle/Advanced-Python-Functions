s1={1,5,2,6,8,9}
s2={'a','g','b','f','r'}
s3=list(zip(s1,s2))
print(s3)
s4=[1,52,83,96,6]
s5=[5,8,9,3,4,76]
for x,y in zip(s4,s5[::-1]):
    print(x,y)
dict1=[1,5,3,9,8]
dict2=[1,2,7]
dict3={dict1:dict2 for dict1,dict2 in zip(dict1,dict2)}
print(dict3) 