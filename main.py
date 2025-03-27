import random
import time

# Title
game_title = "\033[1m🎮 Number Guessing Game🎲\033[0m\n"
print(game_title)

# GameInfo
GameInfo: dict = {"👨‍💻 Developer": "Abdul Rehman Jiwani", "📌 Version":"0.0.2"}

# Name
name =  input("Enter your name: ")

# How to Play
how_to_play = """\n\033[1m📖 How to Play: -\033[0m 
1. \033[1m🎯 Guess the number:\033[0m The game will ask you to guess a number according to your choosen range.
2. \033[1m💡 Get hints:\033[0m After each guess, the game will tell you if your guess was too high or too low.
3. \033[1m⏳ Limited attempts:\033[0m You have a total of 5 attempts to guess the correct number.
4. \033[1m🏆 Win or Lose:\033[0m If you guess the number within no. of attempts, you win! Otherwise, you lose, and the game will reveal the secret number.
5. \033[1m🏆 Levels:\033[0m There are three different levels.
                    i. Easy: You've to guess a number between 1 to 100 within 5 attempts.
                    ii. Medium: You've to guess a number between 21 to 50 within 3 attempts.
                    iii. Hard: You've to guess a number between 1 to 10 within 2 attempts."""

# Menu
menu = """\n\033[1m🎮 Game Menu: -\033[0m
1. 🎲 Start Game
2. 📖 How to Play
3. 🏆 View High Scores
4. ℹ️ Game Info
5. 🚪 Exit
"""
print(menu)

# Game Logic
def Game():
    random_number = random.randint(1, 100)
    attempts = 5

    # Level Functionality starts...
    print("""\n🎯 Choose a Level:
1. 🟢 Easy
2. 🟡 Medium
3. 🔴 Hard""")
    
    Level = str(input("\n🎮 Select any (E/M/H): "))
    
    # Easy Level
    if Level == "E" or Level == "e":
        game_level = "Easy"
        print(f"\nPlayer {name}, you selected the {game_level} level. Now, Guess a number between 1 to 100 in {attempts} attempts. Are you ready {name}? Let's get started! 🚀")

    # Medium Level
    elif Level == "M" or Level == "m":
        game_level = "Medium"
        random_number = random.randint(21, 50)
        attempts = 3
        print(f"\nPlayer {name}, you selected the {game_level} level. Now, Guess a number between 21 to 50 in {attempts} attempts. Are you ready {name}? Let's get started! 🚀")

    # Hard Level
    elif Level == "H" or Level == "h":
        game_level = "Hard"
        random_number = random.randint(1, 10)
        attempts = 2
        print(f"\nPlayer {name}, you selected the {game_level} level. Now, Guess a number between 1 to 10 in {attempts} attempts. Are you ready {name}? Let's get started! 🚀")
    
    else:
        print("Invalid Input")
    
    # Game Functionality stars....
    print(f"\n\033[1m\033[3m🎮 Game has started at its {game_level} Level!\033[0m\033[0m\n")

    guess = int(input("Guess the number: "))
    attempts -= 1
    while guess != random_number and attempts > 0:
        if guess > random_number:
            print(f"📈 Too High! Try Again, You've {attempts} attempt left.")

        elif guess < random_number:
            print(f"📉 Too Low! Try Again, You've {attempts} attempt left.")

        attempts -= 1
        guess = int(input("\nGuess the number: "))
    
    if guess == random_number:
        print(f"\n🎉 Congrats! You won 🏆, You guessed \033[1m{guess}\033[0m correctly in \033[1m{attempts}\033[0m attempt")
        print(f"👋 Thanks for playing! Goodbye {name}!")

    elif guess != random_number:
        print(f"😢 You lost! The number was {random_number}")
        chance = input("🔄 Wanna try Again? (Y/N): ")

        if chance == "Y" or chance == "y":
            Game()
        elif chance == "N" or chance == "n":
            print(f"Thanks for playing! Goodbye {name} 👋")
        else:
            print("Invalid Input")


# Navigation
navigation = int(input("Navigate: "))

while navigation != "5":
    if navigation == 1:
        Game()
        break
    elif navigation == 2:
        print(how_to_play)
        read = input("Done Reading it? (Y/N): ")
        if read == "Y" or read == "y":
            print("Redirecting to Game Menu...")
            time.sleep(0.5)
        elif read == "N" or read == "n":
            print("Ok waiting....")
            time.sleep(5.0)
    elif navigation == 3:
        print("\nHigh Score feature will be added soon.")
        print("Redirecting to Game Menu...")
    elif navigation == 4:
        print(GameInfo)
    elif navigation == 5:
        exit()
    else:
        print("Invalid Input")
    
    print(menu)
    navigation = int(input("Navigate: "))