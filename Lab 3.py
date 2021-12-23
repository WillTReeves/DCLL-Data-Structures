from DCLL import DCLL
from stopwatch import Stopwatch
import random


def genlist(size):
    A = DCLL()
    for x in range(size):
        num = random.randint(-9,9)
        A.append(num)
    return A

def checkoff(fulllist):

    if fulllist.getlenth() != 1:
        tobepopped = []
        k = fulllist.index(0)
        k = k.get_item()
        length = fulllist.getlenth()
        
        if k == 0:
            tobepopped.append(0)

        elif k == 1 or k == -1:
            for x in range(length):
                tobepopped.append(x) 
                
        elif k < 0:
            for x in range(0,- length, k):
                tobepopped.append(x)

           
        else:
            for x in range(0,length, k): 
                tobepopped.append(x)
                
        
        for y in reversed(tobepopped):
            fulllist.pop(y)
            if len(tobepopped) == 0 or fulllist.getlenth() == 0 :
                break    
        
        if fulllist.getlenth() == 0 :
            exit()
        else:
            print(fulllist)
            checkoff(fulllist)

        
    



    

def main(size):
    startlist = genlist(size)
    print(startlist)
    checkoff(startlist)


main(25)