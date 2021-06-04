import modules


def only_letters(psswd):
    # Only letters ?
    if(modules.counter_Additions["countNumber"] == 0 and modules.counter_Additions["countSymbols"] == 0 and modules.counter_Additions["countMiddle"] == 0):
        modules.counter_Deductions["countLettersOnly"] = len(psswd)


def only_numbers(psswd):
    # Only numbers ?
    if(modules.counter_Additions["countUpper"] == 0 and modules.counter_Additions["countLower"] == 0 and modules.counter_Additions["countLower"] == 0):
        modules.counter_Deductions["countNumbersOnly"] = len(psswd)


def repeated(psswd):
    # Repeated characters
    rep_char = 0
    for elem in modules.alphabet:
        counter = psswd.count(elem)
        if(counter > 1):
            rep_char += counter
    modules.counter_Deductions['countRepChars'] = rep_char


def consecutives(psswd):
    # Consecutive Uppercases, Lowercases, Numbers
    for i in range(len(psswd)):
        if(i > 0):
            if(psswd[i].isupper() and psswd[i-1].isupper()):
                modules.counter_Deductions['countConsUpp'] += 1
            elif(psswd[i].islower() and psswd[i-1].islower()):
                modules.counter_Deductions['countConsLow'] += 1
            elif(psswd[i].isnumeric() and psswd[i-1].isnumeric()):
                modules.counter_Deductions['countConsNum'] += 1

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
            if (order in modules.Lower):
                modules.counter_Deductions['countSeqLetters'] += 1
            elif (order in modules.Numbers):
                modules.counter_Deductions['countSeqNumbers'] += 1
            elif (order in modules.Symbols):
                modules.counter_Deductions['countSeqSymbols'] += 1


def Deductions(psswd):
    only_letters(psswd)
    only_numbers(psswd)
    repeated(psswd)
    consecutives(psswd)
    sequentials(psswd)

    result = modules.counter_Deductions["countLettersOnly"] + \
        modules.counter_Deductions["countNumbersOnly"] + \
        modules.counter_Deductions['countRepChars'] + \
        modules.counter_Deductions['countConsUpp']*2 + \
        modules.counter_Deductions['countConsLow']*2 + \
        modules.counter_Deductions['countConsNum']*2 + \
        modules.counter_Deductions['countSeqLetters']*3 + \
        modules.counter_Deductions['countSeqNumbers']*3 + \
        modules.counter_Deductions['countSeqSymbols']*3

    return result
