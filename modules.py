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
