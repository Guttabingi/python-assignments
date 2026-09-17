#Assignment: Python Basics and Data Structures
#PART 1
# question 1

name ="Guttabingi Maria Concepta"
age = 28
height = 159.5
student = True
print(name)
print(age)
print(height)
print(student)

# question 2

name = "Abdurrahman"
age = 25
height = 1.75
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# PART 2

# question 3
Myfavouritefoods = ['nuts','rolex','fries','fruitcake','beans','beef']
print(Myfavouritefoods)
print(Myfavouritefoods[0], ',' ,Myfavouritefoods[-1])
Myfavouritefoods.append('samosas')
#print(Myfavouritefoods)
Myfavouritefoods.remove('nuts')
#print(Myfavouritefoods)
Myfavouritefoods[2]='chocolate'
print(Myfavouritefoods)

#question 4
scores = [75, 80, 65, 90, 85]
print(scores)
print(max(scores))
print(min(scores))
scores.append(70)
print(scores)

#PART 3
#question 5
DaysOfTheWeek=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
print(DaysOfTheWeek)
print(DaysOfTheWeek[0])
print(DaysOfTheWeek[-1])
#DaysOfTheWeek[0]='Monday'
#Answer: A tuple doesn't support item assignment while a list does i.e a tuple isn't mutable while a list is.

#PART 4
#question 6
numbers = [1, 2, 3, 4, 2, 5, 3, 6, 1]
setnumbers =set(numbers)
print(setnumbers)
#Answer: Some values have disappeared because sets do not support duplicate values.

#question 7
Languages=[ 'Python', 'Java', 'Python', 'C++', 'JavaScript','Python']
setLanguages=set(Languages)
print(setLanguages)
setLanguages.add('Django')
print(setLanguages)

#PART 5
#question 8
StudentDetails={'Name':'Naka','Age':24,'Course':'BCOM','Level':2,'Skills':'Java'}
print(StudentDetails)
print(StudentDetails['Name'])
StudentDetails['email']='naka678@gmail.com'
print(StudentDetails)
StudentDetails['Level']= 3
del StudentDetails['Age']
print(StudentDetails)

#Final Challenge
#question 9
students={
'student1':{'name': 'Jane Nambi','age': 22,'course': 'Backend Development','skills': ['Python, HTML, Git']
            },
'student2':{'name': 'Sandra Nalule','age': 28,'course': 'Frontend Development','skills': ['CSS, HTML, Git']
            },
'student3':{'name': 'Ayebale Avia','age': 24,'course': 'Backend Development','skills': ['Python, Java, Git']
            }
}
print(students)




#Assignment: Student Information Manager
namex='Ssaku Abdu'
agex=25
heightx=159.8
isenrolled=True

#1. List
Skillsx=['HTML','CSS','Python','JavaScript']
print(Skillsx[0])
Skillsx.append('SQL')
Skillsx.remove('CSS')
print(Skillsx)

#2. Tuple
favouritenos=(20,4,89)
print(favouritenos[1])

#3. Set
hobbies={'diving','reading','boardgames','reading'}
print(hobbies)
# The duplicate value was removed since sets don't support duplicate values
hobbies.add('singing')
#print(hobbies)

#4. Dictionary
studentx={
'namex': 'Ssaku Abdu',
'agex': 25,
'heightx': 159.8,
'isenrolled': True,
'Skillsx': ['HTML','CSS','Python','JavaScript'],
'favouritenos':[20,4,89],
'hobbies':['diving','reading','boardgames','reading']
}
#print(studentx)
print(studentx['namex'])
print(studentx['Skillsx'])
studentx['country']='Uganda'
#print(studentx)
studentx['agex']= 29
print(studentx)

#Bonus Challenge
namem= 'Guttabingi Maria Concepta'
Agem=28
Favoriteprogramminglag='Python'
studentmaria={
    'name':namem,
    'age':Agem,
    'favproglag':Favoriteprogramminglag
}
#print(studentmaria)
print(f'Hello {studentmaria['name']}!')
print(f'You are {studentmaria['age']} years old.')
print(f'Your favourite programming language is {studentmaria['favproglag']}.')












