"""Voter registration application"""
import sys

valid_binary_entries = ["yes", "no"]
states = ["AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "GU", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME",
          "MI", "MN", "MO", "MP", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM",
          "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX",
          "UM", "UT", "VA", "VI", "VT", "WA", "WI", "WV", "WY"]


def exit_application(message: str):
    """Method to print out an exit message then exits the application"""
    if message:
        print(message)

    sys.exit()


def invalid_entry():
    """Method to print out message to let user know only 'yes' or 'no' values are allowed"""
    print("Please only enter a \'yes\' or a \'no\'")


def continue_application(message):
    """Method that prompts the user to continue the application or quit"""
    continue_app = input("Do you want to continue with the application? "
                         "\nEnter \'yes\' or \'no\': ")
    while not continue_app.isalpha() or not continue_app.lower() in valid_binary_entries:
        invalid_entry()
        continue_app = input("Do you want to continue with Voter Registration? ")

    if continue_app.lower() == "no":
        exit_application(message)


def registration_application():
    """Method that receives user input for registration application with data validation"""
    first_name = input("What is your first name? ")
    while not first_name:
        first_name = input("What is your first name? ")

    continue_application("Have a good day. Goodbye!")

    last_name = input("What is your last name? ")
    while not last_name:
        last_name = input("What is your last name? ")

    continue_application("Have a good day. Goodbye!")

    age = input("How old are you? ")
    while not age.isdigit():
        age = input("Please only enter a valid value for your age: ")

    if int(age) < 18:
        exit_application("Sorry, you must be 18 years or older to vote.")

    continue_application("Have a good day. Goodbye!")

    citizenship = input("Are you a U.S. Citizen? \nEnter \'yes\' or \'no\': ")
    while not citizenship.isalpha() or not citizenship.lower() in valid_binary_entries:
        invalid_entry()
        citizenship = input("Are you a U.S. Citizen? \nEnter \'yes\' or \'no\': ")

    if citizenship.lower() == 'no':
        exit_application("Sorry, you must be a U.S. citizen to register to vote. Goodbye.")

    continue_application("Have a good day. Goodbye!")

    state = input("What is your state of residence? "
                  "\nEnter 2 letters representing the abbreviation. (Ex: \'MD\' for Maryland): ")
    while not state.isalpha() or len(state) != 2 or not state.upper() in states:
        state = input("Please enter a valid U.S. state of residence: ")

    continue_application("Have a good day. Goodbye!")

    zipcode = input("Enter your zipcode: ")
    while not zipcode.isnumeric() or not len(zipcode) == 5:
        state = input("Please enter a valid zipcode: ")

    print(
        "\nThank you for registering to vote, here is the information you entered:",
        "\nFirst name: ", first_name,
        "\nLast name: ", last_name,
        "\nAge: ", age,
        "\nU.S. Citizen: ", citizenship,
        "\nState of residence: ", state.upper(),
        "\nZipcode: ", zipcode,
        "\n\nCongratulations you are eligible to vote."
    )


# Start application
print("Welcome to the Python Voter Registration Application.")
continue_application("Have a good day. Goodbye!")
registration_application()
