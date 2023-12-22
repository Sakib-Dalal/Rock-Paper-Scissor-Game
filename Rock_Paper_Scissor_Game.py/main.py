import random
user_input = int(input("What do you choose? Type 0 to Rock 🪨, 1 for Paper 📄 or 2 for Scissors ✂️. \n➡️"))
num = random.randint(0, 2)

rock = 0
paper = 1
scissors = 2

# computer

if user_input >= 3:
    print("--Invalid input ☠️--")
elif num == rock:
    print("Computer Chose: Rock 🪨")
elif num == paper:
    print("Computer Chose: Paper 📄")
elif num == scissors:
    print("Computer Chose: Scissors ✂️")


# user
if user_input == rock:
    print("Use Chose: Rock 🪨\n")
elif user_input == paper:
    print("Use Chose: Paper 📄\n")
elif user_input == scissors:
    print("Use Chose: Scissors ✂️\n")

# algorithm
if num == user_input < 3:
    print("--Draw 🙅‍--")

if num == 0 and user_input == 2:
    print("--Computer 💻 Win 🎉--")

elif num == 2 and user_input == 0:
    print("--User 😎 Win 🎉--")

elif num > user_input < 3:
    print("--Computer 💻 Win 🎉--")
elif num < user_input < 3:
    print("--User 😎 Win 🎉--")
