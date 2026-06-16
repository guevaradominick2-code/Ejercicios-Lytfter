import csv
from actions.actions import student_exists
from Students_class import Student

def csv_data_export(path, students_data):
    
    flat_students_list = []
    
    for student in students_data:
    
        flat_student = {
            "Full Name": student.name,
            "Section": student.section,
            "Spanish": student.grades["Spanish"],
            "English": student.grades["English"],
            "Social": student.grades["Social"],
            "Science": student.grades["Science"]
        }
        flat_students_list.append(flat_student)
    
    with open(path, "w", encoding = "UTF-8", newline = "") as file:

        headers = flat_students_list[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(flat_students_list)



def csv_data_import(path, students_data):

    try:
        with open(path, "r", encoding= "UTF-8") as import_file:
            

            reader = csv.DictReader(import_file)

            for data in reader:

                if not student_exists(students_data, data["Full Name"], data["Section"]):
                    students = Student(data["Full Name"], data["Section"], float(data["Spanish"]), float(data["English"]), float(data["Social"]), float(data["Science"]))
                    students_data.append(students)
                else:
                    print(f"Student {data['Full Name']} from section {data['Section']} already exists, skipping...")

    except FileNotFoundError as ex:
        print(f"ERROR - Check if the file correctly located in this folder or create a new file named (Massive list upload.csv)")


