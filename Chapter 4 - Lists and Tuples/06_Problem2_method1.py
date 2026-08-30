#  Write a program to accept marks of 6 students and display them in a sorted manner.

stu1 = int(input("Enter marks of first student :- "))
stu2 = int(input("Enter marks of second student :- "))
stu3 = int(input("Enter marks of third student :- "))
stu4 = int(input("Enter marks of fourth student :- "))
stu5 = int(input("Enter marks of fifth student :- "))
stu6 = int(input("Enter marks of seventh student :- "))

Marks = [stu1,stu2,stu3,stu4,stu5,stu6]

Marks.sort()

print(Marks)