import json
from datetime import datetime, date

from datetime import date
today = str(date.today())

class Table:
    def __init__(self, table_id):
        self.table_id = table_id
        self.start_time = None
        self.end_time = None
        self.play_hours = ""
        self.play_minutes = ""
        self.availibility = True


    def string(self):
        return f"""
        Table ID: {self.table_id}
        Start Time: {self.start_time}
        End Time: {self.end_time}
        Total Time: {self.play_hours} Hours {self.play_minutes} Minutes
        Availibility: {self.availibility}
        """

tables_as_dict = []
all_tables = []

for i in range(1,13):
    table = Table(str(i))
    tables_as_dict.append(table.__dict__)
    all_tables.append(table)


while True:
    print("-" * 10)
    print("Welcome to the Cougar Game Room Management Application!")
    print("-" * 10)
    print("----Pool Table Menu----")
    menu_choice = input("""
    Enter 1: START/END Game
    Enter 2: VIEW ALL TABLES
    Enter 3: QUIT
    ENTER CHOICE: """)
    print("-" * 10)

    if(menu_choice == '3'):
        break

    elif(menu_choice == '2'):
            view_choice = input("""
            Enter 1: VIEW ALL TABLES
            Enter 2: VIEW OCCUPIED TABLES
            Enter 3: VIEW OPEN TABLES
            ENTER CHOICE: """)
            print("-" * 10)

            if(view_choice == '1'):
                for table in all_tables:
                    print(table.string())

            elif(view_choice == '2'):
                print("-" * 10)
                print("Occupied Tables: ")
                for table in all_tables:
                    if table.availibility == False:
                        print(f"Table: {table.table_id}")

            elif(view_choice == '3'):
                print("-" * 10)
                print("Open Tables: ")
                for table in all_tables:
                    if table.availibility == True:
                        print(f"Table: {table.table_id}")

            else:
                print("Your input was not valid. Please Enter a valid menu choice.")

    elif(menu_choice == '1'):
        while True:
            try:
                table = int(input("Select a table: "))
                table_choice = all_tables[(table - 1)]
                break
            except ValueError:
                print("Please select a valid table")
            except IndexError:
                print("Select a valid table 1 - 12")

        if(table_choice.availibility == True):
            table_start = input("Enter start of rent time: ")
            table_choice.start_time = table_start
            table_choice.availibility = False

        elif(table_choice.availibility == False):
            try:
                table_end = input("Enter end of rent time: ")
                table_choice.availibility = True
                table_choice.end_time = table_end
                with open(f"pool-9-30-2018.txt","w") as file_object:
                    file_object.write(table_choice.string())
            except:
                table_choice.availibility = True

    else:
        print("Enter a menu option: ")

    with open("current.json", "w") as file_object:
        json.dump(tables_as_dict,file_object, indent = 2)

print("""
 Thank you for using my pool management application
 Good Bye :)
 """)
