# Functions go here
def choice_checker(question, error):
    valid = False
    while not valid:

        # Ask user for choice (amd put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return "rock"
        elif response == "p" or response == "paper":
            return "paper"
        elif response == "s" or response == "scissors":
            return "scissor"

        # check for exit code...
        elif response == "xxx":
            return 'xxx'
        else:
            print(error)


# Main routine goes here

# Loop for testing purpose
user_choice = ""
while user_choice != "xxx":
    print()
    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s):",
                                 "Please enter rock / paper / scissors")

    print(f'You chose {user_choice}')

# Print out choice for comparison purposes
print("You chose {}".format(user_choice))
