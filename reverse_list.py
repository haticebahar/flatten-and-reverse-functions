def reverse(mylist):
    
    for i in range(int(len(x)/2)):
        temp = mylist[i]
        mylist[i] = mylist[len(mylist)-(i+1)]
        mylist[len(mylist)-(i+1)] = temp
        
    counter = 0
    for i in mylist:
        if isinstance(i,list):
             
            for a in range(int(len(i)/2)):
                temp = mylist[counter][a]
                mylist[counter][a] = mylist[counter][len(i)-(a+1)]
                mylist[counter][len(i)-(a+1)] = temp
                counter +=1
    print(mylist)
                


mylist = [[1, 2], [3, 4], [5, 6, 7]] # given input 
reverse(mylist)