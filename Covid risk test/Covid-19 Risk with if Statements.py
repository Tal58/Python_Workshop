check1= True
age = input("Are you a cigarette addict older than 75 years old? Please enter Yes or No ").title()
#try to get esimated value till it's true
while check1 == True: 
    if age != "Yes" and age != "No":
        age = input("Are you a cigarette addict older than 75 years old? Please enter Yes or No ").title()
    else:
        check1 = False
        check2 = True 
        #try to get esimated value till it's true   
        chronic = input("Do you have a severe chronic disease? Please enter Yes or No ").title() 
        while check2 == True:
                if chronic != "Yes" and chronic != "No":
                      chronic = input("Do you have a severe chronic disease? Please enter Yes or No ").title()
                else:
                      check2 = False
                      check3 = True
                      #try to get esimated value till it's true
                      immune = input("Is your immune system too weak? Please enter Yes or No ").title() 
                      while check3 == True:  
                            if immune != "Yes" and immune != "No":        
                                  immune = input("Is your immune system too weak? Please enter Yes or No  ").title() 
                            else:
                                  check3 == False #all entered yes/no values will turn to True/False values
                                  if age == "Yes":
                                     age = True
                                  else:
                                     age = False
                                  if chronic == "Yes":
                                     chronic = True
                                  else:
                                     chronic = False       
                                  if immune == "Yes":
                                     immune = True
                                  else:
                                     immune = False
                                  risk = age or chronic or immune
                                  if risk == True:
                                          print("You are in risky group")
                                          break
                                  else:
                                          print("You are not in risky group")
                                          break 