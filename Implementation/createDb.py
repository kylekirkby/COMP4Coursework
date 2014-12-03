import sqlite3

def create_table(db_name,table_name,sql):

    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        #expects a tuple - need comma after value in tuple
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it? y/n ?: ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
            else:
                print("The existing table was kept.")
        else:
            keep_table = False

        if not keep_table:
            cursor.execute(sql)
            db.commit()


def referential_integrity():
    with sqlite3.connect("Database.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        db.commit()

def create_client_table():
    
    sql = """CREATE TABLE Client(
    ClientID integer,
    ClientTitle text,
    ClientFirstName real,
    ClientSurname text,
    ClientAddrLine1 text,
    ClientAddrLine2 text,
    ClientAddrLine3 text,
    ClientAddrLine4 text,
    ClientEmail text,
    ClientPhoneNumber text,
    Primary Key(ClientID));"""

    create_table("Database.db","Client",sql)
        

def create_plasterer_table():

    sql = """CREATE TABLE Plasterer(
    PlastererID integer,
    PlastererTitle text,
    PlastererFirstName real,
    PlastererSurname text,
    PlastererAddrLine1 text,
    PlastererAddrLine2 text,
    PlastererAddrLine3 text,
    PlastererAddrLine4 text,
    PlastererEmail text,
    PlastererPhoneNumber text,
    PlasterDailyRate real,
    Primary Key(PlastererID));"""

    create_table("Database.db","Plasterer",sql)



def create_material_table():

    sql = """CREATE TABLE Material(
    MaterialID integer,
    MaterialName text,
    MaterialPrice real,
    Primary Key(MaterialID));"""

    create_table("Database.db","Material",sql)


def create_job_table():

    sql = """CREATE TABLE Job(
    JobID integer,
    ClientID integer,
    PlastererID integer,
    InvoiceID integer,
    JobDescription text,
    JobAddrLine1 text,
    JobAddrLine2 text,
    JobAddrLine3 text,
    JobAddrLine4 text,
    JobDaysWorked integer,
    JobComplete text,
    Primary Key(JobID),
    Foreign Key (ClientID) references Job(JobID),
    Foreign Key (PlastererID) references Plasterer(PlastererID),
    Foreign Key (InvoiceID) references Invoice(InvoiceID));"""

    create_table("Database.db","Job",sql)


def create_invoice_table():

    sql = """CREATE TABLE Invoice(
    InvoiceID integer,
    JobID integer,
    InvoiceAmountPreTax real,
    InvoiceAmountAfterTax real,
    InvoiceReceived integer,
    InvoiceDate text,
    InvoiceText text,
    InvoicePaid integer,
    Primary Key(InvoiceID),
    Foreign Key (JobID) references Job(JobID));"""Job

    create_table("Database.db","Invoice",sql)

                
def create_appointment_table():


    sql = """CREATE TABLE Appointment(
    AppointmentID integer,
    JobID text,
    AppointmentDate text,
    AppointmentTime text,
    Primary Key(AppointmentID),
    Foreign Key(JobID) references Job(JobID));"""


    create_table("Database.db","Appointment",sql)






def create_jobMaterials_table():

    sql = """CREATE TABLE JobMaterials(
    JobMaterialsID integer,
    JobID integer,
    MaterialID integer,
    JobMaterialsQuantity integer,
    Primary Key(JobMaterialsID),
    Foreign Key(JobID) references Job(JobID),
    Foreign Key(MaterialID) references Material(MaterialID));"""


    create_table("Database.db","JobMaterials",sql)


def populate_db():


    create_client_table()
    create_plasterer_table()
    create_material_table()
    create_job_table()
    create_invoice_table()
    create_appointment_table()
    create_jobMaterials_table()

    


if __name__ == "__main__":

    populate_db()
    referential_integrity()
