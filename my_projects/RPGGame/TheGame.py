#!/usr/bin/python3

import random

player_name = input("What is your name, adventurer? ")

print(f"Welcome to the dungeon, {player_name}!")

health = 100
gold = 0
inventory = []

while True:
    print(f"\n{player_name}'s stats:")
    print(f"Health: {health}")
    print(f"Gold: {gold}")
    print(f"Inventory: {inventory}")

    choice = input("What would you like to do? [explore/battle/shop/quit] ").lower()

    if choice == "explore":
        print("You explore the dungeon and find a treasure chest!")
        loot = random.choice(["health potion", "gold", "sword", "armor"])
        print(f"You found: {loot}")
        if loot == "health potion":
            health += 20
            print(f"You drink the health potion and gain 20 health!")
        elif loot == "gold":
            gold += random.randint(1, 10)
            print(f"You found some gold!")
        elif loot == "sword":
            inventory.append("sword")
            print("You found a sword!")
        elif loot == "armor":
            inventory.append("armor")
            print("You found some armor!")

    elif choice == "battle":
        print("You encounter a monster!")
        monster_health = random.randint(50, 100)
        while monster_health > 0:
            print(f"Your health: {health}")
            print(f"Monster's health: {monster_health}")
            action = input("What would you like to do? [attack/run] ").lower()
            if action == "attack":
                damage = random.randint(10, 20)
                monster_health -= damage
                print(f"You attack the monster and deal {damage} damage!")
                if monster_health <= 0:
                    print("You defeated the monster!")
                    gold += random.randint(5, 15)
                    break
                else:
                    monster_damage = random.randint(5, 15)
                    health -= monster_damage
                    print(f"The monster attacks you and deals {monster_damage} damage!")
                    if health <= 0:
                        print("You have been defeated!")
                        quit()
            elif action == "run":
                print("You run away from the monster.")
                break

    elif choice == "shop":
        print("You arrive at a shop.")
        print("Health potion: 10 gold")
        print("Sword: 50 gold")
        print("Armor: 100 gold")
        item = input("What would you like to buy? ").lower()
        if item == "health potion":
            if gold >= 10:
                gold -= 10
                health += 20
                print("You bought a health potion!")
            else:
                print("You do not have enough gold.")
        elif item == "sword":
            if gold >= 50:
                gold -= 50
                inventory.append("sword")
                print("You bought a sword!")
            else:
                print("You do not have enough gold.")
        elif item == "armor":
            if gold >= 100:
                gold -= 100
                inventory.append("armor")
                print("You bought some armor!")
            else:
                print("You do not have enough gold.")

    elif choice == "quit":
        print("Thanks for playing!")
        quit()

    else:
        print("Invalid choice.")

