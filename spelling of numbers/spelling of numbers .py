number_list = ["0","1","2","3","4","5","6","7","8","9"]
written_form = ["zero","one","two","three","four","five","six","seven","eight","nine"]
trial = 0
addition = 0
text_form = ""
check = True
while check == True:
    number = input("Please enter a number: ")
    for x in number:
        if number_list.count(x) == 1: # check all input values whether it is the number list or not
            trial += 1      
    if trial == len(number): # if all entered values are in the number list trial will equal to length of the entered value
        check = False
        for y in number:
            text_form = text_form + f"{written_form[int(y)]} ".title()
            
        print(text_form)

    else:  
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        trial = 0               #for continuation of the while loop we reset the two values to zero 
        addition = 0
