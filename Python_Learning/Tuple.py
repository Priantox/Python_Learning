#1
tuple1 = ('jack',89,100)
#print(tuple1[2])


#2
# t1 = ()
# print(t1)


#3
# t2 = (10,)
# print(type(t2))

#4
# t4 = tuple([1,2,3,4,5])
# print(type(t4))


#5
# t6 = tuple('Python')
# print(t6)


#6
# t7 = 10,20,30,40
# print(type(t7))
# print(t7)

# a,b,c,d = t7
# print(a)
# print(b)
# print(c)
# print(d)


#7
# L1 = [1,2,3,4,5]
# a,b,c,d,e = L1
# print(a)
# print(b)

# a,b,c = 'SKY'
# print(a)
# print(b)
# print(c)


#8
# t9 = 10,2,3,4,4,5,7
# a,b,*c = t9
# print(a)
# print(b)
# print(c)



#9
# t1 = tuple(x for x in range(10))
# print(t1)

# t2 = (*(x for x in range(10)),)
# print(t2)

#t3 = (*(x for x in range(1,10,2)),)
#print(t3) 
# t4 = (*(x for x in 'python'),)
# print(t4)
# t5 = (*(x for x in 'PyThoN' if x.islower()),)
# print(t5)
# t6 = tuple(x**2 for x in (1,2,4,5,3))
# print(t6)


 
#10
# t1 = (1,1,3,1,3,4,2)
# print(t1.count(2))
# print(t1.index(2))


#11
t1 = (1,2,34,5)
t2 = (5,4,3)
t = t1 + t2
print(t)

