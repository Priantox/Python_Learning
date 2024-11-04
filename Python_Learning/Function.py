#1
# def fun_name(a,b,c):
#     r = a + b + c
#     print(r)

# fun_name(1,2,3);


#2
# def fun(a,b,c):
#     r = a + b + c
#     return r

# print(fun(10,5,8))


#3
# def net_sal(basic,allowance,deduction):
#     print('Basic: ',basic)
#     print('Allowance: ',allowance)
#     print('Deduction: ',deduction)

# net_sal(deduction=2000,allowance=1000,basic=2999)


#4
# def net_sal(basic,allowance,deduction):
#     print('Basic: ',basic)
#     print('Allowance: ',allowance)
#     print('Deduction: ',deduction)

# net_sal(2000,allowance=1000,deduction=2999)


#5
# def add(a,b = 0,c = 0):
#     return a + b + c

# print(add(4,5))
# print(add(4))
# print(add(b = 10,c = 2,a = 10))

# def addItem(item,L = []):
#     L.append(item)
#     return L

# L1 = [1,2,3,4]
# addItem(5,L1)
 

# def addItem(item,L = []):
#     L.append(item)
#     return L


# print(addItem(5))


#6
# def add(a,b,/,c,d,e,f):
#     return a + b + c + d + e + f

# c = add(2,7,d = 8,f = 1,e = 9,c = 10)
# print(c) 


#7
# def add(a,b,/,c,d,*,e,f):
#     return a + b + c + d + e + f

# r = add(2,4,3,4,f = 9,e = 8)
# print(r) 
 

#8
# def fun(*x):
#     print(x)

# fun(10,20,3,4)
# fun()
# fun(True,1)


# def fun(*args,a,b):
#     print(a,b,args)

# #fun(3,4)
# fun(1,2,34,454,3,a = 4,b = 5)


#9
# def fun(a,b,c):
#     print(a,b,c)

# L = [11,23,4]
# fun(L[0],L[1],L[2])
# fun(*L)

# str1 = 'Sky'
# fun(*str1)


#10
# def fun(a,b,c):
#     return a+1,b+1,c+1

# t = fun(10,20,30)
# print(t)

# x,y,z = fun(10,20,30)
# print(x,y,z) 


#11
# def fun(**args):
#     print(args)
#     print(type(args))

# fun(name = 'Alan',roll = 10,Addr = 'Dhaka')


# def fun(**args):
#     for x in args:
#         print(x,args[x])

# fun(name = 'Alan',roll = 10,Addr = 'Dhaka')


#12
# L = [1,23,4,5]
# L = (1,23,4,5)
# L = {1,23,4,5}

# itr = iter(L)
# print(next(itr))
# print(next(itr))
# print(next(itr))


#13
# def Days():
#     L = ['Sun','Mon','Tue','Wed','Thr','Fri','Sat']
#     i = 0

#     while True:
#         x = L[i]
#         i = (i + 1) % 7
#         yield x
    
# d = Days()
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))

# def Days():
#     L = [1 ,2,3,4,5,6,7]
#     i = 0

#     while True:
#         x = L[i]
#         i = (i + 1) % 7
#         yield x
    
# d = Days()
# print(next(d))
# print(next(d)) 
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))


#14
def display(name):
    print('hello',name)

d = display

d('john')
  