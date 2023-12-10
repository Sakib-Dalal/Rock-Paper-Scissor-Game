import random
user_input = int(input("What do you choose? Type 0 to Rock 🪨, 1 for Paper 📄 or 2 for Scissors ✂️. \n➡️"))
num = random.randint(0, 2)

rock = 0
paper = 1
scissors = 2

# computer
if num == rock:
    print("Computer Chose: Rock 🪨")
elif num == paper:
    print("Computer Chose: Paper 📄")
elif num == scissors:
    print("Computer Chose: Scissors ✂️")

# user
if user_input == rock:
    print("Use Chose: Rock 🪨")
elif user_input == paper:
    print("Use Chose: Paper 📄")
elif user_input == scissors:
    print("Use Chose: Scissors ✂️")

# algorithm
if num == user_input:
    print("--Draw 🙅‍--")
elif num > user_input:
    print("--Computer 💻 Win 🎉--")
elif num < user_input:
    print("--User 😎 Win 🎉--")
