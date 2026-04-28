#Create a list
inventory=["IPAD","LAPTOP","IPHONE"]
# Acessing items
print(f"Primary item:{inventory[0]}") # IPAD
# Modifying the list
inventory.append("Mouse") # Adds to the end
inventory.insert(1,"Webcam") #Adds at the index 1
inventory.pop(0) #Removes "LAPTOP"
print(f"Current Stock:{inventory}")