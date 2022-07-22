def add_gamer(gamer, gamers):    #this function is used to check input of gamer, if it covers the requirements, input parameters will be added to gamers list
    count = 0
    if isinstance(gamer['name'], str) and len(gamer['name']) >=2:
        for x in gamer['availability']:
            if x in availability_list:
                count +=1
        if count == len(gamer['availability']):
             gamers[gamer['name']] = gamer['availability']
        else:
            print( "You did not enter available day")
    else:
        print("You made a mistake while entering gamer name") 

def build_daily_frequency_table(): #this function contain build_daily_frequency_table(), check all day according to the gamers availability and calculate availability
    Monday,Tuesday,Wednesay,Thursday,Friday,Saturday,Sunday =0,0,0,0,0,0,0  
    names= list(gamers.keys())
    for x in range(0,len(names)):
        for y in gamers[names[x]]:
            if y == "Monday":
                Monday+=1
                count_availability[y] = Monday
            elif y== "Tuesday":
                Tuesday+=1
                count_availability[y] = Tuesday
            elif y=="Wednesday":
                Wednesay+=1
                count_availability[y] = Wednesay
            elif y=="Thursday":
                Thursday+=1
                count_availability[y] = Thursday
            elif y=="Friday":
                Friday+=1
                count_availability[y] = Friday
            elif y=="Saturday":
                Saturday+=1
                count_availability[y] = Saturday
            elif y=="Sunday":
                Sunday+=1
                count_availability[y] = Sunday
    
    return count_availability

def find_best_night(): #this function is used to find max players in the best day for game
    return max(count_availability.values())
def second_night(): #this function is used to find second max players in the best day for game
    day_values = list(count_availability.values())
    second_value = sorted(day_values)[-2]
    return second_value

def game_night(): #this function is used to get the most available day for the game 
    for x in availability_list:
        if count_availability[x] == find_best_night():
            return x  
def second_game_night(): #this function is used to get the most available second day for the game 
    for x in availability_list:
        if count_availability[x] == second_night():
            return x 
def available_on_night(): #this function is used to get attending/not attending list of players on game night
    names= list(gamers.keys())
    for x in range(0,len(names)):
        for y in gamers[names[x]]:
            if y == game_night():
                attending_game_night.append(names[x]) 
    for z in names:
        if z not in attending_game_night:
            not_attending.append(z)

def second_available_on_night(): #this function is used to get attending/not attending list of players on second game night
    names= list(gamers.keys())
    for x in range(0,len(names)):
        for y in gamers[names[x]]:
            if y == second_game_night():
                second_attending_game_night.append(names[x]) 
    for z in names:
        if z not in second_attending_game_night:
            second_not_attending.append(z)

def send_email(): #this function is used to send e-mail to the players
    for x in attending_game_night:
        print(f"The e-mail has already sent to {x} on {game_night()}'s Abruptly Goblins!")
def second_send_email(): #this function is used to send e-mail to the players
    for x in second_attending_game_night:
        print(f"The e-mail has already sent to {x} on {second_game_night()}'s Abruptly Goblins!")
gamers= {} #list of people who are attendig game night
count_availability = {}
attending_game_night = []
second_attending_game_night = []
second_not_attending = []
not_attending = []
availability_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
gamer1 = {'name':'Kimberly Warner','availability': ["Monday", "Tuesday", "Friday"]}
add_gamer(gamer1,gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
build_daily_frequency_table()
print(f"Frequency of each day is as follows : {build_daily_frequency_table()}")
print(f"Max players is {find_best_night()}")
print(f"Best day for the game is {game_night()}")
available_on_night()
print(f"list of gamers on {game_night()} is {attending_game_night} ")
print(f"list of gamers who will not attend the game on {game_night()} is {not_attending} even if we call them.")
send_email()
second_available_on_night()
print(f"Max players for second night  is {second_night()}")
print(f"Best day for the second game is {second_game_night()}")
print(f"list of gamers on {second_game_night()} is {second_attending_game_night} ")
print(f"list of gamers who will not attend the game on {second_game_night()} is {second_not_attending} even if we call them.")
second_send_email()
deneme = input("please enter")

