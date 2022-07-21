dict_chr = {"(": ")", "{": "}", "[" :"]"}
chr_list_open = ["(","{","["]
chr_list = ["(", ")", "{", "}", "[" ,"]"]
sentence = list(input("Please enter a word: "))
def brackets(words):
    first_bracket = []
    bracket = [] 
    for x in range(0,len(words)):                   #collect opening brackets and other brackets seperately
        if  words[x] in chr_list_open:
            first_bracket.append(words[x])
        if  words[x] in chr_list:
            bracket.append(words[x])
    if len(first_bracket) >0 and len(first_bracket)*2 == len(bracket) : #to check the requested conditions 
        while len(bracket):    
                x=0
                if dict_chr[first_bracket[x]]== bracket[x+1]:
                        first_bracket.pop(x)
                        bracket.pop(x)
                        bracket.pop(x)
                elif dict_chr[first_bracket[x]] == bracket[len(bracket)-1-x]:
                        first_bracket.pop(x)
                        bracket.pop(x)
                        bracket.pop()
                elif bracket[x+1] in first_bracket:
                    for x in range(0,len(bracket)):
                        if bracket[x] not in chr_list_open:
                            return False
                        if dict_chr[first_bracket[x]]== bracket[x+1]:
                          first_bracket.pop(x)
                          bracket.pop(x)
                          bracket.pop(x)
                          break
                        else:
                          x+=1                   
                else:
                        break
        if len(bracket) == 0 and len(first_bracket) ==0:
            return True
        else:
            return False
    elif words == ['"', '"'] or words==["'", "'"]: #to check inputs "" or ''
        return True
    elif len(words) !=0:
                    return " False You did not enter a opening or closing bracket!!!"
    else:
        return False
print(brackets(sentence))