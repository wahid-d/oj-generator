import random

# (0, 25) - upper, (26, 51) - lower, (52) - space, (53, 62) - digits, (63, 94) - special
def strings(length, hasUpper = True, hasLower = True, hasDigit = False, hasSpaces = False, hasSpecial = False):
    dataset = []
    newString = ""
    datalist = list(range(65, 91)) + list(range(97, 123)) + list(range(32, 33)) + list(range(48, 58)) + list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))

    if hasUpper:
        dataset += datalist[0:26]
    if hasLower:
        dataset += datalist[26:52]
    if hasSpaces:
        dataset += (datalist[52:53])
    if hasDigit:
        dataset += datalist[53:63]
    if hasSpecial:
        dataset += datalist[63:95]

    for i in range(length):
        newString += chr(dataset[random.randint(0, len(dataset) - 1)])
    return newString

# print(strings(20, hasSpecial=False, hasLower=True, hasSpaces=True, hasDigit=True,hasUpper=True))
