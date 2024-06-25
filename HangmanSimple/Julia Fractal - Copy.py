# modules
import random

# Welcome Message
name = input("Enter Your Name: ")
print("Good Luck ! ", name)

# choosing random word for guess from list.
words = ['rainbow' , 'computer' , 'science' , 'programming' ,
         'python' , 'mathematics' , 'player' , 'condition' ,
         'reverse' , 'water' , 'board' , 'geeks']

word = random.choice(words)
temp = word
guessed = "_ "*len(word)

print("Guess {} character word".format(len(word)))

# set difficulty
turns = 19 # set any number of turns

fails = 0

while turns > 0:
    print(guessed)
    guess = input("Guess a letter:")
    if guess in word:
        pass
    else:

        
##    failed = 0
##    for char in word:
##        if char in guesses:
##            print(char, end=" ")
##
##        else:
##            print("_")
##            failed += 1
##    if failed == 0:
##        print("You Win")
##        print("The word is: ", word)
##        break
##    print()
##    guess = input("guess a character:")
##    guesses += guess
##    if guess not in word:
##        turns -= 1
##        print("Wrong")        
##        print("You have", + turns, 'more guesses')
##        if turns == 0:
##            print("You Loose")
