#reads random string with upper and lowercase letters 
#if we add other functions inside random.choice we can get other chars too

import random
def space(): 
    return chr(32)
def uppercase(): 
    return chr(random.randint(65, 90))
def lowercase(): 
    return chr(random.randint(97, 122))
def digits(): 
    return chr(random.randint(48, 57))
def chars():
    return random.choice(chr(random.randint(33,47))+chr(random.randint(58,64))+chr(random.randint(91,96))+chr(random.randint(123,126)))

def rand_str(n):
    str=''.join(random.choice(uppercase()+lowercase()) for i in range(n))
    return str

n=int(input())
print(rand_str(n))