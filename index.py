import pprint

#lists to check in Ascii map
Upper = list(range(65,91))
Lower = list(range(97,123))
Letters = Upper+Lower
Numbers = list(range(48,58))
Symbols = list(range(33,48))+list(range(58+65))+list(range(91,97))

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
    counter_u = 0
    counter_l = 0
    counter_n = 0
    for i in range(len(password)):
        #print(password[i].isnumeric())
        checker_u = password[i-1].isupper() == password[i].isupper()
        checker_l = password[i-1].islower() == password[i].islower()
        checker_n = password[i-1].isnumeric() == password[i].isnumeric()
        if( (i>0) and (checker_u == password[i].isupper()) ):#Consecutive Uppercase
            counter_u+=1
        elif( (i>0) and (checker_l == password[i].islower()) ):#Consecutive Lowercase
            counter_l+=1
        elif( (i>0) and (checker_n == password[i].isnumeric()) ):#Consecutive Numbers
            counter_n+=1
    #print('Contador Mayusculas: ',counter_u-1,'\nContador Minusculas: ',counter_l-1,'\nContador Numeros: ',counter_n-1)
    counter_Deductions['countConsUpp'] = counter_u-1
    counter_Deductions['countConsLow'] = counter_l-1
    counter_Deductions['countConsNum'] = counter_n-1
    #Sequential Letters
    #Sequential Numbers
    #Sequentials Symbols
    list_p = []
    count_ele_l = 1
    count_ele_n = 1
    count_ele_s = 1 
    keyboard_symbols = [64, 35, 36, 37, 94, 38, 42, 40]
    for i in range(len(password)):list_p.append(ord(password[i]))
    for i in range(len(password)):
        actual = list_p[i]
        #check if letter turn to lower
        if actual in Letters: 
            word1 = chr(actual).lower()
            actual = ord(word1)
            list_p[i] = actual
        #data 'actual' and 'list_p[i]' updated
        print(actual)
        #check to counters
        if(actual in Letters):
            if( (i>=2) and (list_p[i-1] == actual-1) ):
                count_ele_l+=1
        elif(actual in Numbers):
            if( (i>=2) and (list_p[i-1] == actual-1) ):
                count_ele_n+=1
        elif(actual in Symbols):
            if( (i>=2) and (list_p[i-1] == actual-1) ):
                count_ele_s+=1
    #print('Contador simbolos: ',count_ele_s-2,'\nContador letras: ',count_ele_l-2,'\nContador Numeros: ',count_ele_n-2)
    #storage
    counter_Deductions['countSeqLetters'] = count_ele_l
    counter_Deductions['countSeqNumbers'] = count_ele_n
    counter_Deductions['countSeqSymbols'] = count_ele_s

    resul = ( 
        counter_Deductions['countLettersOnly'] + 
        counter_Deductions['countNumbersOnly'] + 
        counter_Deductions['countRepChars'] + 
        (counter_Deductions['countConsUpp']*2) + 
        (counter_Deductions['countConsLow']*2) + 
        (counter_Deductions['countConsNum']*2) + 
        (counter_Deductions['countSeqLetters']*3) + 
        (counter_Deductions['countSeqNumbers']*3) + 
        (counter_Deductions['countSeqSymbols']*3) )

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
    '''
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(counter_Additions)
    '''
    
    return(result)



###############################################################################################################
def main(counter_Additions, counter_Deductions):
    password = "PAatata93@"
    #print('Password: ',password)
    add_data = Additions(password) #calculating additions to socre
    '''
    print('Score Additions: ', add_data)
    print('\n')
    print('Contadores almacenados en Additions: ', counter_Additions)
    '''
    deduction_data = Deductions(password) #calculating deductions to score

    #print('Deductions: ',deduction_data)
    score = add_data - deduction_data
    print('Score: ',score,'%')

if __name__ == "__main__":
    main(counter_Additions, counter_Deductions)