import modules


def differentiation(psswd, length):
    # Uppercase, Lowercase, Number or Symbol ?
    for element in psswd:
        ascii_element = ord(element)
        if ascii_element in modules.Upper:
            modules.counter_Additions["countUpper"] += 1
        elif ascii_element in modules.Lower:
            modules.counter_Additions["countLower"] += 1
        elif ascii_element in modules.Numbers:
            modules.counter_Additions["countNumber"] += 1
        elif ascii_element in modules.Symbols:
            modules.counter_Additions["countSymbols"] += 1

        # Any element that is not first or last
        if (psswd.index(element) != 0 and psswd.index(element) != length-1) and (ascii_element in modules.Middle):
            modules.counter_Additions["countMiddle"] += 1


def requirements():
    # Are requirements done?
    for key in modules.counter_Additions:
        if (modules.counter_Additions[key] > 0) and (key != 'countMiddle') and (key != 'countRequirements'):
            modules.counter_Additions['countRequirements'] += 1

# Addition methods


def Additions(psswd, length):
    differentiation(psswd, length)
    requirements()

    # Return additions counter
    result = (modules.counter_Additions['countSize']*4) +\
        ((length-modules.counter_Additions['countUpper'])*2) +\
        ((length-modules.counter_Additions['countLower'])*2) +\
        (modules.counter_Additions['countNumber']*4) +\
        (modules.counter_Additions['countSymbols']*6) +\
        (modules.counter_Additions['countMiddle']*2) +\
        (modules.counter_Additions['countRequirements']*2)
    return result
