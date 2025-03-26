import random

# Title
game_title = "\033[1m🎮Number Guessing Game🎲\033[0m"
print(game_title)

# Intro
game_introduction = "A game, where you'll get few attempts to guess a number between 0 to 100. Are you ready? Let's get started! 🚀\n"
print(game_introduction)

# How to Play
how_to_play = """\n\033[1m📖 How to Play: -\033[0m 
1. \033[1m🎯 Guess the number:\033[0m The game will ask you to guess a number between 0 and 100.
2. \033[1m💡 Get hints:\033[0m After each guess, the game will tell you if your guess was too high or too low.
3. \033[1m⏳ Limited attempts:\033[0m You have a total of 5 attempts to guess the correct number.
4. \033[1m🏆 Win or Lose:\033[0m If you guess the number within 5 attempts, you win! Otherwise, you lose, and the game will reveal the secret number."""

# Menu
menu = """\n\033[1m🎮 Game Menu: -\033[0m
1. 🎲 Start Game
2. 📖 How to Play
3. 🏆 View High Scores
4. 🚪 Exit
"""
print(menu)

# Game Logic
def Game():
    random_number = random.randint(1, 101)
    # print(random_number)

    attempts = 5

    print("\n\033[1m\033[3m🎮 Game has started!\033[0m\033[0m\n")

    guess = int(input("Guess the number: "))

    while guess != random_number and attempts > 0:
        
        if guess > random_number:
            print(f"📈 Too High! Try Again, You've {attempts} attempt left.")

        elif guess < random_number:
            print(f"📉 Too Low! Try Again, You've {attempts} attempt left.")

        guess = int(input("\nGuess the number: "))
        attempts -= 1
    
    if guess == random_number:
        print(f"\n🎉 Congrats! You won 🏆, You guessed \033[1m{guess}\033[0m correctly in \033[1m{attempts}\033[0m attempts!")
        print("Thanks for playing! Goodbye 👋")

    elif guess != random_number:
        print(f"😢 You lost!, The number was {random_number}")
        chance = input("🔄 Wanna try Again? (Y/N): ")

        if chance == "Y" or chance == "y":
            Game()
        elif chance == "N" or chance == "n":
            print("Thanks for playing! Goodbye 👋")
        else:
            print("Invalid Input")


# Navigation
navigation = int(input("Navigate: "))

while navigation != "4":
    if navigation == 1:
        Game()
        break
    elif navigation == 2:
        print(how_to_play)
    elif navigation == 3:
        print("\nHigh Score feature will be added soon.")
    elif navigation == 4:
        exit()
    else:
        print("Invalid Input")
    
    print(menu)
    navigation = int(input("Navigate: "))