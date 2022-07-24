new_list = []
# list = [
# [ 13, 14, 15, 16, 1],
# [ 12, 23, 24, 17, 2],
# [ 11, 22 ,25, 18, 3],
# [ 10, 21, 20, 19, 4],
# [ 9, 8, 7, 6, 5]
# ]

# list = [
#     [12,13,14,15,16,1],
#     [11,22,23,24,17,2],
#     [10,21,20,19,18,3],                       #as you wish you can check other list.
#     [9,8,7,6,5,4]
# ]


list = [[19,20,21,22,23,24,1],
        [18,37,38,39,40,25,2],
        [17,36,47,48,41,26,3],
        [16,35,46,49,42,27,4],
        [15,34,45,44,43,28,5],
        [14,33,32,31,30,29,6],
        [13,12,11,10,9,8,7]]

while len(list)>= 1 and len(list[0]) >= 1 :    # if len(list)>= 1 and len(list[0]) >= 1:(this case used many times because  the loop finishes in the middle of the loop)
        for x in range(0,len(list)):    
                new_list.append(list[x][len(list)-1])    
                list[x].pop()
        if len(list)>= 1 and len(list[0]) >= 1:                  
                for x in reversed(range(0,len(list[0]))):
                    new_list.append(list[len(list)-1][x])
                list.pop(-1) 
        if len(list)>= 1 and len(list[0]) >= 1:            
                for x in reversed(range(0,len(list))):    
                   new_list.append(list[x][0])
                   list[x].pop(0) 
        if len(list)>= 1 and len(list[0]) >= 1:     
                for x in range(0,len(list[0])):
                  new_list.append(list[0][x])
        list.pop(0)
print(new_list)
         

    


                   




       




# for x in range(0,5):
#     new_list.append(list[x][4])
#     print(new_list)
#     for x in range(0,4):
#         list[x].pop(-1)
#         print(list)
        # for x in reversed(range(0,3)):
        #     new_list.append(list[3][x])
        #     print(new_list)
        # for x in reversed(range(0,4))
        # list = list[x].pop(-1)


# for x in reversed(range(3)):
#     new_list.append(list[4][x])
#     print(new_list)
# for x in reversed(range(3)):
#     new_list.append(list[x][0])
#     print(new_list)
# for x in range(1,4):
#     new_list.append(list[0][x])
#     print(new_list)
# for x in range(1,4):
#     new_list.append(list[x][3])
#     print(new_list)
# for x in reversed(range(1,3)):
#     new_list.append(list[3][x])
#     print(new_list)
# for x in reversed(range(1,3)):
#     new_list.append(list[x][1])
#     print(new_list)
# for x in range(1,3):
#     new_list.append(list[x][2])
#     print(new_list)




