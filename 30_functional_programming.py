def compareStudents(student1, student2):
    if student1.getName() > student2.getName():
        return 1
    if student1.getName() < student2.getName():
        return -1
    return 0

def compareGPA(student1, student2):
    if student1.getGPA() > student2.getGPA():
        return 1
    if student1.getGPA() < student2.getGPA():
        return -1
    return 0

 
class Student():
    def __init__(self, name, major):
        '''both name and major are strings'''
        self.name = name
        self.major = major
        self.GPA = 0
 
    def getName(self):
        return self.name
 
    def setGPA(self, gpa):
        self.GPA = gpa
 
    def getGPA(self):
        return self.GPA
 
    def __str__(self):
        return self.name + '\'s GPA is ' + str(self.GPA)
