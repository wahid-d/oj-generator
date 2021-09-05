import random
def randomString(strlen, hasUpper = True, hasLower = True, hasDigit = True, hasSpecial = True, hasSpaces = True):
    data_set = """"""
    if hasUpper:
        data_set += chr(random.randint(65, 90))
    if hasLower:
        data_set += chr(random.randint(97, 122))
    if hasSpaces:
        data_set += chr(32)
    if hasDigit:
        data_set += chr(random.randint(48, 57))
    if hasSpecial:
        data_set += chr(random.randint(91, 96))
    word = """"""
    for i in range(strlen):
        index = random.randint(0, len(data_set)-1)
        word += data_set[index]

    return word

