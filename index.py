import pprint

#lists to check in Ascii map
Upper = list(range(65,91))
Lower = list(range(97,123))
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
    #Consecutive Uppercase
    #Consecutive Lowercase
    counter_l=0
    counter_u=0
    for i in range(len(password)):
        checker_u = password[i-1].isupper() == password[i].isupper()
        checker_l = password[i-1].islower() == password[i].islower()
        if( (i>0) and (checker_u == password[i].isupper()) ):
            counter_u+=1
        elif( (i>0) and (checker_l == password[i].islower()) ):
            counter_l+=1
    print('Contador Mayusculas: ',counter_u-1,'\nContador Minusculas: ',counter_l-1)
    #Consecutive Numbers

    #Sequential Numbers
    #Sequentials Symbols

    #return result
    return 'temporal'
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

    add_data = Additions(password) #calculating additions to socre
    '''
    print('Score Additions: ', add_data)
    print('\n')
    print('Contadores almacenados en Additions: ', counter_Additions)
    '''
    deduction_data = Deductions(password) #calculating deductions to score

    #print('Deductions: ',deduction_data)
    #score = add_data - deduction_data

if __name__ == "__main__":
    main(counter_Additions, counter_Deductions)