# --------------------- PROJECT : RAILWAY TICKET BOOKING -----------------------
import random
class Train():
    def __init__(self, train_num, source, destination, seats,):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.seats = seats


    def display_info(self):
        print(f"Train number: {self.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Available seats: {self.seats}")
        print()  # line break for each train information is displayed


    def book_tickets(self, num_tickets):
        if num_tickets > self.seats:
            return None
        else:
            pnr_list = []
            for i in range(num_tickets):
                pnr_list.append(random.randint(100000, 999999))
            self.seats -= num_tickets
            return pnr_list



class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone Number: {self.phone}")


class Ticket:
    def __init__(self, train, source, destination, passengers, pnr):
        self.train = train
        self.source = source
        self.destination = destination
        self.passengers = passengers
        self.pnr = pnr

    def display_info(self):
        print(f"Train Number: {self.train.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"PNR: {self.pnr}")
        for passenger in self.passengers:
            passenger.display_info()
        print()

class Account:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password



accounts = [
    Account("user1", "password1"),
    Account("user2", "password2")
]


logged_in_account = None

while True:  
    print("\n1. Create an account\n2. Login\n")
    choice = input("Enter choice: ")
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        accounts.append(Account(username, password))

        print("Account created successfully!")

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        for account in accounts:
            if account.username == username and account.check_password(password):
                logged_in_account = account
                break
        if logged_in_account is None:
            print("Invalid username or password.")

        else:
            print(
                f"\nLogged in as {logged_in_account.username}\n\n-----Availabe Train details-----\n")

            break
    else:
        print("Invalid choice.")

if logged_in_account is not None:
    trains = [
        Train("12737", "Tadepalligudem", "Secunderabad", 40),
        Train("12728", "Tadepalligudem", "Visakhapatnam", 50),
        Train("22863", "Vijayawada", "Bangalore", 1),
        
    ]


# Display available trains
for train in trains:
    train.display_info()


# Get user input for booking
while True:
    try:
        train_num = input("Enter Train Number: ")
        num_tickets = int(input("Enter Number of Tickets: "))
        if num_tickets <= 0:
            raise ValueError("Number of tickets should be greater than 0")
        for train in trains:
            if train.train_num == train_num:
                if num_tickets > train.seats:
                    raise ValueError(
                        "Selected more tickets than available seats")  # If the number of tickets entered is more than the available seats, it will raise a ValueError with the message "Selected more tickets than available seats".
                break
        else:
            raise ValueError("Invalid Train Number.")
        break
    except ValueError as e:
        print(f"Invalid Input: {e}")
# The program asks the user to enter the train number and the number of tickets they want to book.

train = None
for t in trains:
    if t.train_num == train_num:
        train = t
        break
# The program then searches for the Train object with the corresponding train number entered by the user.

if train is None:
    print("Invalid Train Number.")
# If the train number is invalid, the program prints "Invalid Train Number." and exits.

else:
    passengers = []
    for i in range(num_tickets):
        print(f"\nEnter details for Passenger {i + 1}:")
        while True:
            try:
                name = input("Name: ")
                if not name:
                    raise ValueError("Name cannot be empty")
                age = int(input("Age: "))
                if age <= 0 or age > 120:
                    raise ValueError("Invalid Age")
                gender = input("Gender: ")
                phone = input("Phone Number: ")
                if not phone or len(phone) != 10 or not phone.isdigit():
                    raise ValueError("Invalid Phone Number")
                passenger = Passenger(name, age, gender, phone)
                passengers.append(passenger)
                break
            except ValueError as e:
                print(f"Invalid Input: {e}")

    pnr_list = train.book_tickets(num_tickets)
    if pnr_list is None:
        print("Tickets not available.")

    else:
        print("\n--------------Booking Successful!------------\n\nYour Ticket Details: \n")

        for i in range(num_tickets):
            ticket = Ticket(train, train.source, train.destination, [
                            passengers[i]], pnr_list[i])
            ticket.display_info()
            print("\n--------Thank You------- \n-------Safe Journey------")



# -------- FINISHED--------
