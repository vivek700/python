
# rock   paper   scissor 

import random


def gamewin(c,y):
    if c==y:
        return "5"
    elif c=="r":
        if y=="p":
            return True
        elif y=="s":
            return False
    elif c=="p":
        if y=="r":
            return False
        elif y=="s":
            return True
    elif c=="s":
        if y=="r":
            return True
        elif y=="p":
            return False                                


print("Computer turn: Rock(r) or Paper(p) or Scissor(s) ?" )
m=random.randint(1,3)
if m==1:
    c="r"
elif m==2:
    c="p"
elif m==3:
    c="s"    
y=input("Your turn: Rock(r) or Paper(p) or Scissor(s) ?\n")

w=gamewin(c,y)
# print(w)
print("Computer chose: "+c)
print("You chose: "+ y)
# print(m)

if w==None:
    print("invalid entry")
elif w=="5":
    print("Tie")    
elif w==True:
    print("You win!")    
elif w== False:
    print("You lose!")    


