Base=["Brown Basmati rice with Arudula,chicken and no suace",
       "Saffron Basmati rice with super greens,falefel and hummus",
       "Black lentils with baby spinach,grilled beef,pickels, and ranch"
      ]
prices=[9,12,14]
num_Bowl=len(Base)
print(f"We sell many {num_Bowl} diffrent kids of Bowls")
Bowls=list(zip(prices,Base))
print("\nUnsorted Bowls(price,Bowls):")
print(Bowls)
Bowls.sort() #SORTS FROM CEAPEST TO MOST EXPENSIVE
print("\nSorted Menu:")
print(Bowls)
cheapest_Bowl=Bowls[0]
priciest_Bowl=Bowls[2]
three_cheapest=Bowls[:3] #Slices from index 0 to 2
print(f"\nCheapest option: {cheapest_Bowl}")
print(f"Priciest option: {priciest_Bowl}")
print(f"Budget Options: {three_cheapest}")

