""" randomString(n) - generates random string with length n, and default parameters:
hasUpper=true hasLower=true hasDigit hasSpaces hasSpecial """
import random
def randomString(strlen, hasUpper = True, hasLower = True, hasDigit = False, hasSpecial = False, hasSpaces = False):
    data_set = """"""
    ascii = """ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()_+?></.,;: """
    if hasUpper:
        data_set += ascii[0:26]
    if hasLower:
        data_set += ascii[26:52]
    if hasSpaces:
        data_set += ascii[84]
    if hasDigit:
        data_set += ascii[52:62]
    if hasSpecial:
        data_set += ascii[62:84]
    word = """"""
    for i in range(strlen):
        index = random.randint(0, len(data_set)-1)
        word += data_set[index]
    
    return word
    
#print(randomString(20, hasSpaces=True))