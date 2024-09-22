import random

print("~~~Welcome to RPS~~~")

user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name here: ")

print("""
1. Paper vs Rock --> Paper
2. Rock vs Scissors --> Rock
3. Scissors vs Paper --> Scissors
""")

print("""
Choices are:
1. Rock
2. Paper
3. Scissors
""")

while True:
    # Get user's choice
    choice = int(input("Enter your choice (1-3): "))
    
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice (1-3): "))
    
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"
    
    print("The user's choice is:", user_choice)
    
    # Computer's random choice
    computer = random.randint(1, 3)
    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    
    print("The computer's choice is:", comp_choice)
    
    # Determine the winner
    if user_choice == comp_choice:
        print("It's a tie!")
        result = "Tie"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        print("User wins this round!")
        result = user_choice
    else:
        print("Computer wins this round!")
        result = comp_choice
    
    # Update scores
    if result == "Tie":
        ties += 1
    elif result == user_choice:
        user_score += 1
    else:
        comp_score += 1
    
    # Display scores
    print(f"\n{name}'s score: {user_score}")
    print(f"Computer's score: {comp_score}")
    print(f"Ties: {ties}\n")
    
    # Ask if the user wants to play again
    repeat = input("Do you want to play again? (Yes/No): ").strip().lower()
    
    if repeat == "no":
        print("Game over. Thanks for playing!")
        break
