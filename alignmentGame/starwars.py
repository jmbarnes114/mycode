#!/usr/bin/env python3

print("Welcome to the D&D alignment game! Please answer the following questions to determine your Star Wars character's alignment.")

# initialize variables
import random

# Define the questions to determine the player's alignment
questions = [
    "Do you believe in following rules and traditions, even if they're inconvenient? (y/n) ",
    "Do you prioritize helping others, even at your own expense? (y/n) ",
    "Do you value honesty and integrity above all else? (y/n) ",
    "Do you believe that might makes right? (y/n) ",
    "Do you prefer to work alone, or as part of a team? (alone/team) "
]

# Define the possible alignments and their descriptions
alignments = {
    ("Lawful", "Good"): "The Noble Hero, a true Jedi and Light side user, Obi-Wan Kenobi",
    ("Lawful", "Neutral"): "The Lawful Guardian The fearless Bounty Hunter, Bobba Fett",
    ("Lawful", "Evil"): "The Tyrannical Ruler, you rule with an iron fist, Lord Vader",
    ("Neutral", "Good"): "The Carefree Adventurer, once a jedi, you turned away to find yourself, Ashoka Tano",
    ("Neutral", "Neutral"): "The Neutral Observer, as a droid, you dont have much say regarding alligiance, C3PO",
    ("Neutral", "Evil"): "The torn one, you are torn between the dark side and light side of the force, but you are a dark user, Kylo Ren",
    ("Chaotic", "Good"): "The Rebel with a Cause, Never out of malice or hate, you will go anywhere and work with anyone, Han Solo",
    ("Chaotic", "Neutral"): "The selfish one, once a jedi, turned sides based on your own beliefs, Count Dooku",
    ("Chaotic", "Evil"): "The Chaotic Villain, The evil Master of the dark side of the force, Empoer Palpatine"
}

# Initialize the variables to track the player's alignment
lawful = False
chaotic = False
good = False
evil = False

# Loop through the questions to determine the player's alignment
for question in questions:
    while True:
        answer = input(question)
        if answer.lower() == "y":
            lawful = True
            break
        elif answer.lower() == "n":
            chaotic = True
            break
        elif answer.lower() == "alone":
            evil = True
            break
        elif answer.lower() == "team":
            good = True
            break
        else:
            print("Invalid answer. Please enter 'y' or 'n', 'alone', or 'team'.")

# Determine the player's alignment based on their answers
alignment = []
if lawful:
    alignment.append("Lawful")
elif chaotic:
    alignment.append("Chaotic")
else:
    alignment.append("Neutral")

if good:
    alignment.append("Good")
elif evil:
    alignment.append("Evil")
else:
    alignment.append("Neutral")

# Print a fun description of the player's alignment
if tuple(alignment) in alignments:
    print("Congratulations, you are " + alignments[tuple(alignment)] + "!")
else:
    print("You are " + " ".join(alignment) + ". That's...interesting. Lets hope you agree and thanks for playimg!")

