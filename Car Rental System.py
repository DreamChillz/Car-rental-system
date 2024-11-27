import arrow
from datetime import datetime

#Importing list of staff users
staff_data_list = []
with open('Staff_Data.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split each line into fields using comma as the delimiter
        fields = line.strip().split(', ')
        # Append the fields to the data list as a tuple or list
        staff_data_list.append(fields)
file.close()

StaffID = 0
StaffName = 1
Password = 2
StaffRoles = 3
DateOfRegister = 4

renting_rate_list = []
with open('CarRentingRate.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split each line into fields using comma as the delimiter
        fields = line.strip()
        # Append the fields to the data list as a tuple or list
        renting_rate_list.append(fields)
file.close()

# Importing the list of cars
car_list = []
with open('Car_Details.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split each line into fields using comma as the delimiter
        fields = line.strip().split(', ')
        # Append the fields to the data list as a tuple or list
        car_list.append(fields)
file.close()

CarRegistrationNo = 0
CarModel = 1
Passenger_capacity = 2
Availability = 3
YearOfManufacture = 4
CarManufacturer = 5
InsuranceExpiryDate = 6
InsurancePolicyNumber = 7
LastServiceDate = 8
RoadTaxExpiryDate = 9

# List to store rental transactions
rental_transactions = []
with open('Rental_Transactions.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split each line into fields using comma as the delimiter
        fields = line.strip().split(', ')
        # Append the fields to the data list as a tuple or list
        rental_transactions.append(fields)
file.close()

CarRegistrationNo = 0
CusID = 1
RentalDate = 2
ReturnDate = 3
RentalDays = 4
TotalRent = 5
PaymentStatus = 6

#Defining Manager page function
def Manager():
    print("\nWelcome to the Manager Dashboard\n")
    print("Functions: \nA. Register new staff/user \nB. Update staff/user profile \nC. Delete staff/user \nD. Update renting rate per day \nE. View monthly revenue report")
    choice = input("\nPlease select a function (A/B/C/D/E):")

    if choice.upper() == "A":
        new_user_list = []
        #Adding new staff/user information to the list
        new_user_list.append(input("Please enter the staff ID:"))
        new_user_list.append(input("Please enter the staff name:"))
        new_user_list.append(input("Please enter the password:"))
        new_user_list.append(input("Please enter the staff role:"))
        new_user_list.append(arrow.now().format('DD MMMM YYYY'))
        staff_data_list.append(new_user_list)
        print("Registration successful.")

    elif choice.upper() == "B":
        staffID = input("Please enter the Staff ID to be updated:")
        
        #Determining which user to be updated
        for sub_list in staff_data_list:
            if staffID in sub_list:
                update_index = staff_data_list.index(sub_list)
     
        print("1. Staff ID:",staff_data_list[update_index][StaffID], 
              "\n2. Staff Name:",staff_data_list[update_index][StaffName], 
              "\n3. Password:", staff_data_list[update_index][Password], 
              "\n4. Staff Roles:",staff_data_list[update_index][StaffRoles])
        
        #Determining which field to be updated
        update_choice = int(input("Please enter the field to be updated (1/2/3/4):")) -1
        if update_choice in range(0,5):
            staff_data_list[update_index][update_choice] = input("Please insert new value:")
            print("New value:",staff_data_list[update_index][update_choice])
        else: 
            print("No such field.")

    elif choice.upper() == "C":
        #Determine which staff id to delete
        deleteStaff = input("Please enter the Staff ID to be deleted:")
        #Determine the index of staff to be deleted
        for sub_list in staff_data_list:
            if deleteStaff in sub_list:
                delete_index = staff_data_list.index(sub_list)
        #Remove staff from list
        staff_data_list.pop(delete_index)
        print("User successfully deleted!")

    elif choice.upper() == "D":
        #Determine which type of car to update
        print("Which type of car renting rate would you like to update? (A/B)")
        typeOfCar = input("A. 5 seater \nB. 7 seater\n").upper()
        if typeOfCar == "A":
            #Updating new renting rate for 4 seater car
            renting_rate_list[0] = input("Please enter the new rate:")
            print("Data successfully updated!")
        elif typeOfCar == "B":
            #Updating new renting rate for 7 seater car
            renting_rate_list[1] = input("Please enter the new rate:")
            print("Data successfully updated!")
        else:
            print("Selection not available.")

    elif choice.upper() == "E":
        month = input("Please enter the month of monthly revenue report to be generated (Exp. April):")
        TotalMonthlyRevenue = 0
        report = open(f'{month}_Revenue_Report.txt', 'w')
        #Adding all transaction together to find total revenue
        for rental in range(1, len(rental_transactions)):
        #Check if customer has any transactions
            if month in rental_transactions[rental][RentalDate]:
                TotalMonthlyRevenue = TotalMonthlyRevenue + int(rental_transactions[rental][TotalRent])
                print(rental_transactions[rental])
                report.write("\n".join([', '.join(rental_transactions[rental])]))
                report.write("\n")
        report.close()
        #Writing all the transaction that occur in the month to text file
        report = open(f'{month}_Revenue_Report.txt', 'a')
        report.write(f"\nTotal Monthly Revenue: {str(TotalMonthlyRevenue)}")
        report.close()
        print("Total Monthly Revenue:", TotalMonthlyRevenue)

    else:
        print("Invalid option. Please enter 'A', 'B', 'C', 'D', 'E'.")

#Defining Customer Service Staff I page function
def CUSI():
    print("\nWelcome to the Customer Service Staff I System\n")
    print("System roles: ")
    print("1. Register a Customer")
    print("2. Update Customer Details")
    print("3. View Registered Customers")
    print("4. Update Own Profile")
    print("5. Delete customers with no rental transactions")

    role=input("\nEnter the number of the task that you want to perform (1/2/3/4/5). ").strip()

    # call the function based on what number the user typed in
    if role=="1":
        registerCustomer()
        
    elif role=="2":
        updateCustomerDetails()

    elif role=="3":
        viewCustomers()

    elif role=="4":
        updateCSSIProfile()

    elif role=="5":
        deleteCustomerData()

    else:
        print("Invalid input. Please enter (1/2/3/4/5).")

def registerCustomer():
    print("Please enter customer information.")
    name=input("Customer Name:")

    nationality=input("Nationality (Local/Foreign):")

    #To check whether customer is a local or a foreigner
    if nationality.lower()=="local":
        nric=str(input("Customer NRIC (example: 999999-99-9999):")) #if local, enter NRIC
        passportNo=None

    elif nationality.lower()=="foreign":
        passportNo=str(input("Customer Passport Number (example: PA1234567890X):")) #if foreign, enter passport number
        nric=None

    else:
        print("Invalid input. Please try again.")
        registerCustomer()

    drivingLicenseNo=str(input("Customer Card Driving License No (example: D12345678):"))
    address=str(input("Customer Contact Address (example:10, Main Street, 34000 Taiping, Perak, Malaysia):"))
    phoneNo=str(input("Customer Phone Number (example:05-8051234):"))

    # Get the current date
    registrationDate = datetime.now()
    # Format the current date into DD-MM-YYYY
    formattedDate = registrationDate.strftime("%d-%m-%Y")

    #set the generated customer id to the variable "gen_customerID"
    gen_customerID=generateCustomerID()
    #to make first letter of the value capitalize and the rest lowercase
    formattedNationality=nationality.capitalize()

    # Output of customer info
    print("\nHere is the following customer information:")
    print("\nCustomerID:", gen_customerID)
    print("Customer Name:", name)
    print("Customer NRIC:", nric)
    print("Customer Passport Number:", passportNo)
    print("Customer Card Driving License No:", drivingLicenseNo)
    print("Customer Contact Address:", address)
    print("Customer Phone Number:", phoneNo)
    print("Customer Registration Date:", formattedDate)
    print("Customer Nationality:", formattedNationality)

    # To confirm submission of customer data 
    confirmation=input("Submit? (YES/NO)")
    if confirmation.upper()=="YES":

        # Open text file in append mode
        with open("Customer_Data.txt", "a") as c:
            #add customer data to the file
            c.write(f"\n{gen_customerID}\t{name}\t{nric}\t{passportNo}\t{drivingLicenseNo}\t{address}\t{phoneNo}\t{formattedDate}\t{formattedNationality}" )

        print("\nThis customer has been successfully registered.")

    elif confirmation.upper()=="NO":
        print("Please try again")
        registerCustomer()

#Defining a function to count no of customers in the file
def countCustomers():
    # Initialize a set to store unique CustomerID values
    customer_ids = set()

    # Read the existing data from the file
    with open('Customer_Data.txt', "r") as c:
        # Skip the first line (header)
        next(c)
        for line in c:
            # Extract the CustomerID from each line and add it to the set
            customer_id = line.strip().split("\t")[0]  # Assuming CustomerID is the first field
            customer_ids.add(customer_id)
    # Return the number of unique CustomerID values
    return len(customer_ids)

customerCount=countCustomers()

# Defining a function to generate customerID
def generateCustomerID():
    global customerCount
    # to ensure numeric part of the customer id increments for each new customer
    customerCount =customerCount + 1
    #The :05d specifies that the number should be formatted to have at least five digits, with leading zeros if necessary.
    customer_id = f"C{customerCount:05d}"
    return customer_id

# Defining function for updating customer details
def updateCustomerDetails():
    id=str(input("CustomerID:"))
    updateloop="YES"

    # Read the data from the file
    with open('Customer_Data.txt', "r") as c:
        lines = c.readlines()

    # Flag to track if customer ID is found
    customer_found = False

    #loop for user to update customer details
    while updateloop.upper()=="YES":
        
        # Find the line corresponding to the customer ID
        for i, line in enumerate(lines):

            if line.startswith(id):
                customer_found = True
                # Split the line into parts based on tabs
                parts = line.strip().split("\t")

                print("\nHere are the following details that you can update.")
                print("\n1. Phone number")
                print("2. Address")
                print("3. Driving License No")
                print("4. Passport No (Foreigner Only)")
                updateNo=int(input("Enter the number of the details that you would like to update."))
                

                # update the data in the file according to number the user typed in
                if updateNo==1:
                    parts[6]=str(input("Phone number:"))

                elif updateNo==2:
                    parts[5]=str(input("Address:"))

                elif updateNo==3:
                    parts[4]=str(input("Driving License No:"))

                elif updateNo==4 and parts[8]=="Foreign":
                    parts[3]=str(input("Passport Number:"))

                else:
                    print("Invalid input. Please retry.")
                    continue

                # Reconstruct the line with updated details
                lines[i] = "\t".join(parts) + "\n" 

                # Write the updated data back to the file
                with open('Customer_Data.txt', "w") as c:
                    c.writelines(lines)
                print("Customer data updated successfully.")
                updateloop=input("Update other details? (YES/NO)")
                break
                
        # Check if customer ID was found        
        if not customer_found:
            print("Customer with ID" ,id, "not found.")
            break


# Defining function to view a list of registered customers
def viewCustomers():
    print("\nHere is the list of registered customers.\n")

    # Read the data from the file
    with open('Customer_Data.txt','r') as c:
        #output data in the file
        print(c.read())
    return

#defining function for updating own profile
def updateCSSIProfile():
    staffID = "LindaP"
    
    #Determining which user to be updated
    for sub_list in staff_data_list:
        if staffID in sub_list:
            update_index = staff_data_list.index(sub_list)

    print( "\n1. Staff Name:",staff_data_list[update_index][StaffName], 
        "\n2. Password:",staff_data_list[update_index][Password])
    
    #Determining which field to be updated
    update_choice = int(input("\nPlease enter the field to be updated (1/2):")) 
    if update_choice in range(1,3):
        staff_data_list[update_index][update_choice] = input("Please insert new value:")
        print("New value:",staff_data_list[update_index][update_choice])
    else: 
        print("No such field.")

                
def deleteCustomerData():
    # Read customer data from file, skipping the header
    with open("Customer_Data.txt", "r") as f:
        header = f.readline().strip()  # Read and skip the header line
        print(header)
        customers = [line.strip().split("\t") for line in f.readlines()]

    # Read rental data from file, skipping the header
    with open("Rental_Transactions.txt", "r") as f:
        rentals = [line.strip().split(", ") for line in f.readlines()]

    # Find customers with no rental transactions
    customers_to_delete = []
    for customer in customers:
        has_rental = False
        for rental in rentals:
            if rental[1] == customer[0]:
                has_rental = True
                break
        if not has_rental:
            customers_to_delete.append(customer)

    if customers_to_delete:
        print("Customers with no rental transactions recorded:")
        for customer in customers_to_delete:
            print("\t".join(customer))  # Print customer data that can be deleted

        # Prompt user to input CustomerID of customer to delete
        customer_id = input("\nEnter the CustomerID of the customer you want to delete (or type 'exit' to cancel): ")
        if customer_id.lower() == 'exit':
            return
        else:
            customer_id = customer_id.upper()
            # Write updated customer data back to file, excluding the deleted customer
            with open("Customer_Data.txt", "w") as f:
                f.write(header)  # Rewrite the header line
                for customer in customers:
                    if customer[0] != customer_id:
                        f.write("\n"+"\t".join(customer))
                print(f"Customer with CustomerID {customer_id} has been deleted.")

    else:
        print("All customers have rental transactions recorded. No customers to delete.")

# Defining Customer Service II page
def CUSII():
    print("\nWelcome to the Customer Service II!")
    print("\n1. Check Available Car")
    print("2. Record Rental Details")
    print("3. Generate Bill")
    print("4. View Rental Transactions")
    print("5. Return Car")
    print("6. Delete Rental Transactions")

    action = input("\nEnter your choice (1/2/3/4/5/6): ")

    if action == '1':
        check_available_car()
    elif action == '2':
        rental_details()
    elif action == '3':
        generate_bill()
    elif action == '4':
        date = input("Enter the date (DD MMMM YYYY) to view rental transaction: ")
        #date = datetime.strptime(date_str, '%d %B %Y')
        view_rental_transaction(date)
    elif action == '5':
        return_car()
    elif action == '6':
        delete_rental_transactions()
    else:
        print("Invalid option. Please enter '1', '2', '3', '4', '5', '6'.")

# Get request from customer and check the car status
def check_available_car():
    passenger_count = int(input("Enter number of passengers: "))
    status = 0
    for i in range(1,len(car_list)):
        if int(car_list[i][Passenger_capacity]) >= passenger_count and car_list[i][Availability] == "Available":
            print(car_list[i][CarRegistrationNo],"\t", 
                  car_list[i][CarModel], 
                  "\tPassenger capacity:", car_list[i][Passenger_capacity], 
                  "\tStatus:", car_list[i][Availability])
            status = 1
    if status == 0:
        print("There are no cars available now.")

# Accept and record rental details from customers
def rental_details():
    print("\n-- Rental Details --")
    registration_number = input("Enter the Registration Number: ").upper()
    customer_id_input = input("Enter Customer ID: ").upper()
    rental_date = input("Enter rental date (DD MMMM YYYY): ")
    return_date = input("Enter return date (DD MMMM YYYY): ")
    status = 0
    for sub_list in car_list:
        if registration_number in sub_list:
            car_index = car_list.index(sub_list)
            status = 1
    if status == 0:
        print("There is no such car. Please enter the correct registration number.")
        return

    #Check and see if the car is available for rent
    if car_list[car_index][Availability] == "Available":
        rental_periods = (datetime.strptime(return_date, '%d %B %Y') - datetime.strptime(rental_date, '%d %B %Y')).days + 1
        if car_list[car_index][Passenger_capacity] == 5:
            total_rental = rental_periods * int(renting_rate_list[0])
        else:
            total_rental = rental_periods * int(renting_rate_list[1])

        #Change status of car availability
        car_list[car_index][Availability] = "Reserved"

        #Add rental data to transaction list
        rental_data = [registration_number, customer_id_input, rental_date, return_date, rental_periods, total_rental, "not paid"]
        rental_transactions.append(rental_data)
        print(f"Rental Periods: {rental_periods} days")
        print(f"Total Rental: RM {total_rental}")
        print("Rental transaction successful.")
        return rental_data
    
    else:
        print("This car is not available for rent.")

#Generating bill according to customer
def generate_bill():
    cus_bill = input("Please enter Customer ID:").upper()
    billnum = 0
    total_rental = 0

    for sub_list in rental_transactions:
        #Check if customer has any transactions
        if cus_bill in sub_list:
            bill_index = rental_transactions.index(sub_list)
            if rental_transactions[bill_index][PaymentStatus] == "not paid":
                print("\n--- Bill ---")
                print(f"Car Registration Number: {rental_transactions[bill_index][CarRegistrationNo]}")
                print(f"Customer ID: {rental_transactions[bill_index][CusID]}")
                print(f"Rental Date: {rental_transactions[bill_index][RentalDate]}")
                print(f"Return Date: {rental_transactions[bill_index][ReturnDate]}")
                print(f"Rental Periods (Days): {rental_transactions[bill_index][RentalDays]}")
                print(f"Total Rental: RM{float(rental_transactions[bill_index][TotalRent]):.2f}")
                print(f"Payment Status: {rental_transactions[bill_index][PaymentStatus]}")
                total_rental = total_rental + float(rental_transactions[bill_index][TotalRent])
                billnum = billnum + 1

    #If customer has no transactions
    if billnum == 0:
        print("No rental data available.")
    else:
        payment = input("Do you want to proceed to payment? (Y/N)")
        #Proceed to payment section
        if payment.upper() == "Y":
            print(f"Total rental: RM{total_rental:.2f}")
            payment_amount = float(input("Enter payment amount: RM "))

            if payment_amount >= total_rental:
                change = payment_amount - total_rental
                print(f"Change: RM {change:.2f}")

                #Updating the availability of car
                for sub_list in rental_transactions:
                    if cus_bill in sub_list:
                        payment_index = rental_transactions.index(sub_list) 
                        car_register = rental_transactions[payment_index][CarRegistrationNo]
                        rental_transactions[payment_index][PaymentStatus] = "Paid"
                        for sub_list in car_list:
                            if car_register in sub_list:
                                car_index = car_list.index(sub_list) 
                                car_list[car_index][Availability] = "Rented"

                print("Payment successful.")   
                generate_receipt(cus_bill)

            else:
                print("Insufficient payment amount.")

#Generating receipt for cuetomer who has paid
def generate_receipt(cus_bill):

    for sub_list in rental_transactions:
        #Check if customer has any transactions
        if cus_bill in sub_list:
            bill_index = rental_transactions.index(sub_list)
            print("\n---- Receipt ----")
            print(f"Car Registration Number: {rental_transactions[bill_index][CarRegistrationNo]}")
            print(f"Customer ID: {rental_transactions[bill_index][CusID]}")
            print(f"Rental Date: {rental_transactions[bill_index][RentalDate]}")
            print(f"Return Date: {rental_transactions[bill_index][ReturnDate]}")
            print(f"Rental Periods (Days): {rental_transactions[bill_index][RentalDays]}")
            print(f"Total Rental: RM{float(rental_transactions[bill_index][TotalRent]):.2f}")
            print(f"Payment Status: {rental_transactions[bill_index][PaymentStatus]}")

#View rental transaction based on the date given
def view_rental_transaction(date):
    print(f"\n--- Rental Transaction on {date} ---")
    for rental in range(1, len(rental_transactions)):
        if rental_transactions[rental][2] == date:
            print(f"Car Registration Number: {rental_transactions[rental][CarRegistrationNo]}")
            print(f"Customer ID: {rental_transactions[rental][CusID]}")
            print(f"Rental Date: {rental_transactions[rental][RentalDate]}")
            print(f"Return Date: {rental_transactions[rental][ReturnDate]}")
            print(f"Rental Periods (Days): {rental_transactions[rental][RentalDays]}")
            print(f"Total Rental: RM{float(rental_transactions[rental][TotalRent]):.2f}")
            print(f"Payment Status: {rental_transactions[rental][PaymentStatus]}")
            print("------------------------")

#Defining a function to carry out the process of car returning
def return_car():
    registration_number = input("Enter the Registration Number of the car to return: ").upper()
    for sub_list in car_list:
        if registration_number.upper() in sub_list:
            return_index = car_list.index(sub_list)
    #update the availability status of a car
    if car_list[return_index][Availability] == "Rented" or car_list[return_index][Availability] == "Reserved":
        car_list[return_index][Availability] = "Available"
        print("Car returned successfully.")
    else:
        print("Invalid car registration number or the car is not rented.")

#Defining a function to delete transactions
def delete_rental_transactions():
    cus_del_trans = input("Please enter Customer ID:").upper()
    status = 0
    for sub_list in rental_transactions:
        if cus_del_trans in sub_list:
            date = input("Enter the rental date (DD MMMM YYYY) of transaction to be removed: ")
            status = 1
            for sub_list in rental_transactions:
                if cus_del_trans in sub_list:
                    del_index = rental_transactions.index(sub_list) 
                    if rental_transactions[del_index][RentalDate] == date:
                        rental_transactions.pop(del_index)
                        print("Transaction successfully deleted.")
                        status = 2

    if status == 0:
        print(f"Customer ID {cus_del_trans} does not exist.")
    elif status == 1:
        print("There are no transactions to be deleted.")

#Defining CarServiceStaff page function
def CARS():
    print("\nWelcome to the Car Service Dashboard\n")

    print("Select your action: \nA. View Car Details ONLY\nB. Register a New Car\nC. Update Existing Car Information \nD. Update own profile")
    validAns = input("Please select a function by typing (A/B/C):").upper().strip()

    #Function A - View Only for Availability status
    if validAns == "A":
        print("\nThese are the Car Models and their Car Registration Number.\n")
        for car in range(1, len(car_list)):
            print(car_list[car][CarRegistrationNo] + " " + car_list[car][CarModel])

        carplate = input("\nEnter the Car Registration Number accurately to check Availability:").upper().strip()
        status = ""
        for sub_list in car_list:
            if carplate in sub_list:
                carplate_index = car_list.index(sub_list)
                status = True
                print("\n" +car_list[carplate_index][CarRegistrationNo] + " " + car_list[carplate_index][CarModel] + "\nStatus: " + car_list[carplate_index][Availability])
                print("\nRental Date \tReturn Date")

        for sub_list in rental_transactions:
            if carplate in sub_list:
                carplate_index = rental_transactions.index(sub_list)
                print(f"{rental_transactions[carplate_index][RentalDate]} \t{rental_transactions[carplate_index][ReturnDate]}")
        
        if status == "":
            print("Invalid carplate.")

    #Function B - Register a new Car
    elif validAns == "B":
        new_car = []
        print("\nPlease key in the following details: \n")
        CarRegNo = input("Car Registration Number: ").upper()
        new_car.append(CarRegNo)
        CarMod = input("Car Model: ")
        new_car.append(CarMod)
        SeatCap = input("Seating Capacity: ")
        new_car.append(SeatCap)
        CarAVB = input("Car Availability:\n 1. Available\n 2. Reserved\n 3. Rented\n 4. Under Service\nEnter (1/2/3/4) to Select:")
        if CarAVB == "1":
            new_car.append("Available")
        elif CarAVB == "2":
            new_car.append("Reserved")
        elif CarAVB == "3":
            new_car.append("Rented")
        elif CarAVB == "4":
            new_car.append("UnderService")
        else:
            print("Invalid input.")

        YrOfManu = input("Year of Manufacture (DD-MM-YYYY): ")
        new_car.append(YrOfManu)
        CarManu = input("Car Manufacturer: ")
        new_car.append(CarManu)
        InsurExpDate = input("Insure Expiry Date (DD-MM-YYYY): ")
        new_car.append(InsurExpDate)
        InsurPolicyNo = input("Insurance Policy Number: ")
        new_car.append(InsurPolicyNo)
        LastServ = input("Last Service Date (DD-MM-YYYY):")
        new_car.append(LastServ)
        RoadTaxExpDate = input("Road Tax Expiry Date (DD-MM-YYYY):")
        new_car.append(RoadTaxExpDate)

        car_list.append(new_car)
        
    #Displaying information of the recently added car
        print("\n\nThe new vehicles information has been successfully added to the list. \n" +
                "\nCar Registration Number: " + car_list[-1][CarRegistrationNo] +"\n"+
                "Car Model: " + car_list[-1][CarModel] +"\n"+
                "Seating Capacity: " + car_list[-1][Passenger_capacity] +"\n"+
                "Car Availability: " + car_list[-1][Availability] +"\n"+
                "Year of Manufacture: " + car_list[-1][YearOfManufacture] +"\n"+
                "Car Manufacturer: " + car_list[-1][CarManufacturer] +"\n"+
                "Insurance Expiry Date: " + car_list[-1][InsuranceExpiryDate] +"\n"+
                "Insure Policy Number: " + car_list[-1][InsurancePolicyNumber] +"\n"+
                "Last Service Date: " + car_list[-1][LastServiceDate] +"\n"+
                "Road Tax Expiry Date: " + car_list[-1][RoadTaxExpiryDate])

    #Function C - Update the information of an existing Car
    elif validAns == "C":
        print("\nThese are the Car Models and their Car Registration Number.\n")
        for car in range(1, len(car_list)):
            print(car_list[car][CarRegistrationNo] + " " + car_list[car][CarModel])

        carplate = input("Please enter the carplate of the car to make changes: ").upper().strip()
        status = ""

        for sub_list in car_list:
            if carplate in sub_list:
                carplate_index = car_list.index(sub_list)
                status = True

        if status == "":
            print("Invalid carplate.")

        # To show user the current state of car information
        def status():
            print("\nThis is the current state of " + carplate + "'s information:")
            print(f"1. Insurance Policy Number: {car_list[carplate_index][InsurancePolicyNumber]}")
            print(f"2. Insurance Expiry Date: {car_list[carplate_index][InsuranceExpiryDate]}")
            print(f"3. Road Tax Expiry Date: {car_list[carplate_index][RoadTaxExpiryDate]}")
            print("4. Car Renting Rate per Day: ", end = "")
            if car_list[carplate_index][Passenger_capacity] == "5":
                print(renting_rate_list[0])
            else:
                print(renting_rate_list[1])
            print(f"5. Rental Availability: {car_list[carplate_index][Availability]}")
            
            
        #A while loop for users to continue updating data of the same carc
        done = "A"
        while done == "A":
            print("\nThis is the current state of " + carplate + "'s information:")
            print(f"1. Insurance Policy Number: {car_list[carplate_index][InsurancePolicyNumber]}")
            print(f"2. Insurance Expiry Date: {car_list[carplate_index][InsuranceExpiryDate]}")
            print(f"3. Road Tax Expiry Date: {car_list[carplate_index][RoadTaxExpiryDate]}")
            print("4. Car Renting Rate per Day: ", end = "")
            if car_list[carplate_index][Passenger_capacity] == "5":
                print(renting_rate_list[0])
                RentingRate = 0
            else:
                print(renting_rate_list[1])
                RentingRate = 1
            print(f"5. Rental Availability: {car_list[carplate_index][Availability]}")

            edit = input("Type 1/2/3/4/5 to select the information you wish to edit: ")
            if edit == "1":
                car_list[carplate_index][InsurancePolicyNumber] = input("Insurance Policy Number: ")
                status()

            elif edit == "2":
                car_list[carplate_index][InsuranceExpiryDate] = input("Insurance Expiry Date (DD MMMM YYYY): ")
                status()

            elif edit == "3":
                car_list[carplate_index][RoadTaxExpiryDate] = input("Road Tax Expiry Date (DD MMMM YYYY): ")
                status()

            elif edit == "4":
                renting_rate_list[RentingRate] = input("Car Renting Rate per Day: ")
                status()

            elif edit == "5":
                CarAVB = input("Car Availability:\n 1. Available\n 2. Reserved\n 3. Rented\n 4. Under Service\n 5. Disposed\nEnter (1/2/3/4/5) to Select:")

                if CarAVB == "1":
                    car_list[carplate_index][Availability] = "Available"
                    status()

                elif CarAVB == "2":
                    car_list[carplate_index][Availability] = "Reserved"
                    status()

                elif CarAVB == "3":
                    car_list[carplate_index][Availability] = "Rented"
                    status()

                elif CarAVB == "4":
                    car_list[carplate_index][Availability] = "UnderService"
                    status()

                elif CarAVB == "5":
                    car_list[carplate_index][Availability] = "Disposed"
                    print("This car " + carplate + " is labeled as DISPOSED so it will be deleted automatically.")
                    car_list.pop(carplate_index)

                    print("This car's information is permanently deleted.")
                    break

                else:
                    print("Invalid input.")
                
            else:
                print("Invalid input.")
                break

            done = input("\nDo you still wish to edit any other information of this car?\nA. Yes\nB. No \nType A or B to Select:").upper().strip()

        else:
            print("Changes are successfully made.")

    elif validAns == "D":
        staffID = "MarcusC"
    
        #Determining which user to be updated
        for sub_list in staff_data_list:
            if staffID in sub_list:
                update_index = staff_data_list.index(sub_list)
    
        print( "\n1. Staff Name:",staff_data_list[update_index][StaffName], 
            "\n2. Password:",staff_data_list[update_index][Password])
        
        #Determining which field to be updated
        update_choice = int(input("\nPlease enter the field to be updated (1/2):")) 
        if update_choice in range(0,3):
            staff_data_list[update_index][update_choice] = input("Please insert new value:")
            print("New value:",staff_data_list[update_index][update_choice])
        else: 
            print("No such field.")

    else:
        print("Please key in a valid function by typing (A/B/C/D).")


#Header of system
print("Welcome to Langkawi Island Car Rental System")
status = ""

#Limit the number of login to 3 times
for i in range(0,3,1):
    #Get username and password from user
    username = input("Username:")
    password = input("Password:")
    
    #Check if username is valid or not
    for sub_list in staff_data_list:
        while username in sub_list:
            index = staff_data_list.index(sub_list)
            
            for j in range(0,2,1):
                
                #Check if password is correct
                if password == staff_data_list[index][Password]:
                    print("Login Successful.")
                    answer = "Y"
                    
                    while answer.upper() == "Y":
                        #Identify the role of the user
                        if staff_data_list[index][StaffRoles] == "MANAGER": 
                            Manager()
                        elif staff_data_list[index][StaffRoles] == "CUSI":
                            CUSI()
                        elif staff_data_list[index][StaffRoles] == "CUSII":
                            CUSII()
                        elif staff_data_list[index][StaffRoles] == "CARS":
                            CARS()
                        else:
                            print("Sorry, you are not allowed to access this system.")
                        
                        answer = input("\nDo you still want to continue? (Y/N)")

                    else:
                        #Update data in text file
                        file = open('Staff_Data.txt', 'w')
                        file.write("\n".join([', '.join(map(str, item)) for item in staff_data_list]))
                        file.close()

                        file = open('CarRentingRate.txt', 'w')
                        for items in renting_rate_list:
                            file.write(items+"\n")
                        file.close()

                        file = open('Rental_Transactions.txt', 'w')
                        file.write("\n".join([', '.join(map(str, item)) for item in rental_transactions]))
                        file.close()

                        file = open('Car_Details.txt', 'w')
                        file.write("\n".join([', '.join(map(str, item)) for item in car_list]))
                        file.close()

                        status = True
                        break
                else:
                    status = True
                    print("Wrong Password. Try again!")
                    password = input("Password:")
                    
            break

        if status == "" or status == False:
            status = False
        else:
            status = True

    if status == False:
        print("Username does not exist.")
    else:
        break