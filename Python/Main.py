from enemy import Enemy

# Player Stats
playerHP = 20
playerAtk = 3

# enemys
gob1 = Enemy(7,2)

gob2 = Enemy(7,2)


# story start
print("""
You awake in a dark room with only the faint glow of torch light coming from the wall to your right.
You have your trusted sword and shield, but nothing else.
You grab the torch, and see a recket door to the left of the door.
""")

yes_no_answer = input("would you like to kick the door open? (y/n)) ")

if ("y" in yes_no_answer. lower()):
    print("You kick the door open")
elif ("n" in yes_no_answer.lower()):
    print("You wait 10 minutes and then decide to kick the door open anyways")
else:
    print("thank for playing")

print ("""You kick the door open and spot 2 goblins.
You startled the goblins and they spot you. You are now in combat.
""")

# until both goblins are dead, you will be in a fight
while ((gob1.hp >= 0 or gob2.hp >= 0)):
    print(f"current HP: {str(playerHP)}")

    # This is the player's attack
    player_attack_answer = input("Which goblin do you attack? (left/right) ")
    if ("l" in player_attack_answer.lower()):
        print(f"You attack the goblin on the left it take {str(playerAtk)} damage")
        gob1.hp -= playerAtk
    elif ("r" in player_attack_answer.lower()):
        print(f"You attack the goblin on the right it take {str(playerAtk)} damage")
        gob2.hp -= playerAtk
    else:
        print ("You missed your attack")

    # if goblin 1 has any health left it attacks.
    if (gob1.hp > 0):
        print(f"The goblin on the left attacks the you! and you take {str(gob1.atk)} damage")
        playerHP -= gob1.atk
    
    # if goblin 2 has any health left it attacks.
    if (gob2.hp > 0):
        print(f"The goblin on the right attacks the you! and you take {str(gob2.atk)} damage")
        playerHP -= gob2.atk

    if (playerHP <= 0):
        break

if (playerHP <= 0):
    print("You died!")
else:
    print("""You kill the goblins, but you are battered from the fight.
    You rummage through their possesions and find a health potion and drink it.
    """)