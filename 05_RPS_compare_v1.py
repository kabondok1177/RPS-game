# RPS Component 3 - Compare user choice and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare options
        if user_choice == comp_choice:
            result = "tie"
        else:
            result = "not tie"

        print(f"({comp_choice} vs {user_choice}: {result}")

    comp_index += 1
    print()