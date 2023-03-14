# Main routine more efficient than v2


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here...

rounds_played = 0
choose_instrution = "Please choose rock (r), paper (p) or scissors"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "" :
        heading = "Continous Mode: " \
                  "Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of " \
                   "{}".format(rounds_played )
