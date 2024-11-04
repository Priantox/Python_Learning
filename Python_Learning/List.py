mylist = ['John','smith','aric']
list1 = [0,1,2,3,4,5,6,7,8,9,10,100]

#1
# print(mylist)
# print(mylist[2])
# print(mylist[-2])


#2
# list1 = list((1,2,3,4,5))
# print(list1)


#3
# mylist = ['John',129]


#4
# list1[2] = 'Max'  


#5
#len(mylist)

#6
# print(list1[:])
# print(list1[3:])
# print(list1[3:8])
# print(list1[2:9:2])
# print(list1[-1:-10:-1])
# temp = list1[2:10 :2]
# print(temp)

#7
# list1[0:3] = [10,20,30]
#list1[0:3] = [10,20]
#list1[0:3] = [10,20,30,40]
# list1[::2] = [11,22,33,44,55]
# print(list1)

#8
# list2 = [1,2,3,4]
# list3 = [5,6,7,8]

# listi = list2 + list3
# listi = listi + [9,10,11]
# listi.extend([12,13])
# print(listi)

#9
# list2 = [1,2,3]
# list2 = list2*2
# print(list2)


#10
# print(1 in list1)
# print(23 not in list1)


#11
# for i in range(len(list1)):
#     print(list1[i])

# for i in range(len(list1) -1,-1,-1):
#     print(list1[i])


#12
#list1.append(100)
#list1.extend([100,200])
#list1.insert(19,11)
# L2 = list1.copy()
# print(id(list1[0]))
# print(id(L2[0]))


#13
# list1.pop()
# list1.pop(0)
#del list1[1]
#del list1[0:2]
#list1.remove(100)
#list1.clear()
#list1[:] = []
#del list1[:]
# print(list1)


#14
#print(list1.index(6))
listi = [1,3,5,4,3,46]
# print(listi.index(3,2))
# print(listi.index(3,2,6))
# print(listi.count(3))
#listi.reverse()
#listi.sort()
#listi.sort(reverse=True)
# listx = ['aa','yy','mm','BB','aa',"ZZ"]
# listx.sort(key=str.upper)
# print(listx)


#15
# L = []
# for x in range(10):
#     L.append(x)
# print(L)

# L2 = [x**2 for x in range(10)]
# print(L2)

# L3 = [x for x in(1,4,5,3,45,65) if x % 2 == 0]
# print(L3)

# L4 = [x.lower() for x in 'PyThOn']
# print(L4)

# L5 = [x for x in 'abjd4378y7$^#sjnds' if x.isalpha()]
# print(L5)

# data = input('Enter name ')
# L6 = data.split()
# print(L6)

# L6 = [input('Enter name ').split()]
# print(L6)


#16
# A = [[1,2,3],[4,5,6],[7,8,9]]
# B = [[9,8,7],[6,5,4],[3,2,1]]

# C = []

# for i in range(len(A)):
#     S = []
#     for j in range(len(A[0])):
#         S.append(A[i][j] + B[i][j])
#     C.append(S)
# print(C)

