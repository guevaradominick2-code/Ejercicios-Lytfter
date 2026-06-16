from Students_class import Student

def get_valid_name():
        
        while True:
            try:
                student_name = input("Insert Student Full name: ")
                if not student_name:
                    print("ERROR - NAME MUST NOT BE EMPTY")
                    continue
                for index in student_name:
                    if index.isdigit():
                        raise ValueError
                else:
                        break
            except ValueError as ex:
                print("ERROR - NAME MUST NOT CONTAIN NUMBERS")    
        return student_name

def get_valid_section():
        while True:
            try:    
                student_section = input("Insert student's section:  ")
                if len(student_section) == 3 and student_section[0].isdigit() and student_section[1].isdigit() and student_section[2].isalpha():
                        break
                else:
                        raise ValueError
            except ValueError as ex2:
                print(f'ERROR - Section must contain the information according the format (YearCourse and Subgroup)')    
        return student_section

def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Insert {subject} score: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("ERROR - Scores must be numbers from 0 to 100")
        except ValueError:
            print("ERROR - Scores must be in number format")
        
def add_student(students_data):

    

    students_counter = 1
    
    while True:
        

        try: 
            students_quantity = int(input("Digit how many students are you adding: " ))
            break
        except ValueError as ex:
            print(f"Error - Insert the quantity in format number")
        

    while students_counter <= students_quantity:
        print(f"""Add the information of the student number {students_counter}
-------------------------------------------------------------------------------""")
        name = get_valid_name()
        section = get_valid_section()

        if student_exists(students_data, name, section):
            print(f"Error - Student {name} from the {section} already exists in dataset")
            students_counter += 1
        else:
            spanish_grade = get_valid_grade ("Spanish")
            english_grade = get_valid_grade ("English")
            social_grade = get_valid_grade ("Social")
            science_grade = get_valid_grade ("Science")

            student = Student(name, section, spanish_grade, english_grade, social_grade, science_grade)
            students_data.append(student)
            students_counter += 1

    return students_data

def view_all_students(students_data):

    print(f"{"Full Name".ljust(30)}{"Section".ljust(10)}{"Spanish".ljust(10)}{"English".ljust(10)}{"Social".ljust(10)}{"Science".ljust(10)}")

    for students in students_data:
        print (f"{students.name.ljust(30)}{students.section.ljust(10)}{str(students.grades["Spanish"]).ljust(10)}{str(students.grades["English"]).ljust(10)}{str(students.grades["Social"]).ljust(10)}{str(students.grades["Science"]).ljust(10)}")
        
def top_3_students(students_data):

    
    print(f"""Top 3 Students:
---------------------------------
{"Full Name".ljust(30)}{"Section".ljust(20)}{"Average Score".ljust(10)}""")
    
    students_data.sort(key=lambda student: ((student.grades["Spanish"]+student.grades["English"]+student.grades["Social"]+student.grades["Science"])/4), reverse = True)
    
    for name in students_data[:3]:
        print(f"{name.name.ljust(30)}{name.section.ljust(20)}{(name.grades["Spanish"]+name.grades["English"]+name.grades["Social"]+name.grades["Science"])/4}")

def all_students_average_grades(students_data):

    print(f"""Average Score for all students:
---------------------------------
{"Full Name".ljust(30)}{"Section".ljust(20)}{"Average Score".ljust(10)}""")
    
    students_data.sort(key=lambda student: student.name)

    for name in students_data[0:]:
        print(f"{name.name.ljust(30)}{name.section.ljust(20)}{(name.grades["Spanish"]+name.grades["English"]+name.grades["Social"]+name.grades["Science"])/4}")

def students_failing(students_data):

    failing_list = []

    for students in students_data:
        
        if students.grades["Spanish"] < 60 or students.grades["English"] < 60 or students.grades["Social"] < 60 or students.grades["Science"] < 60:
            
            failing_grades = {}
            if students.grades["Spanish"] < 60:
                failing_grades["Spanish"] = students.grades["Spanish"]
            if students.grades["English"] < 60:
                failing_grades["English"] = students.grades["English"]
            if students.grades["Social"] < 60:
                failing_grades["Social"] = students.grades["Social"]
            if students.grades["Science"] < 60:
                failing_grades["Science"] = students.grades["Science"]
        
            failing_student_data = {"Full Name": students.name,
                                    "Section": students.section,
                                    "Failing Grades": failing_grades

            }
            failing_list.append(failing_student_data)
    return failing_list                         
    
def failing_students_display(failing_list):

    print(f"{"Full Name".ljust(30)}{"Section".ljust(10)}{"Spanish".ljust(10)}{"English".ljust(10)}{"Social".ljust(10)}{"Science".ljust(10)}")

    for students in failing_list:
        print (f"{students["Full Name"].ljust(30)}{students["Section"].ljust(10)}{str(students["Failing Grades"].get("Spanish", "-")).ljust(10)}{str(students["Failing Grades"].get("English", "-")).ljust(10)}{str(students["Failing Grades"].get("Social", "-")).ljust(10)}{str(students["Failing Grades"].get("Science", "-")).ljust(10)}")

def student_exists(students_data, name, section):

    for students in students_data:
        if students.name.lower() == name.lower() and students.section.lower() == section.lower():
            return True
    return False

def delete_confirmation(name, section):

    while True:
            try:
                confirmation = int(input(f"""Are you sure that you want to delete the student {name} of the section {section} from system
            ----------------------------------------------------------                             
                1. Press 1 to continue
                2. Press 2 for cancel action:
----------------------------------------------
"""))
                break
            except ValueError as ex:
                print("ERROR - Value must be inserted in digit format")
    return confirmation

def student_delete(students_data):
    
    name = get_valid_name()
    section = get_valid_section()

    
    if student_exists(students_data, name, section):
        confirmation = delete_confirmation(name, section)
        if confirmation == 1:
            for students in students_data:
                if students.name.lower() == name.lower() and students.section.lower() == section.lower():
                    students_data.remove(students)
                    print(f"Student {name} deleted successfully")
                    break
        elif confirmation == 2:
            print("Action canceled...")
                
        else:
            print("Error - Invalid Number")
    else:
        print("Student does not exist in the dataset")
    
    


