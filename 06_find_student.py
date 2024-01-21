#  Write a python code to find student from a given list using class

class student():
  def __init__(self, name, ID):
    self.name = name
    self.ID = ID

  def displayInfo(self):
        print(f"Name: {self.name}\nID: {self.ID}\n")

  def findStudent(self, argu):
    if argu == self.name or argu == str(self.ID):
      student.displayInfo()

students = [
  student("Sachin1", 101),
  student("Sachin2", 102),
  student("Sachin3", 103),
  student("Sachin4", 104),
  student("Sachin5", 105),
  student("Sachin6", 106),
  student("Sachin7", 107),
  student("Sachin8", 108),
  student("Sachin9", 109),
  student("Sachin10", 110)
]

argu = input("Enter Name or ID to find a student: ")
for student in students:
  student.findStudent(argu)

