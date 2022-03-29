import random
# shake Water Gun or Rock Paper Scissors

def gameWin(Comp, you):
    # If two value are equal , delcare a tie!
    if comp == you:
        return None
    # Check for all possibilities when computer choose s   
    elif comp =='s':
        if you=='w':
            return False
        elif you =='g':
            return True  
    # Check for all possibilities when computer choose w              
    elif comp =='w':
        if you=='g':
            return False
        elif you =='s':
            return True 
    # Check for all possibilities when computer choose g               
    elif comp =='w':
        if you=='g':
            return False
        elif you =='s':
            return True              



print("Comp Turn : Snake(s) Water(w)  or Gun(g)?")
randNo = random.randint(1,3)


print(randNo)
if randNo == 1:
    comp  = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'        



you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)


print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
     print("You Lose!")