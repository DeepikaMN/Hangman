import random

file = open("random_words.txt" , "r")

words = file.read()
seperate_words = list(map(str, words.split()))

word = random.choice(seperate_words)

allowed_errors=10
guesses=[]
done=False

def draw(allowed_errors):
    if allowed_errors == 8:
            print("    \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
           
    elif allowed_errors == 7:
        
        print(  "   ___ \n"
                "  |      \n"
                "  |     \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
        
    elif allowed_errors == 6:

        print(  "   _____ \n"
                "  |      \n"
                "  |     \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
        
    elif allowed_errors == 5:
        
        print(  "   _____ \n"
                "  |     | \n"
                "  |     \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")

    elif allowed_errors == 4:
        
        print(  "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")

    elif allowed_errors == 3:
        
        print(  "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
    
    elif allowed_errors == 2:
        
        print(  "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     |\n"
                "  |     O\n"
                "  |      \n"
                "  |      \n"
                "__|__\n")

    elif allowed_errors == 1:
        
        print(  "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |     | \n"
                "  |       \n"
                "__|__\n")

    

    elif allowed_errors == 0:
        
        print(  "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n")

while not done:
    for letter in word:
        if letter.lower()in guesses:
            print(letter,end="")
            
        else:
            print("_ ",end="")
    print("")
    if(allowed_errors == 10):
        guess = input("Go ahead and guess your first letter: ")
    else:
        guess = input(f"Allowed guesses left {allowed_errors}, Next Guess: ")

    
    
    guesses.append(guess.lower())
    if guess.lower()not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:

        
            print(  "   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |     O \n"
                    "  |    /|\ \n"
                    "  |    / \ \n"
                    "__|__\n")
            break
    done = True
    draw(allowed_errors)
    for letter in word:
        if letter.lower() not in guesses:
            done=False

    
           
    
    
if done:
    print(f"\nYou found the word! It was {word}!\n")
    print(f"Your guesses were {guesses}\n")
else:
    print(f"\nGame Over! The word was {word}!\n")
    print(f"Your guesses were {guesses}\n")
