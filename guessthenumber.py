import random

randomnum = random.randint(1,100)
# print(randomnum)

rn = random.randint(1,3)
if rn == 1 :
    greet = "Wow!"
elif rn == 2:
    greet = "Nice!"    
elif rn ==3:
    greet = "Awesome!"    

userGuess = None
guesses = 0

while userGuess != randomnum:
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if userGuess == randomnum:
        print(f"{greet} You guessed it right.")
    else:
        if userGuess<randomnum:
            print("You guessed it wrong! Enter a larger number")   
        else:
            print("You guessed it wrong! Enter a smaller number")     

print(f"You guessed the number in {guesses} guesses") 

with open("score.txt",'r') as f:
    highscore = int(f.read())

if highscore > guesses:
    print(f"You have just broken the highscore!")
    with open("score.txt",'w') as f:
        f.write(str(guesses))