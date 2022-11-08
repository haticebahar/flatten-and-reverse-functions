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




def DifferentCases(str): 
    newStr = ''
    finalWord = []
    
    for char in str:
        if char.isalpha():
            newStr += char
        else:
            newStr += ' '
            
    for word in newStr.split():
        word = word.replace(word[0], word[0].upper())
        word = word.replace(word[1:len(word)], word[1:len(word)].lower())
        finalWord.append(word)
        
    return ''.join(finalWord)
