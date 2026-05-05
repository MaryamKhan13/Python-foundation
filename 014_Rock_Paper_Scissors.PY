import random
def play_game():
    options=("rock","paper","scissors")
user_score=0
computer_score=0
print("---Welcome to the pyhton battle arena---")
while True
 user_choice=input("\nChoose rock,paper, or scissors(or type 'quit' to exit):").lower()
 if user_choice=='quit':
    break
 if user_choice not in options:
   print("Invalid choice! Try Again")
   continue
 #Computer makes a random choice
 computer_choice=random.choice(options)
 print(f"Computer chose:{computer_choice}")
 #Determine the winner
 if user_choice==computer_choice:
    print("Its a TIE!")
 elif(user_choice=="rock"and computer_choice=="scissors") or\
     (user_score=="paper"and computer_choice=="rock") or\
     (user_score=="scissors"and computer_choice=="paper"):
    print("You Win!")
    user_score+= 1
else
   print("Computer Wins!")
   computer_score+=1
   