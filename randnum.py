import random


# Extra Features: Try...Except code when y < 5

y = int(input("Numbers Possible: "))
if y >= 5:
    randInt = random.randint(0, y)
else:
    exit()
        

def guess_x():
        hearts = round(y/5)
        print(f"Guess x between 0 and {y}! You have {hearts} hearts!")
        x = int(input("Guess a number: "))
        

        while True:

                if x > randInt:
                    print(f"Lower than {x}")
                    x = int(input("Guess a number: "))
                    hearts -= 1
                    print(f"Hearts: {hearts}")
                    if hearts == 0:
                          print("Game Over.")
                          break
                elif x < randInt:
                    print(f"Higher than {x}")
                    x = int(input("Guess a number: "))
                    hearts -= 1
                    print(f"Hearts: {hearts}")
                    if hearts == 0:
                          print("Game Over.")
                          break
                else:
                    print("Correct!")
                    break
            
           
guess_x()
            

