import menu.menu
import actions.actions
import data.data

students_data = [{"Full Name" : "Maria Vargas",
                      "Section" : "12A",
                      "Grades" :{ "Spanish": 97,
                                  "English" : 100,
                                   "Social" : 46,
                                   "Science": 96, 
                    }},
                    {"Full Name" : "Dominick Guevara",
                          "Section" : "12A",
                          "Grades" :{ "Spanish": 70,
                                  "English" : 45,
                                   "Social" : 90,
                                   "Science": 50 
                    }},{"Full Name" : "Bamba Guevara",
                          "Section" : "12A",
                          "Grades" :{ "Spanish": 100,
                                  "English" : 100,
                                   "Social" : 100,
                                   "Science": 100 
                    }}

    ]

def main():

    while True:
        options = menu.menu.menu_actions()
        if options == 1:
            actions.actions.add_student(students_data)
        elif options == 2:
            actions.actions.view_all_students(students_data)
        elif options == 3:
            actions.actions.top_3_students(students_data)
        elif options == 4:
            actions.actions.all_students_average_grades(students_data)
        elif options == 5:
            data.data.csv_data_export("Full Students List.csv",students_data)
            print("CSV File has been downloaded...")
        elif options == 6:
            data.data.csv_data_import("Massive list upload.csv",students_data)
            print("CSV File has been uploaded...")
        elif options == 7:
            actions.actions.failing_students_display(actions.actions.students_failing(students_data))
        elif options == 8:
            actions.actions.student_delete(students_data)
        elif options == 9:
            print("Closing the program...")
            break

        if not menu.menu.post_action_menu():
            print("Closing the program...")
            break

main()