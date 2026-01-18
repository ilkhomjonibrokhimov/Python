file_name = 'employees.txt'

def add_employee():
    with open(file_name, 'a') as file:
        emp_id = input("Enter employee id: ")
        name = input("Enter name: ")
        position = input("What is the position: ")
        salary = input("How much is the salary: ")

        file.write(f"{emp_id}, {name}, {position}, ${salary}\n")
        print("Employee record added successfully.")


def view_employee():
    with open(file_name, 'r') as file:
        records = file.readlines()
        if not records:
            print("No employee info found!")
            return
        for record in records:
            print(record, end='')
        

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False

    with open(file_name, 'r') as file:
        for record in file:
            data = record.strip().split(',')
            if data[0] == emp_id:
                print(f"ID: {data[0]}, Name: {data[1]}, Position: {data[2]}, Salary: {data[3]}")
                found = True
                break


    if not found:
        print("Employee not found.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    records = []
    updated = False

    with open(file_name, 'r') as file:
        for record in file:
            data = record.strip().split(',')
            if data[0] == emp_id:
                name = input("Enter new name: ")
                position = input("Enter the position: ")
                salary = input("Enter the salary: ")
                records.append(f"{emp_id}, {name}, {position}, ${salary}\n")
                updated = True
            else:
                records.append(record)

    with open(file_name, 'w') as file:
        file.writelines(records)
    
    if updated:
        print("Employee record updated successfully.")
    else:
        print("Employee not found")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    records = []
    deleted = False

    with open(file_name, 'r') as file:
        for record in file:
            data = record.strip().split(',')
            if data[0] != emp_id:
                records.append(record)
            else:
                deleted = True

    with open(file_name, 'w') as file:
        file.writelines(records)

    if deleted:
        print("Employee deleted successfully.")
    else:
        print("Employee not found")


def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add new employee")
        print("2. View all employees")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee records")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employee()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting program. Good bye!")
            break
        else:
            print("Invalid choice. Please, try again")
        

menu()
    

