#1
student = {'name': 'John','age': 25,'courses': ['Math','compsci']}
#print(student['age'])

#2
# student['phone'] = '2234324'
# print(student.get('phone','Not Found'))

#3
# student.update({'name': 'mica','age': 58})
# print(student)

#4
# del student['age']
# print(student)

#5
# print(student.keys())
# print(student.values())
# print(student.items())

#6
for key in student.items():
    print(key)