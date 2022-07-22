months_dict = {"01": 31,
                "02": 28,
                "03": 31,
                "04": 30,
                "05": 31,
                "06": 30,
                "07": 31,
                "08": 31,
                "09": 30,
                "10": 31,
                "11": 30,
                "12": 31}

def day_subtractor(date1, date2):
    months_to_days1,months_to_days2 = 0,0
    days1 = int(date1.split(".")[0])
    for i in range(1,int(date1.split(".")[1])+1):
        if i < 10:
            months_to_days1 += months_dict["0"+str(i)] 
        else:
            months_to_days1 += months_dict[str(i)] 
    years_to_days1 = int(date1.split(".")[2])*365
    total_days1 = days1 + months_to_days1 + years_to_days1
    days2 = int(date2.split(".")[0])
    for i in range(1,int(date2.split(".")[1])+1):
        if i < 10:
            months_to_days2 += months_dict["0"+str(i)] 
        else:
            months_to_days2 += months_dict[str(i)]
    years_to_days2 = int(date2.split(".")[2])*365
    total_days2 = days2 + months_to_days2 + years_to_days2
    if total_days1 > total_days2:
        print(f"There are {total_days1 - total_days2} days between two dates")
    else:
        print(f"There are {total_days2 - total_days1} days between two dates")
control_date1 = True
control_date2 = True
while control_date1:
    date1 = input('Date-1 (DD.MM.YYYY): ')
    if len(date1.split(".")) ==3:
        if date1.split(".")[2].isdigit() and date1.split(".")[0].isdigit() and date1.split(".")[1].isdigit() and int(date1.split(".")[1]) < 13 and int(date1.split(".")[0])<=  months_dict[date1.split(".")[1]]:
            control_date1 = False      
            while control_date2:
                date2 = input('Date-2 (DD.MM.YYYY): ')
                if len(date2.split(".")) ==3:
                    if date2.split(".")[2].isdigit() and date2.split(".")[0].isdigit() and date2.split(".")[1].isdigit() and int(date2.split(".")[1]) < 13  and int(date2.split(".")[0])<=  months_dict[date2.split(".")[1]]:  
                        control_date2 = False
                        day_subtractor(date1,date2)
                    else:
                        print("You made a mistake please try again") 
                else:
                    print("You made a mistake please try again")                           
        else:
            print("You made a mistake please try again")
    else:
        print("You made a mistake please try again")
            
             
   




