

def submit_ticket():
 print("\n---NEW TICKET---")
name=input("Your Name:")
issue=input("What is the problem that you are facing?")
#'a' (Append)adds the new ticket to the end of the file
with open("support_log.txt","a") as file:
 file.write(f"NAME:{name} | ISSUE:{issue}\n")
 print(" Ticket submitted successfully!")
 def view_tickets():
  print("\n---OPEN TICKETS---")
try:
   with open("support_log.txt","r")as file:
    print(file.read())
except FileNotFoundError:
 print("No tickets found yet.")
while True:
 choice = input("\n[1] NEW TICKET [2] VIEW TICKET [3] QUIT:")
 if choice == "1":
  submit_ticket()
elif choice == "2"
view_tickets()
elif choice == "3":
