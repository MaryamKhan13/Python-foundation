def start_room():
 print("\n---DOCTER SIMULATER---")
 print("ITS YOUR FIRST DAY AS A DOCTER AND YOU MUST CURE YOUR PATIENT TO LIVE. YOUR  PATIENT HAS A STOIMATCH BUG AND NEEDS A DIAGNOSIS. ASK QUESTION TO FIND A SOLUTION.")
 choice=input("Do you ask[1]What symtoms are you feeling or [2] Let me get the xray machine ready to see your arm?")
 if choice=="1":
  print(" My symptoms are throwing up non stop and not being able to eat.")
  return"examine_room" # Moving to the next stage 
 else:
  print(" I think you misunderstood me. I have a stomach bug AND YOU KNOW THAT.")  
 return "end"
def examine_room():
    print("\n---THE LAST PHASE---")
    print("YOUR PATIENT’S SYMPTOMS ARE CLEARLY A SIGN OF A STOMACH BUG. YOU HAVE ONE CHANCE FOR A DIAGNOSIS TO LIVE. CHOOSE THE BEST SOLUTION.")

    choice = input("Here is your diagnosis [1] Prochlorperazine or [2] Just drink water: ")

    if choice == "1":
        print("Thank you so much. THE PATIENT LEFT HAPPILY AND YOU STAYED ALIVE BECAUSE OF THE GREAT FEEDBACK SHE GAVE. CONGRATS YOU WIN!")
        return "end"
    else:
        print("You did not listen to me at all. THE PATIENT LEFT ANGRILY AND LATER RETURNED DUE TO HER DISEASE INCREASING BECAUSE SHE REFUSED THE MEDICATION. YOU THEN GOT FIRED AND DIED THE SAME WEEK DUE TO YOUR FAILED JOB. YOU LOSE.")
        return "end"


current_room = "start"
print("Welcome to doctor simulator")

while current_room != "end":
    if current_room == "start":
        current_room = start_room()
    elif current_room == "examine_room":
        current_room = examine_room()



















