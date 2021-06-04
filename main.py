
global alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# counters
countersArray = [
    ['countSize',       'countUpper',      'countLower',        'countNumber',
     'countSymbols',    'countMiddle',     'countRequirements'],
    ['countLettersOnly', 'countNumbersOnly', 'countRepChars',     'countConsUpp', 'countConsLow',
     'countConsNum',    'countSeqLetters', 'countSeqNumbers',   'countSeqSymbols']
]
# Dictionaries(sorting countersArray's elements as dictionaries to better interaction)
counter_Additions = dict.fromkeys(countersArray[0], 0)
counter_Deductions = dict.fromkeys(countersArray[1], 0)

# print('INITIAL STATE OF COUNTERS \n',
#       counter_Additions, '\n', counter_Deductions)

Upper = list(range(65, 91))
Lower = list(range(97, 123))
Letters = Upper+Lower
Numbers = list(range(48, 58))
Symbols = list(range(33, 48))+list(range(58, 65))+list(range(91, 97))
Middle = list(range(33, 48))+list(range(48, 58)) + \
    list(range(58, 65))+list(range(91, 97))+list(range(123, 255))


def differentiation(psswd, length):
    # Uppercase, Lowercase, Number or Symbol ?
    for element in psswd:
        ascii_element = ord(element)
        if ascii_element in Upper:
            counter_Additions["countUpper"] += 1
        elif ascii_element in Lower:
            counter_Additions["countLower"] += 1
        elif ascii_element in Numbers:
            counter_Additions["countNumber"] += 1
        elif ascii_element in Symbols:
            counter_Additions["countSymbols"] += 1

        # Any element that is not first or last
        if (psswd.index(element) != 0 and psswd.index(element) != length-1) and (ascii_element in Middle):
            counter_Additions["countMiddle"] += 1


def requirements():
    # Are requirements done?
    for key in counter_Additions:
        if (counter_Additions[key] > 0) and (key != 'countMiddle') and (key != 'countRequirements'):
            counter_Additions['countRequirements'] += 1

# Addition methods


def Additions(psswd, length):
    differentiation(psswd, length)
    requirements()

    # Return additions counter
    result = (counter_Additions['countSize']*4) +\
        ((length-counter_Additions['countUpper'])*2) +\
        ((length-counter_Additions['countLower'])*2) +\
        (counter_Additions['countNumber']*4) +\
        (counter_Additions['countSymbols']*6) +\
        (counter_Additions['countMiddle']*2) +\
        (counter_Additions['countRequirements']*2)
    return result

# repeated chars


def only_letters(psswd):
    # Only letters ?
    if(counter_Additions["countNumber"] == 0 and counter_Additions["countSymbols"] == 0 and counter_Additions["countMiddle"] == 0):
        counter_Deductions["countLettersOnly"] = len(psswd)


def only_numbers(psswd):
    # Only numbers ?
    if(counter_Additions["countUpper"] == 0 and counter_Additions["countLower"] == 0 and counter_Additions["countLower"] == 0):
        counter_Deductions["countNumbersOnly"] = len(psswd)


def repeated(psswd):
    # Repeated characters
    rep_char = 0
    for elem in alphabet:
        counter = psswd.count(elem)
        if(counter > 1):
            rep_char += counter
    counter_Deductions['countRepChars'] = rep_char


def consecutives(psswd):
    # Consecutive Uppercases, Lowercases, Numbers
    for i in range(len(psswd)):
        if(i > 0):
            if(psswd[i].isupper() and psswd[i-1].isupper()):
                counter_Deductions['countConsUpp'] += 1
            elif(psswd[i].islower() and psswd[i-1].islower()):
                counter_Deductions['countConsLow'] += 1
            elif(psswd[i].isnumeric() and psswd[i-1].isnumeric()):
                counter_Deductions['countConsNum'] += 1

    # print("CONSECUTIVES\n", countU, '\n', countL, '\n', countN)


def sequentials(psswd):
    # Sequential Letters, Numbers,  Symbols
    stack = []

    for element in range(0, len(psswd)):
        order = ord(psswd[element].lower())
        if (len(stack) == 0):
            stack.append(order)
        else:
            if (stack[-1]+1 == order):
                stack.append(order)
            else:
                stack = []
                stack.append(order)

        if (len(stack) >= 3):
            if (order in Lower):
                counter_Deductions['countSeqLetters'] += 1
            elif (order in Numbers):
                counter_Deductions['countSeqNumbers'] += 1
            elif (order in Symbols):
                counter_Deductions['countSeqSymbols'] += 1


def Deductions(psswd):
    only_letters(psswd)
    only_numbers(psswd)
    repeated(psswd)
    consecutives(psswd)
    sequentials(psswd)

    result = counter_Deductions["countLettersOnly"] + \
        counter_Deductions["countNumbersOnly"] + \
        counter_Deductions['countRepChars'] + \
        counter_Deductions['countConsUpp']*2 + \
        counter_Deductions['countConsLow']*2 + \
        counter_Deductions['countConsNum']*2 + \
        counter_Deductions['countSeqLetters']*3 + \
        counter_Deductions['countSeqNumbers']*3 + \
        counter_Deductions['countSeqSymbols']*3

    return result


def main():
    # password model
    password = "Patatabc93@"

    password_length = len(password)

    if(password_length > 8):
        counter_Additions['countSize'] += password_length
        addition = Additions(password, password_length)  # returns % addition
        deduction = Deductions(password)  # returns % deductions
        print("Score: ", addition - deduction, "%")

    else:
        print("Password must be larger or equeal than 8 characters")


if __name__ == "__main__":
    main()
