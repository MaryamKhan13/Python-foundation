import random
print("Generating your 10 lucky numbers...")
lucky_number_string="" # An empty bucket
count=0
while count<10:
 num=random.randint(1,100)
 # Add the number and space to our string bucket
 lucky_number_string+= str(num)+""
 count += 1
 print(f"Your Ticket:{lucky_number_string}")