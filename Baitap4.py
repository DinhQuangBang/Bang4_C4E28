print ("Estimate this answer (exact calculation not needed):"
       " Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 54." 
       " What is the mean ?")

about = ["About 55", "About 65", "About 75", "About 85"]
for index, item in enumerate (about):
     print (index+1, item, sep= ". ")

while True:
    choice = int (input ("Your choice: "))

    if (choice == 1):
        print (":(")
        break
    elif (choice == 2):
        print ("Bingo !!!")
        break
    elif (choice == 3):
        print (":(")
        break
    elif (choice == 4):
        print (":(")
        break