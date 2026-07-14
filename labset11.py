
# labset 11
'''
 Develop Student Grade Tracker: 
 Accept multiple students’ names and marks.
  Store them in a listof tuples or dictionaries. 
  Display summary reports (average, topper, etc.). 
  '''
  
def calc_avg(students):
    total = sum(student['marks']for student in students)
    return total/len(students)

def find_topper(students):
    return max(students,key = lambda x : x['marks'])

def display_report(students):
    print("\n---- Students Report---------\n")
    for student in students:
        print(f"{student['name']} - {student['marks']}")
    avg = calc_avg(students)
    topper = find_topper(students)
    print("Class Average: ",avg)
    print(f"Topper: {topper['name']} - {topper['marks']}")

n = int(input("Enter the number of students: "))
students = []
for i in range(n):
    print(f"Enter the student {i+1} ")
    name = input("Enter the name of student {i+1}: ")
    marks = float(input(f"Enter the marks of {name}: "))

    students.append({'name':name , 'marks': marks})

display_report(students)
