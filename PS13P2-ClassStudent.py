# Stephen Moy
# CIS 106 - W01
# 04/20/2024

# Problem Set 13 - Problems 2: Student Class

class Student:
  def __init__(self, first, last, districtcode, credits):
    self.first = first
    self.last = last
    self.districtcode = districtcode
    self.credits = credits
  
  def tuition(self):
    tuition = self.credits * 250 if self.districtcode == "I" else self.credits * 500
    return tuition

student1 = Student("Stephen", "Moy", "I", 15)
student2 = Student("Monica", "Crinion", "O", 15)

print("First Name: " + student1.first)
print("Last Name: " + student1.last)
print("District Code: " + student1.districtcode)
print("Credit Hours: " + str(student1.credits))
print("Tuition: $" + str(student1.tuition()))

print("\nFirst Name: " + student2.first)
print("Last Name: " + student2.last)
print("District Code: " + student2.districtcode)
print("Credit Hours: " + str(student2.credits))
print("Tuition: $" + str(student2.tuition()))