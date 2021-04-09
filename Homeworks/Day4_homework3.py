#!/usr/bin/env python
# coding: utf-8

# In[ ]:



students = {"student1":[0.0,0.0,0.0,0.0],"student2":[0.0,0.0,0.0,0.0],"student3":[0.0,0.0,0.0,0.0],"student4":[0.0,0.0,0.0,0.0],"student5":[0.0,0.0,0.0,0.0]}#"midetermG","projectG","finalG"

def passingGrade(midterm,project,final):
    return(midterm*0.3 + project*0.3 + final*0.4)

def sortStudent():
    tempList = list()
    maxG = 0.0
    for v0,v1,v2,v3 in students.values():
        tempList.append(v3)
    tempList.sort(reverse=True)
    desStudents = list(range(len(tempList)))
    for k,[v0,v1,v2,v3] in students.items():
        for t in range(len(tempList)):
            if v3 == tempList[t]:
                desStudents[t] = k
    return(desStudents)

def enterStudentInfo():
    count=1
    for i in students.keys():
        print("Please enter the {}.Student's grades: ".format(count))
        midterm = float(input("student{}'s midterm: ".format(count)))
        if midterm < 0 or midterm > 100:
            print("Please enter a valid grade")
            midterm = float(input("student{}'s midterm: ".format(count)))
        project = float(input("student{}'s project: ".format(count)))
        if project < 0 or project > 100:
            print("Please enter a valid grade")
            project = float(input("student{}'s project: ".format(count)))
        final = float(input("student{}'s final: ".format(count)))
        if final < 0 or final > 100:
            print("Please enter a valid grade")
            final = float(input("student{}'s final: ".format(count)))
        students[i] = [midterm,project,final,passingGrade(midterm,project,final)]
        count+=1

print("Enter 5 students grades down below\n")
enterStudentInfo()
print("Students' Ranking\n")
for g in range(len(sortStudent())):
    print("{}.Student : {}".format(g+1,sortStudent()[g]))



# In[ ]:




