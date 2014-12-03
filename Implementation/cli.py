import sqlite3


def add_client(db_name):

    values = ()

    complete = False

    while complete == False:

        try:
            accepted = False
            while accepted == False:
                try:
                    title = input("Enter title: ")
                    if title == "":
                        raise ValueError
                    else:
                        accepted = True
                except ValueError:
                    print("Please enter a correct title")
                    
            accepted = False
            while accepted == False:
                try:
                    firstName = input("Enter First Name: ")
                    if title == "":
                        raise ValueError
                    else:
                        accepted = True
                except ValueError:
                    print("Please enter a correct title")

                    
            firstName = input("Enter First Name: ")
            if firstName == "": raise ValueError
            surname = input("Enter Surname: ")
            if surname == "": raise ValueError
            addrLine1 = input("Enter Street: ")
            addrLine2 = input("Enter Town/City: ")
            addrLine3 = input("Enter County: ")
            addrLine4 = input("Enter Post Code: ")
            email = input("Enter Email: ")
            phoneNumber = input("Enter Phone Number: ")

            values = values + (title,)
            values = values + (firstName,)
            values = values + (surname,)
            values = values + (addrLine1,)
            values = values + (addrLine2,)
            values = values + (addrLine3,)
            values = values + (addrLine4,)
            values = values + (email,)
            values = values + (phoneNumber,)

            complete = True
            
        except ValueError:
            print("Please enter a correct Value!!")
        
    with sqlite3.connect(db_name) as db:
    
        cursor = db.cursor()
        sql = """ insert into Client(
ClientTitle,
ClientFirstName,
ClientSurname,
ClientAddrLine1,
ClientAddrLine2,
ClientAddrLine3,
ClientAddrLine4,
ClientEmail,
ClientPhoneNumber
) values (?,?,?,?,?,?,?,?,?)"""

        
        cursor.execute(sql,values)
        db.commit()







def menu():

    print("Plastering Job Management Application")
    print()
    print("1. Add a Client")
    print("2. Add a Plasterer")
    print("3. Add a Material")
    print("4. Add a Job")
    print("5. Add a Appointment")
    print("6. Add a Invoice")
    print("7. Add a Job Material")
    print("0. Exit")
    print()

def main():
    db_name = "Database.db"
    exitMenu = False
    while exitMenu == False:
        menu()
        try:
            choice = int(input("Enter Option: "))
            if choice == 1:
                add_client(db_name)
            elif choice == 2:
                add_plasterer(db_name)
            elif choice == 3:
                add_material(db_name)
            elif choice == 4:
                add_job(db_name)
            elif choice == 5:
                add_appointment(db_name)
            elif choice == 6:
                add_invoice(db_name)
            elif choice == 7:
                add_jobMaterial(db_name)
            elif choice == 0:
                exitMenu = True
            else:
                print("Please enter a valid choice!!")
                
        except ValueError:
            
            print("Please enter an integer!")
    


if __name__ == "__main__":

    main()
