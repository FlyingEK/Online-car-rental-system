#NEONG YEE KAY_____WONG XIE LING
#TP060276__________TP060781

import os
import datetime
from datetime import datetime
from datetime import timedelta
from datetime import date

#Function to ask user if they want to proceed or exit
def proceed_or_exit():
    print("--------------------------------------------------")
    key = input("Enter 'c' to continue or enter 'e' to exit.")
    while True:
        #if user input c, returns true
        if key == "c":
            return True
        #if user input 3, returns false and go back to admin menu
        elif key == "e":
            admin_function()
            return False
        #prompt input again if invalid input is entered
        else:
            print("Invalid command, please try again.")
            key = input("Enter 'c' to continue or enter 'e' to exit.")

#Function to change list to string
def list_to_str(list):
    #join all field in the list using ";"
    s = ";".join(str(field) for field in list)
    return s

#Function to count lines in a file
def count_line(file_name):
    count = 0
    #open file to read as fh
    with open(file_name,"r") as fh:
        #loop the lines in fh and add 1 to the count value if the line is not empty
        for line in fh.readlines():
            if line != "":
                count = count + 1
    return count

#function to check if the date is within the duration
def duration_true(x, date):
    #get today's date
    today = date.today()
    #the duration
    margin = timedelta(days = x)
    #check if the date is within the duration
    if date >= today - margin:
        return True

#function for admin to enter car record and add it into car.txt
def enter_cardata():
    print("Please enter the data below.")
    print("Car ID, Price, Name, Colour")
    #loop the statements if proceed_or_exit() returns true
    while proceed_or_exit():
        ls = []
        #append 3 record column data get from user
        for col in range(0, 4):
            column_data = input()
            ls.append(column_data)
        ls.append("available for rent")
        str_ls = list_to_str(ls)
        #write the car record into the file
        with open("car.txt", 'a') as file:
            file.writelines("\n"+str_ls)
        #display the notification
        print("car.txt has been updated.")

#function for admin to modify car records in car.txt
def modify_car():
    #loop the statements if proceed_or_exit() returns true
    while proceed_or_exit():
        found = False
        search_value = input("Search for the record you want to modify using Car ID:")
        #open car.txt to read as search_file and temp.txt to write as temp_file
        with open("car.txt", "r") as search_file:
            with open("temp.txt", "w")as temp_file:
                #loop the line in search_file
                for line in search_file.readlines():
                    record = line.strip().split(";")
                    #search if the value inputted by user is in the search_file record
                    if search_value.lower() == record[0].lower():
                        print("Car ID:",record[0])
                        print("[1]Car price:",record[1])
                        print("[2]Car name:",record[2])
                        print("[3]Car colour:",record[3])
                        print("Car availability:",record[4])
                        # prompt the field no to modify and validate if it is integer and within the option
                        while True:
                            try:
                                modify_val = int(input("Please enter the field no to modify:"))
                                if modify_val >= 1 and modify_val <= 3:
                                    break
                                else:
                                    print("Invalid input. Please try again")
                            except:
                                print("Invalid input. Please try again.")
                        record[modify_val] = input("Please enter the new value:")
                        found = True
                    new_record = list_to_str(record)
                    #write all the records including the modified one into temp_file
                    temp_file.write(new_record)
                    temp_file.write("\n")
        #replace car.txt with temp.txt
        os.remove("car.txt")
        os.rename("temp.txt", "car.txt")
        #display notification
        if found:
            print("Data has been updated.")
        else:
            print("Search not found.")

#function to display customer payment record in a duration chosen by the admin.
def display_specificpayment():
    print("I want to see the payment records for last _______ days:")
    #prompt duration and validate if it is integer
    while True:
        try:
            duration = int(input("Please enter the number of days:"))
            break
        except:
            print("Invalid option. Please try again.")
    found = False
    print("Payment ID|customer name|car ID|price|date")
    #open customer_payment.txt to read as payment_file
    with open("customer_payment.txt", "r") as payment_file:
        #loop line in payment file
        for line in payment_file.readlines():
            record = line.strip().split(";")
            #format record[4] in payment file as date dd/mm/yyyy
            payment_date = datetime.strptime((record[4]), '%d/%m/%Y')
            #call the function to check if the payment_date is within the duration, if ture, display the record
            if duration_true(duration, payment_date.date()):
                found = True
                print(record)
    #display notification
    if not found:
        print("No record for the last",duration,"days.")

#function to display the lines in file
def display(file_name):
    #open file to read as display_file
    with open(file_name, "r")as display_file:
        #loop line in display_file to display each line
        for line in display_file.readlines():
            record = line.rstrip("\n")
            print(record)

#function to display the records of car rented out
def display_rentedCar():
    found = False
    #open car.txt to read as available_file
    with open("car.txt", "r")as available_file:
        # loop line in display_file
        for line in available_file.readlines():
            record = line.rstrip("\n").split(";")
            #search for the car record for rented out cars and display it
            if record[4] == "rented out":
                print(record[0:4])
                found = True
    #display notification if no record
    if not found:
        print("No car rented out currently.")

#function to display the records of car available for rent
def display_availableCar():
    found = False
    #open car.txt to read as available_file
    with open("car.txt", "r")as available_file:
        # loop line in available_file
        for line in available_file.readlines():
            record = line.rstrip("\n").split(";")
            # search for the car record for available cars and display it
            if record[4] == "available for rent":
                print(record[0:4])
                found = True
    # display notification if no record
    if not found:
        print("No car available for rent currently.")

#function to search for records by a value in a file
def search(file_name):
    # loop the statements if proceed_or_exit() returns true
    while proceed_or_exit():
        search_value = input("Enter search value:")
        found = False
        #open file to read as search_file
        with open(file_name, "r") as search_file:
            #loop the line in search_file
            for line in search_file.readlines():
                record = line.strip().split(";")
                record_str = list_to_str(record)
                #find if the search value is in the file and print it if found
                if search_value.lower() in record_str.lower():
                    found = True
                    print(record)
            # display notification if not found
            if not found:
                print("Search not found.")

#function to change the state of car from rented out to available for rent
def return_car():
    # loop the statements if proceed_or_exit() returns true
    while proceed_or_exit():
        found = False
        return_car = input("Enter the car ID to return a rented car:")
        #open car.txt to read as car_file and temp.txt to wrtie as temp_file
        with open("car.txt", "r") as car_file:
            with open("temp.txt", "w") as temp_file:
                #loop lines in car_file
                for line in car_file.readlines():
                    record = line.split(";")
                    record_list = []
                    #check if the car ID inputted by user match the car ID in record
                    if record[0] == return_car:
                        #append record[0] to record[3] into the list
                        for i in range(0, 4):
                            record_list.append(record[i])
                        #append "available for rent"
                        record_list.append("available for rent\n")
                        return_record = list_to_str(record_list)
                        #write the car record which is "available for rent" into temp_file
                        temp_file.write(return_record)
                        found = True
                    else:
                        #write the line as normal into temp_file
                        temp_file.write(line)
        #replace car.txt with temp.txt
        os.remove("car.txt")
        os.rename("temp.txt", "car.txt")
        #display notification
        if found:
            print("Data has been updated.")
        else:
            print("Search not found.")

#function to choose and delete a car record
def delete_car():
    # loop the statements if proceed_or_exit() returns true
    while proceed_or_exit():
        found = False
        search_value = input("Search for the record you want to delete using Car ID:")
        # open car.txt to read as search_file and temp.txt to wrtie as temp_file
        with open("car.txt", "r") as search_file:
            with open("temp.txt", "w")as temp_file:
                for line in search_file.readlines():
                    record = line.strip().split(";")
                    # check if the car ID inputted by user match the car ID in record
                    if search_value == record[0]:
                        print("Car ID:",record[0])
                        print("Car price:",record[1])
                        print("Car name:",record[2])
                        print("Car colour:",record[3])
                        print("Car availability:",record[4])
                        found = True
                        #Display delete confirmation message
                        print("Are you sure you want to delete",record[0],record[2],"?")
                        #if proceed_or_exit() returns true then proceed
                        if proceed_or_exit():
                            pass
                    else:
                        #write the line as normal into temp_file
                        temp_file.write(line)
    #replace car.txt with temp.txt
        os.remove("car.txt")
        os.rename("temp.txt", "car.txt")
        #display notification
        if found:
            print("Data has been deleted.")
        else:
            print("Search not found.")

#function to let the users choose type of records they want to display and proceed to the respective function
def display_option():
    print("Please select the records to display:")
    print("[1]Cars Rented Out")
    print("[2]Cars available for Rent")
    print("[3]Customer Bookings")
    print("[4]Customer payment")
    print("[5]Back to previous page")
    #get input of display option from user and validate it to be only integer
    while True:
        try:
            display_opt = int(input("Enter the number:"))
            break
        except:
            print("Invalid option. Please try again.")
    if display_opt ==1:
        display_rentedCar()
    elif display_opt ==2:
        display_availableCar()
    elif display_opt ==3:
        print("No|Booking date|customer name|carID|return date|duration")
        display("customer_booking.txt")
    elif display_opt ==4:
        display_specificpayment()
    elif display_opt ==5:
        admin_function()
    else:
        print("Invalid option. Please try again.")
    display_option()

#function to let the users choose type of records they want to search for and proceed to the respective function
def search_option():
    print("Please select which record you want to search for")
    print("[1]customer booking.")
    print("[2]customer payment.")
    # get input of search option from user and validate it to be only integer
    while True:
        try:
            search_opt = int(input("Enter the number:"))
            break
        except:
            print("Invalid option. Please try again.")
    if search_opt == 1:
        file_name = "customer_booking.txt"
        search(file_name)
    elif search_opt == 2:
        file_name = "customer_payment.txt"
        search(file_name)
    else:
        print("Invalid option. Please try again.")
        search_option()

#function to let the users choose functionality of admin they want to use and proceed to the respective function
def admin_function():
    print("Please type")
    print("[1]To add cars to be rented out")
    print("[2]To modify car details")
    print("[3]To read the records")
    print("[4]To search records")
    print("[5]To return a rented car")
    print("[6]To delete car record")
    print("[7]To modify the noticeboard")
    print("[8]Exit")
    # get input of admin option from user and validate it to be only integer
    while True:
        try:
            admin_opt = int(input("Enter the number:"))
            break
        except:
            print("Invalid input. Please try again")
    if admin_opt == 1:
        enter_cardata()
    elif admin_opt == 2:
        modify_car()
    elif admin_opt == 3:
        display_option()
    elif admin_opt == 4:
        search_option()
    elif admin_opt == 5:
        return_car()
    elif admin_opt == 6:
        delete_car()
    elif admin_opt == 7:
        modifynoticeboard()
        admin_function()
    elif admin_opt == 8:
        print("Log out successfully! Returning to the front page...")
        frontpage()
    else:
        print("Invalid option. Please try again.")
        admin_function()

#login function for the admin
def loginadmin():
    #give 3 attempts to user
    count = 3
    login = False
    #do while the attempt is not 0
    while count > 0:
        print('Please enter your')
        username = input('username:')
        password = input('password:')
        #open Admin.txt to read as fp
        with open("Admin.txt", 'r') as fp:
            #loop line in fp
            for line in fp.readlines():
                file_username, file_password = line.strip().split(";")
                #check if the username and password inputted are match in the record in fp, if true, direct to admin menu
                if username == file_username and password == file_password:
                    print("Login successfully! Welcome back,", username,".")
                    admin_function()
                    login = True
                    break
        #the loop is break if login successfully
        if login:
            break
        #attempts deducted by 1 if wrong login information is entered
        else:
            print("Incorrect username or password, please check again.")
            print(count-1, "attempt(s) left.")
            count = count - 1
    #login failed if attempt is 0 and redirect the user to front page
    if count == 0:
        print("Login failed.")
        print("Returning to front page...")
        frontpage()

#confirmation login for the customers before they can modify their personal data
def customer_confirmlogin():
    # give 3 attempts
    count = 3
    login = False
    # do while the attempt is not 0
    while count > 0:
        print('Please enter your')
        username = input('username:')
        password = input('password:')
        #open customerlogin.txt to read as fp
        with open("customerlogin.txt", 'r') as fp:
            #loop line in fp
            for line in fp.readlines():
                file_username, file_password = line.strip().split(";")
                # check if the username and password inputted are match in the record in fp, if true, return username to be used in modify_personaldetails()
                if username == file_username and password == file_password:
                    login = True
                    return username
        #attempts deduct by 1 if wrong login information is entered
        if not login:
            print("Incorrect username or password, please check again.")
            print(count-1, "attempt(s) left.")
            count = count - 1
    # attempt failed if attempt is 0 and redirect the user to front page
    if count == 0:
        print("Attempt failed.")
        print("Returning to front page...")
        frontpage()

#customer login function
def logincustomer():
    # give 3 attempts
    count = 3
    login = False
    # do while the attempt is not 0
    while count > 0:
        print('Please enter your')
        username = input('username:')
        password = input('password:')
        # open customerlogin.txt to read as fp
        with open("customerlogin.txt", 'r') as fp:
            # loop line in fp
            for line in fp.readlines():
                file_username, file_password = line.strip().split(";")
                # check if the username and password inputted are match in the record in fp, if true, proceed to registered customer menu
                if username == file_username and password == file_password:
                    print("Login successfully! Welcome back,", username,".")
                    registeredfunctions()
                    login = True
                    break
        # the loop is break if login successfully
        if login:
            break
        # attempts deduct by 1 if wrong login information is entered
        else:
            print("Incorrect username or password, please check again.")
            print(count-1, "attempt(s) left.")
            count = count - 1
    # attempt failed if attempt is 0 and redirect the user to front page
    if count == 0:
        print("Login failed.")
        print("Returning to front page...")
        frontpage()

#new customer register
def register():
    #opening the customerlogin.txt file to append as cl
    with open('customerlogin.txt', 'a') as cl:
        #opening the customerdetails.txt file to append as cd
        with open("customerdetails.txt", "a") as cd:
            #asking the user for a username
            registerusername = input("Enter a username:")
            #opening the customerlogin.txt file to read as clog
            with open('customerlogin.txt', 'r') as clog:
                #if the user input registerusername is found in clog
                if registerusername in clog.read():
                    print("This username is taken, please choose another username.")
                    register()
                #in the case that the if statement is false, the username chosen is appended into cl
                else:
                    cl.write('\n'+registerusername+';')
            #users will have to select a password
            registerpassword = input("Enter a password:")
            #password is written into cl
            cl.write(registerpassword)
            print("Registered successfully. Please add some personal details now.")
            #numbering with increment of +1 when adding a new line is added
            num = count_line("customerdetails.txt")+1
            numbering = ("M"+str(num))
            #username, name, password, phone number, email and address will be given by the user
            username = input("Enter a nickname. It does not have to be your real name. Nickname entered:")
            name = input("Please enter your real name. Name entered:")
            password = registerpassword
            phonenumber = input("Please enter your phone number:")
            email = input("Please enter your email address. Email address:")
            address = input("Please enter your home address. Home address:")
            #the input given will be written into cd
            cd.write('\n'+numbering+';'+username+';'+name+';'+password+';'+phonenumber+';'+email+';'+address)
            print("Customer details successfully added.")

#customer viewing personaldetails
def personaldetails():
        #users are prompted to give their username and password
        userpersonaldetails = input("Enter your username:")
        passpersonaldetails = input("Enter your password:")
        #customerdetails.txt is opened to read as f
        with open('customerdetails.txt', 'r') as f:
            #lines are stripped and split with ";"
            for line in f.readlines():
                record = line.rstrip("\n").split(";")
                #when the username and password given aligns with the record it is printed
                if record[2] == userpersonaldetails and record[3] == passpersonaldetails:
                    print(record[0:6])

#cusomter viewing rental history
def rental_history():
        userrentalhistory = input("Enter your username:")
        #opening the customerrentalhistory.txt to read as f
        with open('customerrentalhistory.txt', 'r') as f:
            #when the username is found in the records, it is displayed
            for line in f:
                record = line.rstrip("\n").split(";")
                if record[0] == userrentalhistory:
                    print(record[0:3])

#modifying any personal details
def modify_personaldetails():
    found = False
    username = customer_confirmlogin()
    #customerdetails.txt is opened to read as search_file
    with open("customerdetails.txt", "r") as search_file:
        #temp.txt is opened to write as temp_file
        with open("temp.txt", "w")as temp_file:
            rec_list = []
            #the lines in the file are split with ";"
            for line in search_file.readlines():
                record = line.strip().split(";")
                if username == record[2]:
                    found = True
                    print("Member ID:",record[0])
                    print("Member name:",record[1])
                    print("[1]username:",record[2])
                    print("[2]password:",record[3])
                    print("[3]phone number:",record[4])
                    print("[4]email address:",record[5])
                    print("[5]address:",record[6])
                    while True:
                        try:
                            modify_val = int(input("Please enter the field no to modify:"))
                            #field needs to be in the range of 1 to 5
                            if modify_val >= 1 and modify_val <=5:
                                break
                            else:
                                print("Invalid input. Please try again")
                        except:
                            print("Invalid input. Please try again")
                    #users enter the new value of what they want to modify
                    record[modify_val+1] = input("Please enter the new value:")
                #the new record is changed from list to string and written into the temp file
                new_record = list_to_str(record)
                temp_file.write(new_record)
                temp_file.write("\n")
    #the customerdetails.txt is removed and the temp.txt is renamed to customerdetails.txt
    os.remove("customerdetails.txt")
    os.rename("temp.txt", "customerdetails.txt")

    if found:
        print("Data has been updated.")

#modifying the noticeboard
def modifynoticeboard():
    #choice menu
    print("Please enter:")
    print("[1] If you would like to add new notices")
    print("[2] If you would like to delete any notice")
    print("[3] If you would like to delete all notices")
    while True:
        #as validation, if anything other than a number is accepted, the except will display "Please enter a valid number"
        try:
            user_input = int(input("Number entered:"))
            break
        except:
            print("Please enter a valid number.")
    if (user_input == 1):
        #noticeboard.txt is opened with append as f
        with open("noticeboard.txt", "a") as f:
            #numbering, date and the notice message will be added to f
            addnotice = input("Enter the notice message here:")
            dt = datetime.today().strftime("%d/%m/%Y")
            f.write(str(count_line("noticeboard.txt") + 1) + ";" + str(dt) + ";" + addnotice + "\n")
            print("Notice successfully added.")
    elif (user_input == 2):
        while proceed_or_exit():
            found = False
            notice = input("Enter the notice number:")
            #noticeboard.txt is opened with read as sf
            with open("noticeboard.txt", "r") as sf:
                #temp.txt is opened with write as tf
                with open("temp.txt", "w") as tf:
                    #record is split with ";" and if notice is found in record and if users still decide to proceed, the line will be deleted
                    for line in sf.readlines():
                        record = line.strip().split(";")
                        if notice == record[0]:
                            print("Are you sure you want to delete this notice?\n", record)
                            found = True
                            if proceed_or_exit():
                                pass
                        else:
                            tf.write(line)
            #noticeboard.txt is removed and the temp.txt is renamed to noticeboard.txt
            os.remove("noticeboard.txt")
            os.rename("temp.txt", "noticeboard.txt")

            if found:
                print("Notice removed.")
            else:
                print("Notice number does not exist.")
    elif (user_input == 3):
        with open("noticeboard.txt", "w") as f:
            print("Are you sure you would like to proceed with this?")
            if proceed_or_exit():
                #with truncate, everything in the file will be deleted.
                f.truncate()
                print("All notices have been deleted.")
    else:
        print("Enter a valid number.")
        modifynoticeboard()

#confirming the decision to start booking the car
def startbooking():
    print("--------------------------------------------------")
    key = input("Please enter:\n[1]To book a car\n[2]To terminate process\nNumber entered:")
    #when 1 is entered key returns as true and if 2 is entered it returns as false
    while True:
        if key == "1":
            return True
            break
        elif key == "2":
            return False
            break
        else:
            print("Please enter a valid number.")
            key = input("Please enter\n[1]To book a car\n[2]To terminate process\nNumber entered:")

#confirming on whether to go through with the transaction or not
def confirmation():
    print("--------------------------------------------------")
    confirmation = input("Please enter:\n[1]To confirm booking\n[2]To terminate transaction\nNumber entered:")
    while True:
        if confirmation == "1":
            print("Please make the cash payment at your nearest Super car rental services store now or within 24 hours or the transaction will be terminated.")
            break
        elif confirmation == "2":
            print("Transaction successfully terminated.")
            registeredfunctions()
            break
        else:
            print("Please enter a valid number.")
            confirmation = input("Please enter:\n[1]To confirm booking\n[2]To terminate transaction\nNumber entered:")

#customer booking the car
def customerbooking():
    #when startbooking is false, available cars will be displayed
    if startbooking():
        found = False
        display_availableCar()
        user_input = input("-------------------------------------------------------\nEnter the car ID to book a car:")
        #car.txt is opened with r as df
        with open("car.txt", "r") as df:
            #temp.txt is opened with w as tf
            with open("temp.txt", "w") as tf:
                #lines in df are split with ";"
                for line in df.readlines():
                    record = line.strip().split(";")
                    record_list = []
                    #"rented out" will be appended if the specified record aligns with user input and "available for rent"
                    if record[0] == user_input and record[4] == "available for rent":
                        for i in range(0, 4):
                            record_list.append(record[i])
                        record_list.append("rented out\n")
                        return_record = list_to_str(record_list)
                        tf.write(return_record)
                        found = True
                    else:
                        tf.write(line)
        #car.txt is removed and the temp.txt is renamed with car.txt
        os.remove("car.txt")
        os.rename("temp.txt", "car.txt")
        if found:
            print("Please complete the transaction process.\n------------------------------")
            #car.txt is opened with r as acf
            with open("car.txt", "r") as acf:
                #price, duration and total price will be shown to the customers
                for line in acf.readlines():
                    record = line.strip().split(";")
                    if user_input == record[0]:
                        price = record[1][2:]
                        date1, date2, days = duration()
                        total_price =int(price) * int(days)
                        day = print("at the price of RM", total_price)
                        print("Please enter your full name to book the car.")
                        print("**Make sure the name you enter is correct because it will be used to keep the record for booking.")
                        name = input()
                        confirmation()
            #pin.txt and temp.txt is opened with r and w and named as pinf and temp respectively
            with open("pin.txt", "r") as pinf:
                with open("temp.txt","w") as temp:
                    count = 1
                    for line in pinf.readlines():
                        record = line.strip().split(";")
                        #if record[1] states null and count>0, carID, name, price, start and end date as well as duration is written
                        if record[1] == "NULL" and count > 0:
                            ls = [record[0], user_input, name, "RM"+price, date1.strftime("%d/%m/%Y"), date2.strftime("%d/%m/%Y"), days]
                            str_ls = list_to_str(ls)
                            temp.write(str_ls+"\n")
                            count = count - 1
                        else:
                            temp.write(line)
            #pin.txt is removed and the temp.txt file is renmed with pin.txt
            os.remove("pin.txt")
            os.rename("temp.txt", "pin.txt")
        else:
            print("Invalid car ID or the car is currently not available for rent.")
            customerbooking()

#the duration of when till when the car will be booked for
def duration():
    while True:
        #try and except is used to make sure the user input is less than 15 days and to make sure input is a valid number
        try:
            user_input = int(input("Enter the number of days you want to rent the car for:"))
            assert  0< user_input < 15
            break
        except ValueError:
            print("Please enter a valid number.")
        except AssertionError:
            print("We only rent cars out for a maximum of 14 days. If you would like a longer duration, renew your booking once it ends.")
    #date, start date, end date and duration is displayed
    dt = datetime.today().replace(microsecond=0)
    sum = dt + timedelta(days=user_input)
    num = sum - dt
    print("The car will be booked from", dt, "until", sum,"for", num)
    return dt,sum,user_input

#verifying the pin number after customers make payment
def pin_verification():
    #count 3 is given to allow limited input attempts
    cnt = 3
    found = False
    while cnt > 0:
        while True:
            #try and except to only accept integer value
            try:
                pin = int(input("Please enter the pin number:"))
                break
            except:
                print("Invalid input. Please enter only integer value.")
        #opening pin.txt to r as pin_file and temp.txt to w as temp_file
        with open("pin.txt","r") as pin_file:
            with open("temp.txt","w") as temp_file:
                #when count reaches 0
                count = 0
                total_line = count_line("pin.txt")
                #lines in pin_file are split with ";"
                for line in pin_file.readlines():
                    record = line.strip().split(";")
                    count = count + 1
                    #when the input pin is the same in record [0] and record[1] does not equate to NULL
                    if str(pin) == record[0] and record[1] != "NULL":
                        rec = []
                        found = True
                        #when found true the pin number or record [0] is appended into the file followed by "XXX"
                        rec.append(record[0]+"XXX")
                        for i in range(1,7):
                            rec.append(record[i])
                        str_rec = list_to_str(rec)
                        if count < total_line:
                            temp_file.write(str_rec+"\n")
                        else:
                            temp_file.write(str_rec)
                    else:
                        temp_file.write(line)
        #the pin.txt is removed and the temp.txt is renamed with pin.txt
        os.remove("pin.txt")
        os.rename("temp.txt","pin.txt")
        #when found, the transaction is succssul, but if the wrong pin is given the count will decrease by one
        if found:
            print("Payment confirmed. Thank you.")
            return 1, rec
        else:
            print("Wrong pin, please try again.")
            print(cnt - 1, "attempt(s) left.")
            cnt = cnt - 1
    #once the count reaches 0, the transaction fails
    if cnt == 0:
        print("Transaction failed. Please contact customer service at supercars@gmail.com or head to your nearest car dealership if you are having problems on your PIN number.")
        print("Returning to the menu page...")
        registeredfunctions()
        return 0, "NULL"

#appending data into the respective files after the transaction is successful
def payment():
    true, record = pin_verification()
    if true == 1:
        ls = []
        ls2 = []
        ls3 = []
        #opening the customerpayment.txt to append as pay_file and the following are written into it after being converted into string
        with open("customer_payment.txt","a")as pay_file:
            no = count_line("customer_payment.txt")+1
            ls.append("P"+str(no))
            ls.append(record[2])
            ls.append(record[1])
            ls.append(record[3])
            p_date = date.today().strftime("%d/%m/%Y")
            ls.append(p_date)
            rec = list_to_str(ls)
            pay_file.write("\n"+rec)
        #customer_booking.txt is opened to append as book_file and numbering the records are written
        with open("customer_booking.txt","a")as book_file:
            no = count_line("customer_booking.txt")+1
            ls2.append("B"+str(no))
            ls2.append(record[4])
            ls2.append(record[2])
            ls2.append(record[1])
            ls2.append(record[3])
            ls2.append(record[5])
            ls2.append(record[6])
            rec2 = list_to_str(ls2)
            book_file.write("\n"+rec2)
        #customerrentalhistory.txt is also opened to a as rent_file, the following are also written into it
        with open ("customerrentalhistory.txt","a")as rent_file:
            ls3.append(record[2])
            ls3.append(record[1])
            ls3.append(record[4]+"-"+record[5])
            rec3 = list_to_str(ls3)
            rent_file.write("\n"+rec3)

#new customers registering
def registeredfunctions():
    print("Please type: \n[1] If you want to view personal details")
    print("[2] If you want to modify personal details")
    print("[3] If you want to view personal rental history")
    print("[4] If you want to view the noticeboard")
    print("[5] If you want to view details of cars to be rented out")
    print("[6] If you want to book a car")
    print("[7] If you want to verify your payment.")
    print("[8] If you want to log out.")
    while True:
        #integers are accepted, anything other than that, users will be shown that it is an invalid input
        try:
            user_input = int(input("Enter a number to proceed:"))
            break
        except:
            print("Invalid input. Please try again.")
    #when user_input is any of the numbers shown in the menu, the corresponding functions will be called
    if (user_input == 1):
        personaldetails()
        registeredfunctions()
    elif (user_input == 2):
        modify_personaldetails()
        registeredfunctions()
    elif (user_input == 3):
        rental_history()
        registeredfunctions()
    elif (user_input == 4):
        viewnoticeboard()
        registeredfunctions()
    elif (user_input == 5):
        display_availableCar()
        registeredfunctions()
    elif (user_input == 6):
        customerbooking()
        registeredfunctions()
    elif (user_input == 7):
        payment()
        registeredfunctions()
    elif (user_input == 8):
        print("Logged out successfully.")
        print("----------Thank you for visiting Super Car Rental Service----------")
        print("Returning to the front page...")
        frontpage()
    else:
        print("Invalid input. Please try again.")
        registeredfunctions()

#viewing the SCRS noticeboard
def viewnoticeboard():
    print("--------------------Welcome to Super Car Rental Service's noticeboard!--------------------")
    #opening noticeboard.txt to read as f to print the contents
    with open("noticeboard.txt", "r") as f:
        for line in f.readlines():
            record = line.strip().split(";"+"\n")
            print(record)

#users having no choice but to log in or register to view other details
def no_access():
    print("To access additional information please login or register.")
    while True:
        #accept only integers, any input aside from that will be rejected
        try:
            userlogin = int(input("Please type: \n [1] To login now \n [2] If you want to register \n [3] If you want to return to the front page \n Please choose a number:"))
            break
        except:
            print("Invalid input. Please try again.")
    if userlogin == 1:
        logincustomer()
    elif userlogin == 2:
        register()
    elif userlogin == 3:
        frontpage()
    else:
        print("Enter a valid number")

#the main page menu where users can start navigating through the program
def frontpage():
    print("---------Welcome to Super Car Rental Services!----------")
    print("Please type: \n[1]To view all cars available for rent.")
    print("[2]To view details of cars to be rented out.")
    print("[3]To book now.")
    print("[4]To login.")
    print("[5]To view the noticeboard.")
    print("[6]If you are an admin.")
    while True:
        #only integers are accepted with try and except
        try:
            user_input = int(input("Enter your choice:"))
            break
        except:
            print("Invalid input. Please try again.")
    if user_input == 1:
        display_availableCar()
    elif user_input == 2:
        no_access()
    elif user_input == 3:
        no_access()
    elif user_input == 4:
        logincustomer()
    elif user_input == 5:
        viewnoticeboard()
    elif user_input == 6:
        loginadmin()
    else:
        print("Please enter a valid number.\n----------Thank you for visiting Super Car Rental Services----------")
    frontpage()


frontpage()