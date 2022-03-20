"""
    Created by Wallee#8314 / Red-exe-Engineer
    Simple Words Per Minute version 1.1
"""

# Imports
import random
from time import time
from os import system

# Convert a string of words into a number, make sure if it is less then 9 to add a 0
def str2int(text):

    # See if the number of words is less the 9
    if len(text.split(" ")) < 10:

        # Convert text into a string of it's length with a 0 at the start
        text = "0" + str(len(text.split(" ")))
    
    # Else the number is greater than 9
    else:

        # Convert text into a string of it's length
        text = str(len(text.split(" ")))

    # Return text
    return(text)

# Convert numbers into strings that start with 0 if it is less than 10
def int2str(number):

    # Check if number is less than 10
    if number < 10:

        # assign "0" pluss the string of number to number 
        number = "0" + str(number)

    # Else number is not less than 10
    else:

        # Assign the string of number to number
        number = str(number)

    # Return number
    return(number)

# Say text
def say(text):

    # In case of internet troubles
    try:

        # Use the Google Text To Speech module to convert text into sound
        voice = gTTS(text=text, lang="en")

        # Save the sound to a temp file
        voice.save("temp.mp3")

        # Use the Playsound module to play the temp file
        playsound("temp.mp3")

        # Delete the temp file
        system("rm temp.mp3")

    # Prevent an error
    except Exception as error:

        # Print the problem
        input(error)

# Clean the screen
system("clear")

# Define a useTTs variable
useTTs = ""

# Repeat until useTTs is either y, n, yes, or no
while not useTTs.lower() in ["y", "n", "yes", "no"]:

    # Get user input and assign it to useTTs
    useTTs = input("Say text as well as print? (Requires gTTS and Playsound) [y/n] ")

# Check if useTTs is a yes
if useTTs[0].lower() == "y":

    # Set use TTs to True for ease of code
    useTTs = True

    # Import some more modules
    from gtts import gTTS
    from playsound import playsound
    
    # Tell the user some info they already know
    say("Voice is enabled")

# Else useTTs is not a yes
else:

    # Set useTTs to False
    useTTs = False

# Clear the screen
system("clear")

# Credit the creator who is writting this comment :p
print("Simple WPM by Wallee / Red-exe-Engineer")

# Check is useTTs is enabled
if useTTs:

    # Say the credits
    say("Simple words per minute by Wallee slash Red-exe-Engineer")

# If useTTs is not enabled
else:

    # Wait for user input
    input()

# Clear the screen
system("clear")

# Open the file containing all the words
with open("1-1000.txt", "r") as file:

    # Extract the file's lines
    lines = file.readlines()

# Repeat forever
while True:

    # Assign a blank string to words
    words = ""

    # Repeat a ranfom number of times from 2 to 9
    for word in range(1, random.randint(2, 9)):

        # Assign words to itself pluss a random word
        words = words + lines[random.randint(0, len(lines)-1)].replace("\n", " ")

    # Remove the extra space
    words = words[:-1]

    # Check if useTTs is enabled
    if useTTs:

        # Say the words
        say(words)

    # Clear the screen
    system("clear")

    # Print the words
    print("< " + words)

    # Set a start time for later use
    startTime = time()

    # Get user input and assign it to answear
    answear = input("> ")

    # Get the end time for later use
    endTime = time()

    # Set score to 0
    score = 0

     # Check if the answear is equal to words
    if answear == words:

        # Tell the user they have done well
        print("\nCorrect!", end="")

        # Check if useTTs is enabled
        if useTTs:

            # Say the user is correct
            say("Correct")

    # If answear isn't equal to words
    else:

        # Print failed, new line x2, words, new line, answear
        print("\nOof\n\n" + words + "\n" + answear)

        # Repeat the max number of times between the length of words and answear
        for letter in range(0, max(len(words), len(answear))):

            # Try something that has a "small" chance of causing an error
            try:

                # Check if the index letter of ansear is equal to index letter of words
                if answear[letter] == words[letter]:

                    # Print a space and no new line
                    print(" ", end="")
                else:

                    # Print a ^ and no new line
                    print("^", end="")

                    # Increace score
                    score += 1

            # May be cased by a index error
            except:

                # Print a ^ and no new line
                print("^", end="")

                # Increace score
                score += 1

        # Check if useTTs is enabled
        if useTTs:

            # Say failed
            say("Oof")

    # Set rightWords to the length of words split by spaces
    rightWords = len(words.split(" "))

    # Repeat the value rightWords 
    for index in range(rightWords):

        # Try something
        try:

            # Check if each word of the answear isn't the same as each word as words
            if not words.split(" ")[index] == answear.split(" ")[index]:

                # Subtract 1 from rightWords
                rightWords -= 1

        # May be caused by an index error
        except:

            # Subtract 1 from rightWords
            rightWords -= 1

    # Check  if rightWords is less the 9
    if rightWords < 9:

        # Assign "0" pluss the string of rightWords to rightWords
        rightWords = "0" + str(rightWords)

    # Else rightWords is greater than 9
    else:

        # Assign the string of rightWords to rightWords
        rightWords = str(rightWords)

    # Print some new lines and the word statistics
    print("\n\n ~Statistics~\n")

    # Print some statistics using maths, def not too lazy to comment all this
    print("Time:     " + str(endTime - startTime)[:7] + " seconds!")
    print("Words:    " + rightWords            + " / " + str2int(words)        + " | " + str(100       * (int(rightWords) / int(str2int(words))))[:6] + "%")
    #print("Letters:  " + int2str(len(answear)) + " / " + int2str((len(words))) + " | " + str(100       * (len(answear)    / len(words)))[:6]          + "%") # This had very little use, uncomment if you want to use it
    print("Mistakes: " + int2str(score)                 + " / " + int2str(len(words))   + " | " + str(100 - 100 * (int(score)      / int(len(words))))[:6]     + "%")

    # Wait for and check if input is equal to q, also telling to user how to quit
    if input("\n\n Q to exit ").lower() == "q":

        # Print a thank you
        print("\nThank you for using my program")

        # Check if useTTs is enabled
        if useTTs:

            # Say thank you
            say("Thank you for using my program")

        # Else useTTs is not enabled
        else:

            # Wait for user input
            input("")

        # Clear the screen
        system("clear")

        # Exit the program
        exit()

# Wow, you have read more then the first few lines of code :p
