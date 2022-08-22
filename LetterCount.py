# Have the function LetterCount(str) take the str parameter being passed and return the first word with the
# greatest number of repeated letters.
# For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1.
# Words will be separated by spaces.

def LetterCount(str):
    count2 = 0;
    count1 = 0;
    greatestWord = ""
    newArr= str.split()
    for x in newArr:
        for y in x :
            for i in range(len(x)):
                if x[i] == y:
                    count1+=1
            if count1>count2:
                count2 = count1
                greatestWord = x
                count1 = 0 
            else:
                count1 = 0
    if count2 >=2:
        return greatestWord
    else:
        return -1
print(LetterCount("Today, is the greatest day ever!"))





    


