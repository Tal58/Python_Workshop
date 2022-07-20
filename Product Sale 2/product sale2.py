import math
stock_value = {}
sale_value = {}
lost_items = {}
Control1, Control2 = True, True
while Control1:
    item = input("Please enter your item to do our stock...").lower()
    try:
        cost_price = int(input("How much did you pay per 1 kg?==>>   "))
        sale_price = int(input("How much will you sale per 1 kg?==>>   "))
        amount= int(input("How many kg do you have?==>>   "))
        dec_amount= int(input("What percentage will it be lost? Please enter between (0-100)==>>   "))
        if cost_price >0 and sale_price > 0 and amount > 0 and dec_amount > 0:
            stock_value[item] = [cost_price,amount]
            lost_items[item] = [cost_price,amount]
            amount = math.floor(amount*(100-dec_amount)/100)            
            sale_value[item] = [sale_price,amount]
            Control2 = True
            while Control2:
                yes_no = input("Would you like to add more? Please enter yes or no  ").lower()
                if yes_no == "yes":
                    Control2 = False
                elif yes_no == "no":
                    Control1=False
                    Control2=False
                else:
                    print("You made a mistake. Please try again")
        else:
            print("You made a mistake please try again")
    except Exception as e:
        print(f"{e}. Please try again")

total_cost = 0
Total_kg = 0

for x in stock_value.keys():
    total_cost += stock_value[x][0]*stock_value[x][1]
    Total_kg += stock_value[x][1]

Total_Revenue= 0
Total_sale_kg= 0


for x in sale_value.keys():
    lost_items[x][1] = lost_items[x][1]-sale_value[x][1]
    Total_Revenue += sale_value[x][0]*sale_value[x][1]
    Total_sale_kg += sale_value[x][1]


total_lost_value = 0
total_lost_kg = 0

for x in lost_items.keys():
    total_lost_value += lost_items[x][0]*lost_items[x][1]
    total_lost_kg += lost_items[x][1]

Result = Total_Revenue - total_cost
Lost_kg = Total_kg-Total_sale_kg


print()
print()
print("--------------------COST----------------------------------")
print("Product Name:       Cost Price:Kg:(multiples of *) ")
for x in stock_value.keys():
    print(f"{x}                {stock_value[x][0]}              {stock_value[x][1]}")

print("----------------------------------------------------------")

print()
print()
print("--------------------REVENUE-------------------------------")
print("Product Name:       Sale Price:       Kg:(multiples of *) ")
for x in sale_value.keys():
    print(f"{x}                 {sale_value[x][0]}              {sale_value[x][1]}")

print("----------------------------------------------------------")

print()
print()
print("--------------------LOST ITEMS------------------------------")
print("Product Name:       Sale Price:    Lost- Kg:(multiples of *) ")
for x in lost_items.keys():
    print(f"{x}                   {lost_items[x][0]}              {lost_items[x][1]}")

print("-------------------------------------------------------------")
print()
print("---------------------RESULT----------------------------------")
print(f"Total Revenue ==>> ${Total_Revenue} Total cost ==>> ${total_cost} Total profit ==>> ${Result}  Total lost value ==>> ${total_lost_value}")
print(f"Total kg of all items ==>> {Total_kg}kg Total kg of sold items ==> {Total_sale_kg}kg Total lost items ==> {Lost_kg}kg")
print("-------------------------------------------------------------")
mihail= input("please enter to continue")
