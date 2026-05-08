"""import random

items = ["rock", "paper", "scissor"]

user_score = 0
comp_score = 0

while True:
    print("\n1. Play")
    print("2. Reset Score")
    print("3. Exit")

    choice = input("Enter option: ")

    if choice == "1":
        comp_choice = random.choice(items)
        user_choice = input("Enter your choice: ").lower()

        print("User:", user_choice)
        print("Computer:", comp_choice)

        if user_choice == comp_choice:
            print("Match is tie")

        elif (user_choice == "paper" and comp_choice == "rock") or \
             (user_choice == "rock" and comp_choice == "scissor") or \
             (user_choice == "scissor" and comp_choice == "paper"):
            user_score += 1
            print("User wins")

        else:
            comp_score += 1
            print("Computer wins")

        print("Score → User:", user_score, "| Computer:", comp_score)

    elif choice == "2":
        user_score = 0
        comp_score = 0
        print("Score reset successfully ✅")

    elif choice == "3":
        print("Exiting game 👋")
        break

    else:
        print("Invalid option ❌")"""


import random
import tkinter as tk

items = ["rock", "paper", "scissor"]

# scores
user_score = 0
comp_score = 0

# main game logic
def play(user_choice):
   # global user_score, comp_score

    comp_choice = random.choice(items)

    if user_choice == comp_choice:
        result = "Match is tie"

    elif (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "rock" and comp_choice == "scissor") or \
         (user_choice == "scissor" and comp_choice == "paper"):
        user_score += 1
        result = "User wins"

    else:
        comp_score += 1
        result = "Computer wins"

    # update UI
    result_label.config(
        text=f"User: {user_choice} | Computer: {comp_choice}\n{result}"
    )
    score_label.config(
        text=f"Score → User: {user_score} | Computer: {comp_score}"
    )

# reset function
def reset_scores():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    score_label.config(text="Score → User: 0 | Computer: 0")
    result_label.config(text="Scores reset!")

# exit function
def exit_game():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissor Game")
root.geometry("400x300")

title = tk.Label(root, text="Rock Paper Scissor", font=("Arial", 16))
title.pack(pady=10)

# buttons
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Rock", width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper", width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissor", width=10, command=lambda: play("scissor")).grid(row=0, column=2, padx=5)

# result display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# score display
score_label = tk.Label(root, text="Score → User: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# reset + exit buttons
tk.Button(root, text="Reset", command=reset_scores).pack(pady=5)
tk.Button(root, text="Exit", command=exit_game).pack(pady=5)

# run app
root.mainloop()