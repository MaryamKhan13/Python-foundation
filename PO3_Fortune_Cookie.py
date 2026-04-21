import random

# We pick a random number between 1 and 10
fortune_number = random.randint(1, 10)
lucky_number = random.randint(1, 100)

fortune_text = ""

if fortune_number == 1:
    fortune_text = "A small step today opens a big door tomorrow."
elif fortune_number == 2:
    fortune_text = "Your curiosity will lead you somewhere unexpected and good."
elif fortune_number == 3:
    fortune_text = "An opportunity you’ve been waiting for is already on its way."
elif fortune_number == 4:
    fortune_text = "Kindness you give out will return to you twice over."
elif fortune_number == 5:
    fortune_text = "A surprising answer will arrive when you stop looking for it."
elif fortune_number == 6:
    fortune_text = "A quiet moment will reveal a loud truth."
elif fortune_number == 7:
    fortune_text = "Your next idea will outshine your last one."
elif fortune_number == 8:
    fortune_text = "Someone will appreciate your effort more than you expect."
elif fortune_number == 9:
    fortune_text = "A path you thought was closed will open again."
elif fortune_number == 10:
    fortune_text = "Your patience is about to pay off in an unexpected way."
else:
    fortune_text = "Error: The cookie is empty!"

print("CRACK! Your fortune cookie says:")
print(f"\"{fortune_text}\"")
print(f"Your Lucky Number for today is: {lucky_number}")

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
