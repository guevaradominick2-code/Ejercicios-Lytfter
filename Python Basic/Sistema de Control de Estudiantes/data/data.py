import csv
from actions.actions import student_exists

def csv_data_export(path, students_data):
    
    flat_students_list = []
    
    for student in students_data:
    
        flat_student = {
            "Full Name": student["Full Name"],
            "Section": student["Section"],
            "Spanish": student["Grades"]["Spanish"],
            "English": student["Grades"]["English"],
            "Social": student["Grades"]["Social"],
            "Science": student["Grades"]["Science"]
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

                new_data = {"Full Name" : data["Full Name"],
                                "Section" : data["Section"],
                                "Grades" :{"Spanish": float(data["Spanish"]),
                                        "English": float(data ["English"]),
                                        "Social": float(data["Social"]),
                                        "Science": float(data["Science"])
                                }}
                if not student_exists(students_data, new_data["Full Name"], new_data["Section"]):
                    students_data.append(new_data)
                else:
                     print(f"Student {new_data['Full Name']} from section {new_data['Section']} already exists, skipping...")

    except FileNotFoundError as ex:
        print(f"ERROR - Check if the file correctly located in this folder or create a new file named (Massive list upload.csv)")


