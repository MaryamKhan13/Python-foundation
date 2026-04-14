#   We store the names and prices in variables before they are used
chiilen_chair_description= "Chillen Chair. Soft cotton on a smooth sanded wood base. 18 inches hign * 35 inches wide * 30 inches deep. Blue or Teal"
chillen_chair_price =176.00

lazy_lounger_descrption= "Lazy Lounger. Feather leather arund the exterior and soft cotton on the interior. 60 inches wide * 73 inches high * 23 inches deep. Gray or Dark Pink "
lazy_lounger_price = 230.00 

peachin_patio_set_description= "Peachin Patio Set. Six wodd with cotton seat chairs, One circle wooden table, and on large umbrella(waterproof). Brown with cream and black with white colors."
peachin_patio_set_price= 570.00

#We set a tax of(5.4%)
sales_tax=0.544444
 
 #Every customer starts with o dollars and no items
customer_one_total=0
customer_one_itemization=""

#The customer decides to buy a Chillen Chair
customer_one_total +=chillen_chair_price
customer_one_itemization +=chiilen_chair_description +"/n"

#The customer also  decides to buy a Peachin Patio Set
customer_one_total +=peachin_patio_set_price
customer_one_itemization += peachin_patio_set_description +"/n"
 
 #Calculate the Tax based on subtotal
customer_one_tax = customer_one_total * sales_tax

#Add the tax to the running total
customer_one_total +=customer_one_tax

#We use f-strings for professional currency formatting
print("\n" +"*"*30)
print(" OFFICIAL RECEIPT")
print("*"*30)

print("/nCUSTOMER ITEMS:")
print( customer_one_itemization)

print("-"*30)
print(f"SUBTOTAL+TAX:${customer_one_total:.2f}")
print("*"*30)
print(" THANK YOU FOR SHOPPING")
print("*"*30)
