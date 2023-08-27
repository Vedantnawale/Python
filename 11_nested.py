price = input("Enter the price of product : ")
budget = 300
if(int(price)<125):
    print("Buy the product")
elif(200>=int(price)):
    if(int(price)==200):
        print("Nasta cancel")
    elif(180>int(price)>150):
        print("Double Plate Nasta with tea")
    else:
        print("One Plate Nasta")
else:
    print("Budget Overload")