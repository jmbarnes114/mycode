#!/usr/bin/env python3

print("Welcome to the D&D alignment game! Please answer the following questions to determine your Star Wars character's alignment.")

# initialize variables
lawful = False
chaotic = False
good = False
evil = False

# ask questions to determine character's alignment
while True:
    answer = input("Do you believe in following rules and traditions, even if they're inconvenient? (y/n) ")
    if answer.lower() == "y":
        lawful = True
        break
    elif answer.lower() == "n":
        chaotic = True
        break
    else:
        print("Invalid answer. Please enter 'y' or 'n'.")

while True:
    answer = input("Do you prioritize helping others, even at your own expense? (y/n) ")
    if answer.lower() == "y":
        good = True
        break
    elif answer.lower() == "n":
        evil = True
        break
    else:
        print("Invalid answer. Please enter 'y' or 'n'.")

# determine character's alignment based on answers
if lawful and good:
    print("You are Lawful Good! A true Jedi Obi-Wan Kenobi")
elif lawful and evil:
    print("You are Lawful Evil! The fearsome, Lord Vader")
elif chaotic and good:
    print("You are Chaotic Good! Never tell me the odds, Han Solo")
elif chaotic and evil:
    print("You are Chaotic Evil! Corrupted by the dark side, Emperor palpatine")
elif lawful:
    print("You are Lawful Neutral. Now get your bounty Bobba Fett")
elif chaotic:
    print("You are Chaotic Neutral. Once a Jedi, turned to another side because of your beliefs, Count Dooku")
elif good:
    print("You are Neutral Good. Once a jedi, but ultimately turned away, Ashoka Tano")
elif evil:
    print("You are Neutral Evil. You are torn between the force but rest on the dark side, Kylo Ren")
else:
    print("You are True Neutral. A droid who doesnt have much say regarding alliances, C3PO")

