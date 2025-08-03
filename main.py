import mysql.connector
import pyttsx3
from stdiomask import getpass


def num():
    a = input("To perform the operation write the number associated with the Topic:")
    return a


def caps(a):
    a = a.upper()
    return a


def agen():
    while True:
        try:
            ad = input("Enter the Age:")
            if int(ad) >= 15 and int(ad) <= 105:
                break
            else:
                print()
                print("Enter a valid age for Vaccination")
                print()
        except:
            print()
            print("Enter a valid age for Vaccination")
            print()
    return ad


def aapkaaadhaaraapkipehchaan():
    while True:
        ad = input("Enter the Aadhaar Number:")
        if len(ad) == 12:
            break
        else:
            print()
            print("Please enter a valid Aadhaar Number")
            print()
    caps(ad)
    return ad


def aadhaar2(field):
    while True:
        ad = input(
            "Enter the Aadhaar Number of the person whose "
            + field
            + " is to be updated:"
        )
        if len(ad) == 12:
            print()
            break
        else:
            print()
            print("Please enter a valid Aadhaar Number")
            print()
    caps(ad)
    return ad


def phonen():
    while True:
        ph = input("Enter the Phone Number:")
        if len(ph) == 10:
            print()
            break
        else:
            print()
            print("Please enter a valid Phone Number")
            print()
    caps(ph)
    return ph


def daten():
    while True:
        try:
            dhat = input("Enter the Date of Vaccination (YYYY-MM-DD):")
            if len(dhat) == 10 and dhat[4] == "-" and dhat[7] == "-":
                if int(dhat[0:4]) >= 2020 and int(dhat[0:4]) <= 2022:
                    if int(dhat[5:7]) >= 1 and int(dhat[5:7]) <= 12:
                        if len(dhat[8:]) == 2:
                            if int(dhat[8:]) >= 1 and int(dhat[8:]) <= 31:
                                print()
                                break
                            else:
                                print()
                                print("Please enter a valid Date")
                                print()
                        else:
                            print()
                            print("Please enter a valid Date")
                            print()
                    else:
                        print()
                        print("Please enter a valid Date")
                        print()
                else:
                    print()
                    print("Please enter a valid Date")
                    print()
            else:
                print()
                print("Please enter a valid Date")
                print()
        except:
            print()
            print("Please enter a valid Date")
            print()
    caps(dhat)
    return dhat


def doseren():
    print()
    print("Choose from the Following:")
    print("1. 1st Dose")
    print("2. 2nd Dose")
    print("3. Booster Dose")
    abc = "y"
    while abc == "y":
        while True:
            try:
                x = input("To choose the Dose write the number associated with it:")
                y = int(x)
                break
            except:
                print("The input is wrong. Please try Again.")
                print(" ")
        if y > 0 and y < 4:
            abc = "n"
            break
        else:
            print("The input is wrong. Please try Again.")
            print(" ")
            abc = "y"
    if y == 1:
        return "FIRST"
    elif y == 2:
        return "SECOND"
    elif y == 3:
        return "BOOSTER"


def doseren2():
    print()
    print("Choose from the Following:")
    print("1. 1st Dose")
    print("2. 2nd Dose")
    print("3. Booster Dose")
    abc = "y"
    while abc == "y":
        while True:
            try:
                x = input("To update the Dose choose the number associated with it:")
                y = int(x)
                break
            except:
                print("The input is wrong. Please try Again.")
                print(" ")
        if y > 0 and y < 4:
            abc = "n"
            break
        else:
            print("The input is wrong. Please try Again.")
            print(" ")
            abc = "y"
    if y == 1:
        return "FIRST"
    elif y == 2:
        return "SECOND"
    elif y == 3:
        return "BOOSTER"


def vaccinen():
    print("Choose from the Following:")
    print("1. Sputnik")
    print("2. Covaxin")
    print("3. Covishield")
    abc = "y"
    while abc == "y":
        while True:
            try:
                x = input("To choose the Vaccine write the number associated with it:")
                y = int(x)
                break
            except:
                print("The input is wrong. Please try Again.")
                print(" ")
        if y > 0 and y < 4:
            abc = "n"
            break
        else:
            print("The input is wrong. Please try Again.")
            print(" ")
            abc = "y"
    if y == 1:
        return "SPUTNIK"
    elif y == 2:
        return "COVAXIN"
    elif y == 3:
        return "COVISHIELD"


def ask():
    a = input("Do you want to add another record (y/n):")
    answer = a.lower()[0]
    return answer


def ask2():
    a = input("Do you want to update another record (y/n):")
    answer = a.lower()[0]
    return answer


def ask3():
    a = input("Do you want to see another record (y/n):")
    answer = a.lower()[0]
    return answer


def seldb():
    query = "use " + database + ";"
    cursor.execute(query)
    print("Database Selected.")
    print()


def seltb():
    L2 = []
    cursor.execute("show tables;")
    print("You have the following Tables:")
    for x in cursor:
        L2.append(x)
    for i in range(1, len(L2) + 1):
        print(i, L2[i - 1][0])

    print()
    ab = "y"
    while ab == "y":
        try:
            tbname = int(
                input(
                    "Which table would you like to choose (Enter the number associated):"
                )
            )
            tbname2 = tbname
            if tbname > 0 and tbname <= len(L2):
                ab = "n"
                break
            else:
                print("There is some error. Please try Again.")
                print()
                ab = "y"
        except:
            print("There is some error. Please try Again.")
            print(" ")
            ab = "y"
    print()
    return L2[tbname - 1][0]


def edit(a):
    a = str(a)


engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.say(
    "we present to you our project on covid 19 vaccine database management system made by Anish Murali and Mudit Biedaani"
)
engine.runAndWait()


database2 = "PYTHON ROCKZ LOLZ"
print(" ")
print(" ")
print(" " * 45 + "*" * 70)
print(" " * 70 + "COMPUTER SCIENCE")
print(" " * 75 + "PROJECT")
print(" " * 58 + "COVID VACCINE DATABASE MANAGEMENT SYSTEM")
print(" " * 61 + "(BY MUDIT BIDANI AND ANISH MURALI)")
print(" " * 45 + "*" * 70)
print(" ")
print(" ")
engine.setProperty("rate", 145)
engine.say("please enter the credentials so that we can connect to your database")
engine.runAndWait()
while True:
    try:
        username = input("Enter your mysql username: ")
        password = getpass(prompt="Enter your mysql password: ")
        password = str(password)
        db = mysql.connector.connect(
            host="localhost", port="3307", user=username, passwd=password
        )
        cursor = db.cursor()
        engine.say(
            "Thank you for entering the credentials. we are now connected to your mysql database. Here are the following operations"
        )
        engine.runAndWait()
        break
    except:
        engine.setProperty("rate", 145)
        engine.say(
            "the credentials entered are wrong. we are not connected to your mysql database. please try again"
        )
        engine.runAndWait()
        print("The Login Credentials are Wrong. Please try Again")
        print(" ")
ans = "y"
while ans == "y":
    print(" ")
    print("~" * 78)
    print("Here are the operations that you can use")
    print("~" * 78)
    print(" ")
    print("You can do the following operations:")
    print("1.  Create Database")
    print("2.  Create Table")
    print("3.  Add records in the Table")
    print("4.  Sort the Records and View")
    print("5.  View Records from the Table")
    print("6.  Edit records in the Table")
    print("7.  Delete Table/Database")
    print("8.  Exit")
    abc = "y"
    while abc == "y":
        while True:
            try:
                x = num()
                y = int(x)
                break
            except:
                print("The input is wrong. Please try Again.")
                print(" ")
        if y > 0 and y < 9:
            ans = "n"
            break
        else:
            print("The input is wrong. Please try Again.")
            print(" ")
            ans = "y"
    print("_" * 78)
    print(" ")

    if y == 1:

        try:
            dbname = input("Enter the name of Database you would like to create:")
            caps(dbname)
            global database
            database = dbname
            database2 = database
            dbname2 = dbname
            dbname3 = "create database " + dbname + ";"
            cursor.execute(dbname3)
            print("Database", dbname2, "created successfully.")
            print()
            com = "use " + dbname2 + ";"
            cursor.execute(com)
            print()

            tbname = "Covid_Vaccine_Database"
            tbname2 = tbname

            s = "Name varchar(100) ,Age integer ,Gender varchar(6) ,Aadhar_Number varchar(12) ,Phone_Number varchar(12) ,Vaccine varchar(20) ,Dose varchar(8) ,Date date"

            command = "create table " + tbname + "(" + s + ");"
            cursor.execute(command)

            print("Table Covid Vaccine Database Created Successfully.")
            print()
        except:
            print("There is some error. The Database already exists.")
            print(" ")

    elif y != 1:
        if database2 == "PYTHON ROCKZ LOLZ":
            print("Please Create a Database First")
            print()
            ans = "y"
        else:

            if y == 7:
                abcd = "y"
                while abcd == "y":
                    s = input("Do you want to delete a Database or a Table :")
                    s = s.lower()
                    if s == "database" or s == "table":
                        abcd = "n"
                        break
                    else:
                        print(
                            "Please write either database or table in the input. Try Again."
                        )
                        print()
                        abcd = "y"
                if s == "database":
                    query = "drop database " + database + ";"
                    cursor.execute(query)
                    print("Database Deleted.")

                else:
                    seldb()
                    tbname = seltb()
                    command = "drop table " + tbname + ";"
                    cursor.execute(command)
                    print("Table Deleted.")
                    print()
            elif y == 2:
                seldb()
                while True:
                    try:
                        tbname = input(
                            "Enter the name of the table you would like to create: "
                        )
                        caps(tbname)
                        tbname2 = tbname
                        s = "Name varchar(100) ,Age integer ,Gender varchar(6) ,Aadhar_Number varchar(12) ,Phone_Number varchar(12) ,Vaccine varchar(20) ,Dose varchar(8) ,Date date"
                        command = "create table " + tbname + "(" + s + ");"
                        cursor.execute(command)
                        break
                    except:
                        print("There is some error. Please try Again.")
                        print(" ")
                print("Table " + tbname + " Created Successfully.")
                print()

            elif y == 5:
                seldb()
                tbname = seltb()
                print()
                engine.say(
                    "You have the following options to view Records from the Table. Which one do you want to choose"
                )
                engine.runAndWait()
                print("You have the following options to search Values from the Table:")
                print("1. Print All Records")
                print("2. Print Full Record of a Specific Detail")
                cba = "y"
                while cba == "y":
                    while True:
                        try:
                            x = num()
                            z = int(x)
                            break
                        except:
                            print("The input is wrong. Please try Again.")
                            print(" ")
                    if z > 0 and z < 3:
                        cba = "n"
                        break
                    else:
                        print("The input is wrong. Please try Again.")
                        print(" ")
                        cba = "y"
                print()
                s = 0
                query = "select * from " + tbname + ";"
                cursor.execute(query)
                results = cursor.fetchall()
                nrec = cursor.rowcount
                print("Total records are: ", nrec)
                for row in results:
                    s += 1
                if s != 0:
                    if z == 1:
                        command = "select * from " + tbname + ";"
                        cursor.execute(command)
                        data = cursor.fetchall()
                        nrec = cursor.rowcount
                        print("Total records found are: ", nrec)
                        print()
                        print(
                            "%20s" % "Name",
                            "%20s" % "Age",
                            "%10s" % "Gender",
                            "%20s" % "Aadhaar Number",
                            "%20s" % "Phone Number",
                            "%20s" % "Vaccine",
                            "%15s" % "Dose",
                            "%20s" % "Date",
                        )
                        print(
                            "==============================================================================================================================================================="
                        )
                        for row in data:
                            print(
                                "%20s" % row[0],
                                "%20s" % row[1],
                                "%10s" % row[2],
                                "%20s" % row[3],
                                "%20s" % row[4],
                                "%20s" % row[5],
                                "%15s" % row[6],
                                "%20s" % row[7],
                            )

                        print()

                    elif z == 2:
                        for i in range(1):
                            ans3 = "y"
                            while ans3 == "y":
                                try:
                                    engine.say(
                                        "here is the menu. What do you want to search."
                                    )
                                    engine.runAndWait()
                                    print("What Do You Want To Search:")
                                    print("1. Name")
                                    print("2. Gender")
                                    print("3. Aadhar_Number")
                                    print("4. Phone_Number")
                                    print("5. Vaccine")
                                    print("6. Dose")
                                    dcba = "y"
                                    while dcba == "y":
                                        while True:
                                            try:
                                                x = num()
                                                w = int(x)
                                                break
                                            except:
                                                print(
                                                    "The input is wrong. Please try Again."
                                                )
                                                print(" ")
                                        if w > 0 and w < 7:
                                            dcba = "n"
                                            break
                                        else:
                                            print(
                                                "The input is wrong. Please try Again."
                                            )
                                            print(" ")
                                            dcba = "y"
                                    if w == 1:
                                        name = input(
                                            "Enter the name to find his/her Details:"
                                        )
                                        caps(name)
                                        query = (
                                            "select * from "
                                            + tbname
                                            + " where Name='"
                                            + name
                                            + "';"
                                        )
                                        cursor.execute(query)
                                        results = cursor.fetchall()
                                        nrec = cursor.rowcount
                                        print("Total records found are: ", nrec)
                                        print()
                                        print(
                                            "%20s" % "Name",
                                            "%20s" % "Age",
                                            "%10s" % "Gender",
                                            "%20s" % "Aadhaar Number",
                                            "%20s" % "Phone Number",
                                            "%20s" % "Vaccine",
                                            "%15s" % "Dose",
                                            "%20s" % "Date",
                                        )
                                        print(
                                            "======================================================================================================================================================================"
                                        )
                                        for row in results:
                                            print(
                                                "%20s" % row[0],
                                                "%20s" % row[1],
                                                "%10s" % row[2],
                                                "%20s" % row[3],
                                                "%20s" % row[4],
                                                "%20s" % row[5],
                                                "%15s" % row[6],
                                                "%20s" % row[7],
                                            )

                                    elif w == 2:
                                        gender = input(
                                            "Enter the gender to find his/her Details:"
                                        )
                                        caps(gender)
                                        query = (
                                            "select * from "
                                            + tbname
                                            + " where Gender='"
                                            + gender
                                            + "';"
                                        )
                                        cursor.execute(query)
                                        results = cursor.fetchall()
                                        nrec = cursor.rowcount
                                        print("Total records found are: ", nrec)
                                        print()
                                        print(
                                            "%20s" % "Name",
                                            "%20s" % "Age",
                                            "%10s" % "Gender",
                                            "%20s" % "Aadhaar Number",
                                            "%20s" % "Phone Number",
                                            "%20s" % "Vaccine",
                                            "%15s" % "Dose",
                                            "%20s" % "Date",
                                        )
                                        print(
                                            "======================================================================================================================================================================"
                                        )
                                        for row in results:
                                            print(
                                                "%20s" % row[0],
                                                "%20s" % row[1],
                                                "%10s" % row[2],
                                                "%20s" % row[3],
                                                "%20s" % row[4],
                                                "%20s" % row[5],
                                                "%15s" % row[6],
                                                "%20s" % row[7],
                                            )
                                    elif w == 3:
                                        Aadhar = aapkaaadhaaraapkipehchaan()
                                        caps(Aadhar)
                                        query = (
                                            "select * from "
                                            + tbname
                                            + " where Aadhar_Number='"
                                            + Aadhar
                                            + "';"
                                        )
                                        cursor.execute(query)
                                        results = cursor.fetchall()
                                        nrec = cursor.rowcount
                                        print("Total records found are: ", nrec)
                                        print()
                                        print(
                                            "%20s" % "Name",
                                            "%20s" % "Age",
                                            "%10s" % "Gender",
                                            "%20s" % "Aadhaar Number",
                                            "%20s" % "Phone Number",
                                            "%20s" % "Vaccine",
                                            "%15s" % "Dose",
                                            "%20s" % "Date",
                                        )
                                        print(
                                            "======================================================================================================================================================================"
                                        )
                                        for row in results:
                                            print(
                                                "%20s" % row[0],
                                                "%20s" % row[1],
                                                "%10s" % row[2],
                                                "%20s" % row[3],
                                                "%20s" % row[4],
                                                "%20s" % row[5],
                                                "%15s" % row[6],
                                                "%20s" % row[7],
                                            )
                                    elif w == 4:
                                        Phone_Number = phonen()
                                        caps(Phone_Number)
                                        query = (
                                            "select * from "
                                            + tbname
                                            + " where Phone_Number='"
                                            + Phone_Number
                                            + "';"
                                        )
                                        cursor.execute(query)
                                        results = cursor.fetchall()
                                        nrec = cursor.rowcount
                                        print("Total records found are: ", nrec)
                                        print()
                                        print(
                                            "%20s" % "Name",
                                            "%20s" % "Age",
                                            "%10s" % "Gender",
                                            "%20s" % "Aadhaar Number",
                                            "%20s" % "Phone Number",
                                            "%20s" % "Vaccine",
                                            "%15s" % "Dose",
                                            "%20s" % "Date",
                                        )
                                        print(
                                            "======================================================================================================================================================================"
                                        )
                                        for row in results:
                                            print(
                                                "%20s" % row[0],
                                                "%20s" % row[1],
                                                "%10s" % row[2],
                                                "%20s" % row[3],
                                                "%20s" % row[4],
                                                "%20s" % row[5],
                                                "%15s" % row[6],
                                                "%20s" % row[7],
                                            )
                                    elif w == 5:
                                        Vaccine = vaccinen()
                                        query = (
                                            "select * from "
                                            + tbname
                                            + " where Vaccine='"
                                            + Vaccine
                                            + "';"
                                        )
                                        cursor.execute(query)
                                        results = cursor.fetchall()
                                        nrec = cursor.rowcount
                                        print("Total records found are: ", nrec)
                                        print()
                                        print(
                                            "%20s" % "Name",
                                            "%20s" % "Age",
                                            "%10s" % "Gender",
                                            "%20s" % "Aadhaar Number",
                                            "%20s" % "Phone Number",
                                            "%20s" % "Vaccine",
                                            "%15s" % "Dose",
                                            "%20s" % "Date",
                                        )
                                        print(
                                            "======================================================================================================================================================================"
                                        )
                                        for row in results:
                                            print(
                                                "%20s" % row[0],
                                                "%20s" % row[1],
                                                "%10s" % row[2],
                                                "%20s" % row[3],
                                                "%20s" % row[4],
                                                "%20s" % row[5],
                                                "%15s" % row[6],
                                                "%20s" % row[7],
                                            )
                                    elif w == 6:
                                        Dose = input(
                                            "Enter the Number Dose(s) to search Details:"
                                        )
                                        caps(Dose)
                                        query = (
                                            "select * from "
                                            + tbname
                                            + " where Dose='"
                                            + Dose
                                            + "';"
                                        )
                                        cursor.execute(query)
                                        results = cursor.fetchall()
                                        nrec = cursor.rowcount
                                        print("Total records found are: ", nrec)
                                        print()
                                        print(
                                            "%20s" % "Name",
                                            "%20s" % "Age",
                                            "%10s" % "Gender",
                                            "%20s" % "Aadhaar Number",
                                            "%20s" % "Phone Number",
                                            "%20s" % "Vaccine",
                                            "%15s" % "Dose",
                                            "%20s" % "Date",
                                        )
                                        print(
                                            "======================================================================================================================================================================"
                                        )
                                        for row in results:
                                            print(
                                                "%20s" % row[0],
                                                "%20s" % row[1],
                                                "%10s" % row[2],
                                                "%20s" % row[3],
                                                "%20s" % row[4],
                                                "%20s" % row[5],
                                                "%15s" % row[6],
                                                "%20s" % row[7],
                                            )

                                except:
                                    engine.say("No records found.")
                                    engine.runAndWait()
                                    print("No Records Found ")
                                    print(" ")
                                print()
                                ans3 = ask3()
                                print()
                else:
                    engine.say("Please choose a table which has Records")
                    print("Please choose a Table which has records.")

            elif y == 8:
                engine.say(
                    "If you exit this program then you wont be able to access the same database on this program again"
                )
                engine.runAndWait()
                print(
                    "If you exit this program then you wont be able to access the same database on this program again"
                )
                engine.say("Do you really want to exit")
                engine.runAndWait()
                ques = input("Do you really want to exit (y/n) :")
                ques = ques.lower()
                seuq = ques[0]
                if seuq == "y":
                    L = []
                    query = "show databases;"
                    cursor.execute(query)
                    for i in cursor:
                        L.append(i)
                    if (database,) in L:
                        ques2 = input("Do you want to delete the database (y/n) :")
                        ques2 = ques2.lower()[0]
                        if ques2 == "y":
                            query = "drop database " + database + ";"
                            cursor.execute(query)
                            engine.say("your database is deleted")
                            engine.runAndWait()
                            print("Database Deleted.")
                    engine.say("Thank you for trying our program")
                    engine.say(
                        "Stay Safe, Stay Healthy, Beware of COVID and remember, Health is Wealth"
                    )
                    engine.runAndWait()
                    print("Thankyou for Trying our Program")
                    b = "Stay Safe. Stay Healthy. Health is Wealth"
                    a = "\033[1m" + b + "\033[0m"
                    print(a)
                    ans = "n"
                    break

            elif y == 3:
                seldb()
                agya = "y"
                tbname = seltb()
                while agya == "y":
                    while True:
                        try:
                            engine.say(
                                "enter the value which need to be inserted in the table"
                            )
                            engine.runAndWait()
                            name = input("Enter the Name:")
                            age = agen()
                            gender = input("Enter the Gender:")
                            aadhar = aapkaaadhaaraapkipehchaan()
                            phone = phonen()
                            vaccine = vaccinen()
                            dose = doseren()
                            date = daten()
                            caps(name)
                            caps(gender)
                            caps(dose)
                            edit(name)
                            edit(age)
                            edit(gender)
                            edit(aadhar)
                            edit(phone)
                            edit(vaccine)
                            edit(dose)
                            edit(date)
                            break
                        except:
                            print("There is some Error in the input please try again")
                            print()
                    command = (
                        "insert into "
                        + tbname
                        + "(Name,Age,Gender,Aadhar_Number,Phone_Number,Vaccine,Dose,Date) values('"
                        + name
                        + "',"
                        + age
                        + ",'"
                        + gender
                        + "','"
                        + aadhar
                        + "','"
                        + phone
                        + "','"
                        + vaccine
                        + "','"
                        + dose
                        + "','"
                        + date
                        + "');"
                    )
                    cursor.execute(command)
                    db.commit()
                    print()
                    print("Data Entry Successful!")
                    print()
                    agya = ask()
                    print()
            elif y == 6:
                agyado = "y"
                while agyado == "y":
                    seldb()
                    tbname = seltb()
                    print()
                    s = 0
                    query = "select * from " + tbname + ";"
                    cursor.execute(query)
                    results = cursor.fetchall()
                    nrec = cursor.rowcount
                    print("Total records are: ", nrec)
                    if nrec != 0:
                        engine.say(
                            "Please enter the field in which you want to update the table"
                        )
                        engine.runAndWait()
                        print()
                        print("Which field would you like to update in the table.")
                        print("1. Name")
                        print("2. Age")
                        print("3. Gender")
                        print("4. Aadhar Number")
                        print("5. Phone Number")
                        print("6. Vaccine")
                        print("7. Dose")
                        print()
                        abcdef = "y"
                        while abcdef == "y":
                            while True:
                                try:
                                    x = num()
                                    option = int(x)
                                    break
                                except:
                                    print("The input is wrong. Please try Again.")
                                    print(" ")
                            if option > 0 and option < 8:
                                abcdef = "n"
                                break
                            else:
                                print("The input is wrong. Please try Again.")
                                print(" ")
                                abcdef = "y"
                        print("_" * 78)
                        print(" ")
                        if option == 1:
                            while True:
                                try:
                                    aad = aadhaar2("Name")
                                    n = input("Enter the new name of the person:")
                                    caps(n)
                                    cursor.execute(
                                        "update "
                                        + tbname
                                        + " set Name='"
                                        + n
                                        + "' WHERE Aadhar_Number='"
                                        + aad
                                        + "';"
                                    )
                                    db.commit()
                                    print("## Record Updated ##")
                                    break
                                except:
                                    print("WRONG INPUT. PLEASE TRY AGAIN")
                                    print()
                        elif option == 2:
                            while True:
                                try:
                                    aad = aadhaar2("Age")
                                    n = agen()
                                    cursor.execute(
                                        "update "
                                        + tbname
                                        + " set Age="
                                        + n
                                        + " WHERE Aadhar_Number='"
                                        + aad
                                        + "';"
                                    )
                                    db.commit()
                                    print("## Record Updated ##")
                                    break
                                except:
                                    print("WRONG INPUT. PLEASE TRY AGAIN")
                                    print()
                        elif option == 3:
                            while True:
                                try:
                                    aad = aadhaar2("Gender")
                                    n = input("Enter the new gender of the person:")
                                    caps(n)
                                    cursor.execute(
                                        "update "
                                        + tbname
                                        + " set Gender='"
                                        + n
                                        + "' WHERE Aadhar_Number='"
                                        + aad
                                        + "';"
                                    )
                                    db.commit()
                                    print("## Record Updated ##")
                                    break
                                except:
                                    print("WRONG INPUT. PLEASE TRY AGAIN")
                                    print()
                        elif option == 4:
                            while True:
                                try:
                                    aad = input(
                                        "Enter the Name of person whose Aadhar Number is to be updated:"
                                    )
                                    n = aapkaaadhaaraapkipehchaan()
                                    cursor.execute(
                                        "update "
                                        + tbname
                                        + " set Aadhar_Number='"
                                        + n
                                        + "' WHERE Name='"
                                        + aad
                                        + "';"
                                    )
                                    db.commit()
                                    print("## Record Updated ##")
                                    break
                                except:
                                    print("WRONG INPUT. PLEASE TRY AGAIN")
                                    print()
                        elif option == 5:
                            while True:
                                try:
                                    aad = aadhaar2("Phone Number")
                                    n = phonen()
                                    cursor.execute(
                                        "update "
                                        + tbname
                                        + " set Phone_Number='"
                                        + n
                                        + "' WHERE Aadhar_Number='"
                                        + aad
                                        + "';"
                                    )
                                    db.commit()
                                    print("## Record Updated ##")
                                    break
                                except:
                                    print("WRONG INPUT. PLEASE TRY AGAIN")
                                    print()
                        elif option == 6:
                            while True:
                                try:
                                    aad = aadhaar2("Vaccine Name")
                                    n = vaccinen()
                                    cursor.execute(
                                        "update "
                                        + tbname
                                        + " set Vaccine='"
                                        + n
                                        + "' WHERE Aadhar_Number='"
                                        + aad
                                        + "';"
                                    )
                                    db.commit()
                                    print("## Record Updated ##")
                                    break
                                except:
                                    print("WRONG INPUT. PLEASE TRY AGAIN")
                                    print()
                        elif option == 7:
                            while True:
                                try:
                                    aad = aadhaar2("No. of Doses")
                                    n = doseren2()
                                    caps(n)
                                    cursor.execute(
                                        "update "
                                        + tbname
                                        + " set Dose='"
                                        + n
                                        + "' WHERE Aadhar_Number='"
                                        + aad
                                        + "';"
                                    )
                                    db.commit()
                                    print("## Record Updated ##")
                                    break
                                except:
                                    print("WRONG INPUT. PLEASE TRY AGAIN")
                                    print()
                        agyado = ask2()
                    else:
                        print("Please choose a Table which has records.")

            elif y == 4:
                engine.say(
                    "You have the following options to arrange Values from the Table"
                )
                engine.runAndWait()
                print(
                    "You have the following options to arrange Values from the Table:"
                )
                print("1. Arrange the table in Ascending Order")
                print("2. Arrange the table in Descending Order")
                print()
                cba = "y"
                while cba == "y":
                    while True:
                        try:
                            x = num()
                            z = int(x)
                            break
                        except:
                            print("The input is wrong. Please try Again.")
                            print(" ")
                    if z > 0 and z < 3:
                        cba = "n"
                        break
                    else:
                        print("The input is wrong. Please try Again.")
                        print(" ")
                        cba = "y"
                seldb()
                if z == 1:
                    tbname2 = seltb()
                    print()
                    s = 0
                    query = "select * from " + tbname + ";"
                    cursor.execute(query)
                    results = cursor.fetchall()
                    nrec = cursor.rowcount
                    print("Total records are: ", nrec)
                    for row in results:
                        s += 1
                    if s != 0:
                        print()
                        try:
                            engine.say(
                                "enter the number by which you want to sort the table"
                            )
                            engine.runAndWait()
                            print("1. Arrange the Name in Ascending Order")
                            print("2. Arrange the Age in Ascending Order")
                            print("3. Arrange the Gender in Ascending Order")
                            print("4. Arrange the Vaccine in Ascending Order")
                            print("5. Arrange the Dose in Ascending Order")
                            print()
                            dcbaa = "y"
                            while dcbaa == "y":
                                while True:
                                    try:
                                        x = num()
                                        w = int(x)
                                        break
                                    except:
                                        print("The input is wrong. Please try Again.")
                                        print(" ")
                                if w > 0 and w < 6:
                                    dcbaa = "n"
                                    break
                                else:
                                    print("The input is wrong. Please try Again.")
                                    print(" ")
                                    dcbaa = "y"
                            print()
                            if w == 1:
                                query = (
                                    "select * from "
                                    + tbname
                                    + " order by name "
                                    + "asc"
                                    + ";"
                                )
                                cursor.execute(query)
                                results = cursor.fetchall()
                                nrec = cursor.rowcount
                                print("Total records are: ", nrec)
                                print()
                                print(
                                    "%20s" % "Name",
                                    "%20s" % "Age",
                                    "%10s" % "Gender",
                                    "%20s" % "Aadhaar Number",
                                    "%20s" % "Phone Number",
                                    "%20s" % "Vaccine",
                                    "%15s" % "Dose",
                                    "%20s" % "Date",
                                )
                                print(
                                    "======================================================================================================================================================================"
                                )
                                for row in results:
                                    print(
                                        "%20s" % row[0],
                                        "%20s" % row[1],
                                        "%10s" % row[2],
                                        "%20s" % row[3],
                                        "%20s" % row[4],
                                        "%20s" % row[5],
                                        "%15s" % row[6],
                                        "%20s" % row[7],
                                    )
                            elif w == 2:
                                query = (
                                    "select * from "
                                    + tbname
                                    + " order by Age "
                                    + "asc"
                                    + ";"
                                )
                                cursor.execute(query)
                                results = cursor.fetchall()
                                nrec = cursor.rowcount
                                print("Total records are: ", nrec)
                                print()
                                print(
                                    "%20s" % "Name",
                                    "%20s" % "Age",
                                    "%10s" % "Gender",
                                    "%20s" % "Aadhaar Number",
                                    "%20s" % "Phone Number",
                                    "%20s" % "Vaccine",
                                    "%15s" % "Dose",
                                    "%20s" % "Date",
                                )
                                print(
                                    "======================================================================================================================================================================"
                                )
                                for row in results:
                                    print(
                                        "%20s" % row[0],
                                        "%20s" % row[1],
                                        "%10s" % row[2],
                                        "%20s" % row[3],
                                        "%20s" % row[4],
                                        "%20s" % row[5],
                                        "%15s" % row[6],
                                        "%20s" % row[7],
                                    )
                            elif w == 3:
                                query = (
                                    "select * from "
                                    + tbname
                                    + " order by Gender "
                                    + "asc"
                                    + ";"
                                )
                                cursor.execute(query)
                                results = cursor.fetchall()
                                nrec = cursor.rowcount
                                print("Total records are: ", nrec)
                                print()
                                print(
                                    "%20s" % "Name",
                                    "%20s" % "Age",
                                    "%10s" % "Gender",
                                    "%20s" % "Aadhaar Number",
                                    "%20s" % "Phone Number",
                                    "%20s" % "Vaccine",
                                    "%15s" % "Dose",
                                    "%20s" % "Date",
                                )
                                print(
                                    "======================================================================================================================================================================"
                                )
                                for row in results:
                                    print(
                                        "%20s" % row[0],
                                        "%20s" % row[1],
                                        "%10s" % row[2],
                                        "%20s" % row[3],
                                        "%20s" % row[4],
                                        "%20s" % row[5],
                                        "%15s" % row[6],
                                        "%20s" % row[7],
                                    )
                            elif w == 4:
                                query = (
                                    "select * from "
                                    + tbname
                                    + " order by Vaccine "
                                    + "asc"
                                    + ";"
                                )
                                cursor.execute(query)
                                results = cursor.fetchall()
                                nrec = cursor.rowcount
                                print("Total records are: ", nrec)
                                print()
                                print(
                                    "%20s" % "Name",
                                    "%20s" % "Age",
                                    "%10s" % "Gender",
                                    "%20s" % "Aadhaar Number",
                                    "%20s" % "Phone Number",
                                    "%20s" % "Vaccine",
                                    "%15s" % "Dose",
                                    "%20s" % "Date",
                                )
                                print(
                                    "======================================================================================================================================================================"
                                )
                                for row in results:
                                    print(
                                        "%20s" % row[0],
                                        "%20s" % row[1],
                                        "%10s" % row[2],
                                        "%20s" % row[3],
                                        "%20s" % row[4],
                                        "%20s" % row[5],
                                        "%15s" % row[6],
                                        "%20s" % row[7],
                                    )
                            elif w == 5:
                                query = (
                                    "select * from "
                                    + tbname
                                    + " order by Dose "
                                    + "asc"
                                    + ";"
                                )
                                cursor.execute(query)
                                results = cursor.fetchall()
                                nrec = cursor.rowcount
                                print("Total records are: ", nrec)
                                print()
                                print(
                                    "%20s" % "Name",
                                    "%20s" % "Age",
                                    "%10s" % "Gender",
                                    "%20s" % "Aadhaar Number",
                                    "%20s" % "Phone Number",
                                    "%20s" % "Vaccine",
                                    "%15s" % "Dose",
                                    "%20s" % "Date",
                                )
                                print(
                                    "======================================================================================================================================================================"
                                )
                                for row in results:
                                    print(
                                        "%20s" % row[0],
                                        "%20s" % row[1],
                                        "%10s" % row[2],
                                        "%20s" % row[3],
                                        "%20s" % row[4],
                                        "%20s" % row[5],
                                        "%15s" % row[6],
                                        "%20s" % row[7],
                                    )
                        except:
                            print("No Records Found")
                            print(" ")
                        print()
                    else:
                        print("Please choose a Table wich has records.")

                elif z == 2:
                    tbname = seltb()
                    print()
                    s = 0
                    query = "select * from " + tbname + ";"
                    cursor.execute(query)
                    results = cursor.fetchall()
                    nrec = cursor.rowcount
                    print("Total records are: ", nrec)
                    for row in results:
                        s += 1
                    if s != 0:
                        print()

                        try:
                            engine.say(
                                "enter the number by which you want to sort the table"
                            )
                            engine.runAndWait()
                            print("1. Arrange the Name in Descending Order")
                            print("2. Arrange the Age in Descending Order")
                            print("3. Arrange the Gender in Descending Order")
                            print("4. Arrange the Vaccine in Descending Order")
                            print("5. Arrange the Dose in Descending Order")
                            print()
                            dcbaa = "y"
                            while dcbaa == "y":
                                while True:
                                    try:
                                        x = num()
                                        w = int(x)
                                        break
                                    except:
                                        print("The input is wrong. Please try Again.")
                                        print(" ")
                                if w > 0 and w < 6:
                                    dcbaa = "n"
                                    break
                                else:
                                    print("The input is wrong. Please try Again.")
                                    print(" ")
                                    dcbaa = "y"
                            print()
                            if w == 1:
                                query = (
                                    "select * from "
                                    + tbname
                                    + " order by name "
                                    + "DESC"
                                    + ";"
                                )
                                cursor.execute(query)
                                results = cursor.fetchall()
                                nrec = cursor.rowcount
                                print("Total records are: ", nrec)
                                print()
                                print(
                                    "%20s" % "Name",
                                    "%20s" % "Age",
                                    "%10s" % "Gender",
                                    "%20s" % "Aadhaar Number",
                                    "%20s" % "Phone Number",
                                    "%20s" % "Vaccine",
                                    "%15s" % "Dose",
                                    "%20s" % "Date",
                                )
                                print(
                                    "======================================================================================================================================================================"
                                )
                                for row in results:
                                    print(
                                        "%20s" % row[0],
                                        "%20s" % row[1],
                                        "%10s" % row[2],
                                        "%20s" % row[3],
                                        "%20s" % row[4],
                                        "%20s" % row[5],
                                        "%15s" % row[6],
                                        "%20s" % row[7],
                                    )
                            elif w == 2:
                                query = (
                                    "select * from "
                                    + tbname
                                    + " order by Age "
                                    + "DESC"
                                    + ";"
                                )
                                cursor.execute(query)
                                results = cursor.fetchall()
                                nrec = cursor.rowcount
                                print("Total records are: ", nrec)
                                print()
                                print(
                                    "%20s" % "Name",
                                    "%20s" % "Age",
                                    "%10s" % "Gender",
                                    "%20s" % "Aadhaar Number",
                                    "%20s" % "Phone Number",
                                    "%20s" % "Vaccine",
                                    "%15s" % "Dose",
                                    "%20s" % "Date",
                                )
                                print(
                                    "======================================================================================================================================================================"
                                )
                                for row in results:
                                    print(
                                        "%20s" % row[0],
                                        "%20s" % row[1],
                                        "%10s" % row[2],
                                        "%20s" % row[3],
                                        "%20s" % row[4],
                                        "%20s" % row[5],
                                        "%15s" % row[6],
                                        "%20s" % row[7],
                                    )
                            elif w == 3:
                                query = (
                                    "select * from "
                                    + tbname
                                    + " order by Gender "
                                    + "DESC"
                                    + ";"
                                )
                                cursor.execute(query)
                                results = cursor.fetchall()
                                nrec = cursor.rowcount
                                print("Total records are: ", nrec)
                                print()
                                print(
                                    "%20s" % "Name",
                                    "%20s" % "Age",
                                    "%10s" % "Gender",
                                    "%20s" % "Aadhaar Number",
                                    "%20s" % "Phone Number",
                                    "%20s" % "Vaccine",
                                    "%15s" % "Dose",
                                    "%20s" % "Date",
                                )
                                print(
                                    "======================================================================================================================================================================"
                                )
                                for row in results:
                                    print(
                                        "%20s" % row[0],
                                        "%20s" % row[1],
                                        "%10s" % row[2],
                                        "%20s" % row[3],
                                        "%20s" % row[4],
                                        "%20s" % row[5],
                                        "%15s" % row[6],
                                        "%20s" % row[7],
                                    )
                            elif w == 4:
                                query = (
                                    "select * from "
                                    + tbname2
                                    + " order by Vaccine "
                                    + "DESC"
                                    + ";"
                                )
                                cursor.execute(query)
                                results = cursor.fetchall()
                                nrec = cursor.rowcount
                                print("Total records are: ", nrec)
                                print()
                                print(
                                    "%20s" % "Name",
                                    "%20s" % "Age",
                                    "%10s" % "Gender",
                                    "%20s" % "Aadhaar Number",
                                    "%20s" % "Phone Number",
                                    "%20s" % "Vaccine",
                                    "%15s" % "Dose",
                                    "%20s" % "Date",
                                )
                                print(
                                    "======================================================================================================================================================================"
                                )
                                for row in results:
                                    print(
                                        "%20s" % row[0],
                                        "%20s" % row[1],
                                        "%10s" % row[2],
                                        "%20s" % row[3],
                                        "%20s" % row[4],
                                        "%20s" % row[5],
                                        "%15s" % row[6],
                                        "%20s" % row[7],
                                    )
                            elif w == 5:
                                query = (
                                    "select * from "
                                    + tbname2
                                    + " order by Dose "
                                    + "DESC"
                                    + ";"
                                )
                                cursor.execute(query)
                                results = cursor.fetchall()
                                nrec = cursor.rowcount
                                print("Total records are: ", nrec)
                                print()
                                print(
                                    "%20s" % "Name",
                                    "%20s" % "Age",
                                    "%10s" % "Gender",
                                    "%20s" % "Aadhaar Number",
                                    "%20s" % "Phone Number",
                                    "%20s" % "Vaccine",
                                    "%15s" % "Dose",
                                    "%20s" % "Date",
                                )
                                print(
                                    "======================================================================================================================================================================"
                                )
                                for row in results:
                                    print(
                                        "%20s" % row[0],
                                        "%20s" % row[1],
                                        "%10s" % row[2],
                                        "%20s" % row[3],
                                        "%20s" % row[4],
                                        "%20s" % row[5],
                                        "%15s" % row[6],
                                        "%20s" % row[7],
                                    )
                        except:
                            print("No Records Found")
                            print(" ")
                    else:
                        print("Please choose a Table which has records.")

    print()
    print()
    print()
    print()
    print()
    ans = "y"
