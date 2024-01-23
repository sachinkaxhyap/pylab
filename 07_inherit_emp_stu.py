# Write a python code to inherit employee class to student class

def main():
  emp1 = Employee("Sachin1", 201)
  emp2 = Employee("Sachin2", 202)
  print("Employee Details: ")
  emp1.displayInfo()
  emp2.displayInfo()

  print("\nStudent Details: ")
  stu1 = Student("Kashyap1", 203, 101)
  stu2 = Student("Kashyap2", 204, 102)
  stu1.displayInfo()
  stu2.displayInfo()

class Employee:
  def __init__(self, name, empID):
    self.name = name
    self.empID = empID

  def displayInfo(self):
    print(f"Name: {self.name}\nEmployee ID: {self.empID}")

class Student(Employee):
  def __init__(self, name, empID, stuID):
    super().__init__(name, empID)
    self.stuID = stuID

  def displayInfo(self):
    super().displayInfo()
    print(f"Student ID: {self.stuID}")

if __name__ == '__main__':
  main()