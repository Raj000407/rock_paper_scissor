#we are making a game which is very famous mostly use for deciding the winning teams between the teams which is called rock,paper and scissior

"""import random
items = ["Rock" , "Paper" , "Scissor"]
comp_choice = random.choice(items)


#now i want user inputs
user_choice = input("Enter the choice")
print("user choice  is:",user_choice)

print("computer choice is:",comp_choice)

#rock
if (user_choice==comp_choice):
    print("match is tie")
elif(comp_choice=="Paper"):
    print("comp wins")
else:
    print("user wins")

#paper
if (user_choice==comp_choice):
    print("match is tie")
elif(comp_choice=="Scissor"):
    print("user_input wins")
else:
    print("computer wins")

#Scissor
if (user_choice==comp_choice):
    print("match is tie")
elif(comp_choice=="Paper"):
    print("user wins")
else:
    print("computer wins")"""



""" updated code"""


import random
import tkinter as tk
items=["rock","paper","scissor"]


"""updated scores"""
users_scores=0
comps_scores=0


"""conditions"""
#while True:
def play(users_choice):
  # print("1.play")
  # print("2.Reset")
  # print("3.Exit")
        global users_scores , comps_scores

        comps_choice=random.choice(items)
  

        if(users_choice==comps_choice):
         result="match is tie"

        elif(users_choice=="paper" and comps_choice=="rock") or\
         (users_choice=="rock" and comps_choice=="scissor") or\
         (users_choice=="scissor" and comps_choice=="paper"):
         users_scores+=1
         result="user wins"
      #   print("user wins")

        else:
         comps_scores+=1
         result="computer wins"
       #  print("computer wins")

        #print("the updated user score is:",users_scores)
        #print("updated computer score is:",comps_scores)

        result_label.config(
          text=f"User: {users_choice} | computer: {comps_choice}\n{result}"
        )
        score_label.config(
          text=f"Score-> user: {users_scores} | computer: {comps_scores}"
        )

def reset_scores():
    global users_scores , comps_scores
    users_scores=0
    comps_scores=0
   # print("the user score is updated to 0")
   # print("the computer score is updated to 0")
    score_label.config(text="score->user :0 | computer:0")
    result_label.config(text="scores reset!")

def exit_game():
   # print("Thanks for playing my first game✨")
    root.destroy()
#print("updated users choice:",user_choice)
#print("updated comp_choice",comp_choice)



"""updated code adding GUI""" 
root=tk.Tk()
root.title("1st game🎮🎯")
root.geometry("1920x1080")

title=tk.Label(root , text = "Rock Paper Scissor" , font=("Arial",30))
title.pack(pady=10)

#buttons
frame=tk.Frame(root)
frame.pack(pady=100)

tk.Button(frame, text="ROCK",width=50 , command=lambda: play("rock")).grid(row=0 , column=0 , padx=5)
tk.Button(frame, text="PAPER",width=50 , command=lambda: play("paper")).grid(row=0 , column=1 , padx=5)
tk.Button(frame, text="SCISSOR",width=50 , command=lambda: play("scissor")).grid(row=0 , column=2 , padx=5)


#result
result_label=tk.Label(root , text="" , font = ("Arial",20))
result_label.pack(pady=10)

#score display
score_label=tk.Label(root , text="score-> user : 0 |  computer : 0", font = ("Arial",20))
score_label.pack(pady=80)

#reset+exit button
tk.Button(root , text="RESET" , command=reset_scores).pack(pady=5)
tk.Button(root , text="EXIT" , command=exit_game).pack(pady=5)

root.mainloop()







