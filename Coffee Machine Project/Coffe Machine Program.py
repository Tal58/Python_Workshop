def check_beverages(beverages): #this function checks the store of the machine if it is higher than requested amount the programme will continue 
        if coffe_machine[beverages]["water"] > coffe_machine["Storage/Report"]["water"]: 
            print("Sorry there is not enough water")
        elif coffe_machine[beverages]["milk"] > coffe_machine["Storage/Report"]["milk"]:
            print("Sorry there is not enough milk")
        elif coffe_machine[beverages]["coffee"] > coffe_machine["Storage/Report"]["coffee"]:
            print("Sorry there is not enough Coffe")
        else:                       
            print(f'Your {beverages} will be ready if you insert ${coffe_machine[beverages]["money"]}')
            return True
            
def money_money(): #this function collects the coins if it is bigger than requested amount returns it otherwise the loop will continue
    debit = 0
    while True:        
        moneys = input(f"Please enter your coins (quarter, dimes, nicles, pennies) to take your {request}=> ").lower()         
        if moneys == "quarter":
            debit +=0.25
            coffe_machine["pieces_coins"]["quarter"] += 1
        elif moneys == "dimes":
            debit +=0.1
            coffe_machine["pieces_coins"]["dimes"] += 1
        elif moneys == "nicles":
            debit +=0.05
            coffe_machine["pieces_coins"]["nicles"] += 1
        elif moneys == "pennies":
            debit += 0.01
            coffe_machine["pieces_coins"]["pennies"] += 1
        else:
            print("Please enter proper coin")
        if debit < coffe_machine[request]["money"]:
            print()
            print(f'Sorry you have ${"{:.2f}".format(debit)} now. Please add ${"{:.2f}".format(coffe_machine[request]["money"]- debit)}')
            print()
        else:
            return debit

def store_changes(beverages): #if user can get its beverage, beverage's amounts will be deducted from store
        coffe_machine["Storage/Report"]["water"] -=   coffe_machine[beverages]["water"]
        coffe_machine["Storage/Report"]["milk"] -=    coffe_machine[beverages]["milk"]
        coffe_machine["Storage/Report"]["coffee"] -=  coffe_machine[beverages]["coffee"]
        coffe_machine["Storage/Report"]["money"] +=   coffe_machine[beverages]["money"]

def store_adding(): #this function is to add  water, milk and coffee to machine capacity of the store is (water : 2500, milk : 2500, coffee: 2500)
    checkitems = True
    while checkitems:
        items = input("What would you like to add? Money, water, milk or coffee? ")
        if items.lower() == "water" or items.lower() == "milk" or items.lower() == "coffee" or items.lower() == "money":
            checkitems= False
            if items.lower() == "water":
                print(f'we have only {2500-coffe_machine["Storage/Report"]["water"]} enough space')
                watercheck=True
                while watercheck:
                    water = input("Please enter your water in ml ")
                    if coffe_machine["Storage/Report"]["water"] + int(water) <= 2500:
                        watercheck=False
                        coffe_machine["Storage/Report"]["water"] +=  int(water)
                        print()
                        print()
                        print("------------------------------------")
                        print("Your execution has been completed...")
                        print("------------------------------------")
                    else:    
                        print("Sorry lmit is 2500 ml please try again")  
            elif items.lower() == "milk":
                print(f'we have only {2500-coffe_machine["Storage/Report"]["milk"]} enough space')
                milkcheck=True
                while milkcheck:
                    milk = input("Please enter your milk in ml ")
                    if  coffe_machine["Storage/Report"]["milk"] + int(milk)<= 2500:
                        milkcheck = False             
                        coffe_machine["Storage/Report"]["milk"] += int(milk)
                        print()
                        print()
                        print("------------------------------------")
                        print("Your execution has been completed...")
                        print("------------------------------------")
                    else:
                        print("Sorry lmit is 2500 ml please try again")
            elif items.lower() == "coffee":
                print(f'we have only {2500-coffe_machine["Storage/Report"]["coffee"]} enough space')
                coffeecheck=True
                while coffeecheck:
                    coffee = input("Please enter your milk in ml ")
                    if  coffe_machine["Storage/Report"]["coffee"] + int(coffee)<= 2500:
                        coffeecheck = False             
                        coffe_machine["Storage/Report"]["coffee"] += int(coffee)
                        print()
                        print()
                        print("------------------------------------")
                        print("Your execution has been completed...")
                        print("------------------------------------")
                    else:
                        print("Sorry lmit is 2500 ml please try again")
            elif items.lower() == "money":
                print(f'we have only ${coffe_machine["Storage/Report"]["money"]}')
                control = True
                while control:
                    money = input("would you like to add some money? Yes or No ")
                    if money.lower() =="yes":
                        control = False
                        moneycheck = True
                        while moneycheck:
                            addmoney = input("How much will you add?")
                            if addmoney.isdigit():
                                moneycheck = False
                                coffe_machine["Storage/Report"]["money"] += int(addmoney)
                                print()
                                print()
                                print("------------------------------------")
                                print("Your execution has been completed...")
                                print("------------------------------------")
                            else:
                                print("You made a mistake please try again")
                    elif money.lower() =="no": 
                        control = False               
                        moneycheck = True
                        while moneycheck:
                            moneycut = input("How much will you take? ")
                            if moneycut.isdigit():
                                if coffe_machine["Storage/Report"]["money"] >= int(moneycut):
                                    moneycheck=False
                                    coffe_machine["Storage/Report"]["money"] -= int(moneycut)
                                    print("Your execution has been completed...")
                                else:
                                    print("We don't have enough money")
                            else:
                                print("You made a mistake please try again")
                    else:
                        print("You made a mistake please try again")
        else:
            print("You made a mistake please try again")

def coins(debit):
    while True:        
        if debit >= 0.25:
            coffe_machine["pieces_coins"]["quarter"] -= 1
            customer["quarter"] += 1
            debit -= 0.25
            debit = round(debit,2)
        elif debit >= 0.1:
            coffe_machine["pieces_coins"]["dimes"] -= 1
            customer["dimes"] +=  1
            debit -= 0.1
            debit = round(debit,2)
        elif debit >= 0.05:
            coffe_machine["pieces_coins"]["nicles"] -= 1
            customer["nicles"] +=  1
            debit -= 0.05
            debit = round(debit,2)
        elif debit >= 0.01:
            coffe_machine["pieces_coins"]["pennies"] -= 1
            customer["pennies"] +=  1
            debit -= 0.01
            debit = round(debit,2)
        else:
            return customer

coffe_machine = { "espresso" : {"water" : 50,
                                "milk"  : 0,
                                "coffee": 76,
                                "money" : 1.75},

                 "latte" : {"water" : 100,
                                "milk"  : 50,
                                "coffee": 76,
                                "money" : 2},
                                
                "cappuccino" : {"water" : 75,
                                "milk"  : 75,
                                "coffee": 76,
                                "money" : 2.25},

                "Storage/Report" : {"water" : 1000,
                                    "milk"  : 1000,
                                    "coffee": 1000,
                                    "money" : 4.1}, 
                "pieces_coins"  :   {"quarter" : 10,
                                    "dimes"   : 10,
                                    "nicles"  : 10,
                                    "pennies" : 10} }

money = { "quarter" : 0.25,
          "dimes"   : 0.1,
          "nicles"  : 0.05,
          "pennies" : 0.01}

customer = { "quarter" : 0,
          "dimes"   : 0,
          "nicles"  : 0,
          "pennies" : 0}

customer_coins= {}
control = True
control2 = True #control2 is used to do something as an admin account
machine_open_close = True #machine_open_close will remain True till maintainers control the machine
beverage_check = False #if it is false the machine can not serve beverage to the user   
while machine_open_close == True:
    while control == True:
        print("----------------------------------------------------------------------")
        print(f'storage report: water ==>>{coffe_machine["Storage/Report"]["water"]}ml milk==>> {coffe_machine["Storage/Report"]["milk"]}ml Coffee ==>> {coffe_machine["Storage/Report"]["coffee"]}g')
        print(f'espresso: ${coffe_machine["espresso"]["money"]} and it requires {coffe_machine["espresso"]["water"]} ml water, {coffe_machine["espresso"]["milk"]} ml milk and {coffe_machine["espresso"]["coffee"]}gr coffee')
        print(f'latte: ${coffe_machine["latte"]["money"]} and it requires {coffe_machine["latte"]["water"]}ml water, {coffe_machine["latte"]["milk"]} ml milk and {coffe_machine["latte"]["coffee"]}gr coffee')    
        print(f'cappuccino: ${coffe_machine["cappuccino"]["money"]} and it requires {coffe_machine["cappuccino"]["money"]}ml water, {coffe_machine["cappuccino"]["money"]} ml milk and {coffe_machine["cappuccino"]["money"]}gr coffee')
        print("----------------------------------------------------------------------")
        print()
        print()
        request = input("What would you like to drink? Espresso/Latte/Cappuccino=> ").lower()
        if request == "espresso" or request == "latte" or request == "cappuccino":          
            beverage_check=check_beverages(request)  
            if beverage_check == True:
                debit = money_money() 
                debit = debit - coffe_machine[request]["money"]             
                print(f'Your {request} is ready now enjoy it.')
                if debit !=0:
                    print( f'You have ${"{:.2f}".format(debit)} at the bottom of the machine')
                    customer_coins = coins(debit)
                    print(f"You will receive {customer_coins}")
                store_changes(request)
                for i in customer: #to reset customer coins because he has already taken it
                    customer[i] = 0
                print(coffe_machine["Storage/Report"])
                print(coffe_machine["pieces_coins"])
                control = True # to reopen the system
                beverage_check = False  #to close beverage delivery system              
        elif request == "maintenance":
            machine_open_close == False #the machine turns off
            control = False
            print()
            print()
            print("-----------------------------------------------------------------")
            print("System will be shut down")
            print("-----------------------------------------------------------------")
            import sys 
            sys.exit() 
        elif request == "admin":
            control = False
            print()
            print()
            print("-----------------------------------------------------------------")
            print(f'storage report: water ==>>{coffe_machine["Storage/Report"]["water"]}ml milk==>> {coffe_machine["Storage/Report"]["milk"]}ml Coffeee ==>> {coffe_machine["Storage/Report"]["coffee"]}g')
            print(f'storage report: money ==>>${"{:.2f}".format(coffe_machine["Storage/Report"]["money"])}')
            print("-----------------------------------------------------------------")
            while control2 ==True:
                add_items = input("would you like to add some materials(milk/water/coffee/money)? Please enter Yes or No=> ").lower()
                if (add_items == "yes") or (add_items == "no"):
                    control2= False
                    if add_items =="yes":
                        store_adding()
                        print()
                        print()
                        print("-----------------------------------------------------------------")
                        print(f'storage report: water ==>>{coffe_machine["Storage/Report"]["water"]}ml milk==>> {coffe_machine["Storage/Report"]["milk"]}ml Coffeee ==>> {coffe_machine["Storage/Report"]["coffee"]}g')
                        print(f'storage report: money ==>>${"{:.2f}".format(coffe_machine["Storage/Report"]["money"])}')
                        print("-----------------------------------------------------------------")
                    else:
                        continue
                else:
                    print("You made a mistake. Please try again.")         
            print("program will be closed...")
            import sys 
            sys.exit()
        else:
            print("You made a mistake please try again.")

