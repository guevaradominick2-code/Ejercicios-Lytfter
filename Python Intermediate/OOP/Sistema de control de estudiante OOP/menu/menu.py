def menu_actions():

    menu_options_list = ["1. Add Student", "2. View all students", "3. View top 3 students","4. View Overall scores for all students", "5. Export data to CSV", "6. Import data to CSV", "7. List of students failing", "8. Delete student", "9. Exit"]
    
    while True:
        menu_display = "\n".join(menu_options_list)
        current_menu = f"""Menu options:
{menu_display} 
        --------------------------------
        Enter the number associated to the action :"""
            
        while True:
            try:
                main_menu = int(input(current_menu))
                if main_menu == 9:
                    print("Closing the program...")
                    return 
                elif main_menu < 1 or main_menu > 8:
                    raise ValueError
                return main_menu

            except ValueError:
                    print(f"Invalid Value- Insert valid number from the menu.")

def post_action_menu():
    while True:
        try:
            option = int(input("""
--------------------------------
1. Go back to menu
2. Close program
Enter option: """))
            if option == 1:
                return True
            elif option == 2:
                return False
            else:
                print("ERROR - Insert 1 or 2")
        except ValueError:
            print("ERROR - Insert a valid number")


