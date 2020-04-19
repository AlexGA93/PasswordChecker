
#lists to check in Ascii map
Upper = list(range(65,91))
Lower = list(range(97,123))
Letters = Upper+Lower
Numbers = list(range(48,58))
Symbols = list(range(33,48))+list(range(58,65))+list(range(91,97))

Middle = list(range(33,48))+list(range(48,58))+list(range(58,65))+list(range(91,97))+list(range(123,255))

#print('Middle: ', Middle)
#counters
countersArray = [
    ['countSize','countUpper','countLower','countNumber','countSymbols','countMiddle','countRequirements'],
    ['countLettersOnly','countNumbersOnly','countRepChars','countConsUpp','countConsLow','countConsNum','countSeqLetters','countSeqNumbers','countSeqSymbols']
]
#Dictionaries(sorting countersArray's elements as dictionaries to better interaction)
counter_Additions = dict.fromkeys(countersArray[0],0)
counter_Deductions = dict.fromkeys(countersArray[1],0)
###############################################################################################################
                                        #Functions
def Deductions(password):
    #Letters only
    if(counter_Additions['countNumber']==0 and counter_Additions['countSymbols']==0 ):
        counter_Deductions['countLettersOnly'] = len(password)
    #Numbers Only
    elif(counter_Additions['countUpper']==0 and counter_Additions['countLower']==0 and counter_Additions['countSymbols']==0  ):
        counter_Deductions['countNumbersOnly'] = len(password)
    #Repeat Characters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rep_char = 0
    for elem in alphabet:
        counter = password.count(elem)
        if(counter>1): rep_char+=counter
    #print(rep_char)  #5
    counter_Deductions['countRepChars'] = rep_char

    #Consecutives
    countU = 0
    countL = 0
    countN = 0
    for i in range(len(password)):
        if(i>0):
            #que es?
            if(password[i].isupper() and password[i-1].isupper()):
                #if(password[i-1].isupper()):
                countU+=1
            elif(password[i].islower() and password[i-1].islower()):
                #if(password[i-1].islower()):
                countL+=1
            elif(password[i].isnumeric() and password[i-1].isnumeric()):
                #if(password[i-1].isnumeric()):
                countN+=1
    #print('Contador Mayusculas: ',counter_u-1,'\nContador Minusculas: ',counter_l-1,'\nContador Numeros: ',counter_n-1)
    counter_Deductions['countConsUpp'] = countU
    counter_Deductions['countConsLow'] = countL
    counter_Deductions['countConsNum'] = countN
    #Sequential Letters
    #Sequential Numbers
    #Sequentials Symbols
    list_p = []

    count_ele_l = 0
    count_ele_n = 0
    count_ele_s = 0 
    keyboard_symbols = [64, 35, 36, 37, 94, 38, 42, 40]
    for i in range(len(password)):list_p.append(ord(password[i]))
    for i in range(len(password)):
        actual = list_p[i]
        #check if letter turn to lower
        if actual in Letters: 
            word1 = chr(actual).lower()
            actual = ord(word1)
            list_p[i] = actual
            if((i>=2) and (list_p[i-1] == actual-1) and (list_p[i-2] == actual-2)):
                count_ele_l+=1
        elif (actual in Numbers):
            if((i>=2) and (list_p[i-1] == actual-1) and (list_p[i-2] == actual-2)):
                count_ele_n+=1
        elif (actual in keyboard_symbols):
            if((i>=2) and (list_p[i-1] == actual-1) and (list_p[i-2] == actual-2)):
                count_ele_s+=1

    #storage
    counter_Deductions['countSeqLetters'] = count_ele_l
    counter_Deductions['countSeqNumbers'] = count_ele_n
    counter_Deductions['countSeqSymbols'] = count_ele_s
    resul = (counter_Deductions['countLettersOnly']) + (counter_Deductions['countNumbersOnly'])+ (counter_Deductions['countRepChars']) + (counter_Deductions['countConsUpp']*2) + (counter_Deductions['countConsLow']*2) + (counter_Deductions['countConsNum']*2) + (counter_Deductions['countSeqLetters']*3) + (counter_Deductions['countSeqNumbers']*3) + (counter_Deductions['countSeqSymbols']*3) 

    #return result
    return resul
def Additions(password):
    #checking number of characters
    numberChar = len(password)
    counter_Additions['countSize'] = numberChar

    for element in password:
        ascii_element = ord(element) #every character will be compared to the dictionaries
        #print(ascii_element)
        if ascii_element in Upper:
            counter_Additions['countUpper']+=1
        elif ascii_element in Lower:
            counter_Additions['countLower']+=1
        elif ascii_element in Numbers:
            counter_Additions['countNumber']+=1
        elif ascii_element in Symbols:
            counter_Additions['countSymbols']+=1

        if (password.index(element) !=0 and password.index(element)!= len(password)-1):
            if ascii_element in Middle:
                counter_Additions['countMiddle']+=1

    #Checking dictionaries for requirments
    for key in counter_Additions:
        if (counter_Additions[key] > 0 )and (key!= 'countMiddle') and(key!= 'countRequirements'):
            counter_Additions['countRequirements']+=1
        
    result = (counter_Additions['countSize']*4)+((counter_Additions['countSize']-counter_Additions['countUpper'])*2)+((counter_Additions['countSize']-counter_Additions['countLower'])*2)+(counter_Additions['countNumber']*4)+(counter_Additions['countSymbols']*6)+(counter_Additions['countMiddle']*2)+(counter_Additions['countRequirements']*2)
    
    return(result)
###############################################################################################################
def main(counter_Additions, counter_Deductions):
    password = 'PassWord02@39#'
    add_data = Additions(password) #calculating additions to socre
    deduction_data = Deductions(password) #calculating deductions to score
    score = add_data - deduction_data
    if score > 100:
        print('More than 100% ! Very Good!')
    else:
        print('Score: ',score,'%')

if __name__ == "__main__":
    main(counter_Additions, counter_Deductions)