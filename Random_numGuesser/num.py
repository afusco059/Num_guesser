import random as r



def Num_guesser():
    x = r.randint(1,100)
    y = 5
    print("Hello")
    print(x)
    print(y)
    flag = True
    while flag:
        
        if (y >= x) :
            print("The Computer has guessed correctly")
            
        else :
            print("The computer has gotten the answer wrong")
            y = r.randint(1,100) 
            print(y)
            flag = False
            
  





Num_guesser()