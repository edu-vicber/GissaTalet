import random
namn = input("Vad heter du?")
print("Hej", namn ,"välkommen till spelet!")
randomnumber = random.randint(1,10)
attempts = 0
for i in range(3):
    gissa = int(input("Gissa ett tal mellan 1-10!"))
    attempts += 1
    if gissa == randomnumber:
        print("Rätt!")
        break
    elif attempts < 3:
        print("fel försök igen!")
    else:
        print("Du förlora, nummret var: ", randomnumber)
 