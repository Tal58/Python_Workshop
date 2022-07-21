stock_value = {"apple": [10,10],
                "pear": [12,5],
                "tomato": [8,20],
                "pepper": [20,4]}
stock_value_price =  {10:"apple" ,
                      12 : "pear",
                       8 : "tomato",
                      20:"pepper"}
customer = {"apple": [10,0],
                "pear": [12,0],
                "tomato": [8,0],
                "pepper": [20,0]}

while True:
    try:
        money = int(input("Welcome to our market. Please enter your budget to do your shooping...\n(please enter your character between[0-9] ==>>"))
        if money >0:
            break
        else:
            print("You made a mistake please try again")
    except Exception as e:
        print(f"{e}. Please try again")
print()
print("------------------------------------------------------------------------------")        
print("According to our regulations, we would like to sell our products as follows;")
print("Product Name:   Price:   Kg:(multiples of *) ")
for x in stock_value.keys():
    print(f"{x}           {stock_value[x][0]}       {stock_value[x][1]}")

print("------------------------------------------------------------------------------")   

def customer_request_control():
    for x in customer.keys():
        try:                
            customer_demand = int(input(f"How many kg would you like to buy {x} ==>>?  "))
            customer[x][1] +=customer_demand                           
        except Exception as e:
            print(f"{e}. Please try again")


comparison = sorted(stock_value_price.keys(),reverse =True) #sort the items according to values

def shopping():
    global money
    for x in comparison:       
            total_kg = customer[stock_value_price[x]][1] - customer[stock_value_price[x]][1] % stock_value[stock_value_price[x]][1]
            if money >= (customer[stock_value_price[x]][0] * total_kg):
                money = money - (total_kg * customer[stock_value_price[x]][0])
                customer[stock_value_price[x]][1] = total_kg
                total_kg=0 #to reset the value
            else: 
                max_affordable_kg= (money/stock_value[stock_value_price[x]][0])-((money/stock_value[stock_value_price[x]][0]) % stock_value[stock_value_price[x]][1])
                money = money - (max_affordable_kg * customer[stock_value_price[x]][0])
                customer[stock_value_price[x]][1] = max_affordable_kg
                max_affordable_kg=0 #to reset the value

customer_request_control()
shopping()
for x in customer.keys():
    print(f"You can buy {customer[x][1]} kg {x}")
print(f"You have ${money} left. Thanks for shopping")
 