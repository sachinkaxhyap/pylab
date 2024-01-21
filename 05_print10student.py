# Write a python code to print 10 student details using class and lists

class student():
  def __init__(self, name, ID):
    self.name = name
    self.ID = ID

  def displayInfo(self):
        print(f"Name: {self.name}\nID: {self.ID}\n")

"""def displayInfo(students):
  for i, student in enumerate(students):
    print(f'''{i+1}.
Name: {student.name}
ID: {student.ID}
''')
"""

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

#displayInfo(students)
print("\nStudent Details:")
for i, student in enumerate(students):
  print(f"{i+1}.")
  student.displayInfo()


#RESET = '\033[0m'
#GREEN = '\033[32m'
#for i in students:
#  if i.ID%2==0:
#    print(f"{GREEN}{i.name}{RESET}")
#  else : print (i.name)