from __future__ import print_function
import random

gun_ammo = 1000


grenade_ammo = 2


german_gunman_hp = 600

user_hp = 1000
luck = 0

german_sniper_hp = 600

damage = random.randint(100,250)
def get_damage():
    global damage
    damage = random.randint(100,250)



print ("Ehh.. Hi. You were hired to fight.")
print ("You can fight, right?")
print ("To get you registered here,")
print ("How would you liked to be called?")
user_name = raw_input()
print ("That... works, ",user_name)
print ("Here's a AK-47 with ",gun_ammo, " ammo")
print ("Here are a few grenades " ,grenade_ammo," to be exact")

print ("                   -syhyo-                        \n                 yMMMMMMMs                       \n                 :MMMMMMMMM.                      \n                NMMMMMMMMMy                      \n                NMMMMMMMNm/                      \n                 `.MMMMm:                        \n                 `yMMMMMMh::`               :o`  \n              ./oNMMMMMMMMMMMNs:      h` .omy:   \n            `dMMMMMMMMMMMMMMMMMMh     -mm+-       \n          `yMMMMMMMMMMMMMMMMMMMM+./sdNh:         \n          dMMMMMMMMMMMMMMMMMMMMMMMMm/            \n         sMMMMMMMMMMMMMMMMMMMMMMMM:+            \n         yMMMMMMMMMMMMMMMMMMMMMMMMMs.             \n       yMMMMMooMMMMMMMMMMMMMMMMMMMo              \n        mMMMMm-NMMMMMMMMMMMMMMMMMMM/             \n        .yMMMMMMMMMMMMMMMMMMMMhMMMMm`             \n         .sMMMMMMMMMMMMMMMMMMMysMdo`              \n      yNMMMNyNMMMMMMMMMMMMMMMMMMM+               \n      yMMMMs`sMMMMMMMMMMMMMMMMMMMd               \n      oMddsodMMMMMMMMMMMMMMMMMMMMN               \n             mMMMMMMMMMMMMMMMMM+:.               \n            :NNMMMMMMMMMMMMMMMMN                  \n            y+hMMMMMMMMMMMMMMMMN                  \n             mMMMMMMMh:MMMMMMMMh`                \n             MMMMMMMMM.dMMMMMMMM-                \n             hMMMMMMMh  MMMMMMMN                 \n             sMMMMMMMo   NMMMMMMN                \n             +MMMMMMM-   :MMMMMMM`                \n             :MMMMMMd     sMMMMMN`                \n            `NMMMMM:     /MMMMMy                 \n             `MMMMMm      dMMMMd                 \n             .MMMMM+       oMMMMM.                \n             oMMMMm        .MMMMM+                \n            sMMMMs         sMMMMd`               \n            .mMMMMh        sMMMMMs               \n            -MMMMMh         dMMMMMh               \n             hMMMh          -dMMMN-               \n            +MMM:           -MMMh                \n            `dMMN`           NMMN`               \n            yMMMM.           /MMMMo               \n          :dMMMNd.           :MMMMMd:             \n         /MMN+`              -oNMMMM.            \n          `                     ```              \n")


print ("Ehh... don't die?")
print ("Anyway, good luck.")

print ("\n")


print('Your HP: ', user_hp)
print("Opponent's HP: ", german_gunman_hp)
print('******************************************')

while(user_hp > 0) and (german_gunman_hp > 0):
    
    print('Your HP: ', user_hp)
    print("Opponent's HP: ", german_gunman_hp)
    print('******************************************')

    print('You gotta do what you gotta do, Do you:')
    print('1: Throw grenade')
    print('2: shoot AK-47')
    my_choice = int(raw_input())

    #Define the attack from you
    if my_choice == 2:
        gun_ammo = gun_ammo - 3
        get_damage()
        german_gunman_hp = german_gunman_hp - damage 
        print('You dealt',german_gunman_hp,"damage to your opponent")
        print('Your opponent lost',damage,'health!')

    if my_choice== 1:   
        #Define the grenade chance
        luck = random.randint(1,4) #Get a number between 1 and 4
        if luck == 1:
            grenade_ammo = grenade_ammo - 1
            get_damage()
            user_hp = user_hp - damage
            print ("You threw a grenade and  hit yourself, oops")
        else:
            grenade_ammo = grenade_ammo - 1
            get_damage()
            german_gunman_hp = german_gunman_hp - damage
            print ("You threw a grenade and hurt him/her (we gotta stay politically correct)")

    get_damage()
    user_hp = user_hp - damage 
    print('Your opponent dealt ',damage," damage to you")
    print('You lost ',damage,' health!')
    
if user_hp > 0:
    print('You win the fight!')
else:
    print('You lose the fight!')
print("*******************************")

print("Wild boss appears")

while(user_hp > 0) and (german_sniper_hp > 0):
    
    print('You are attacked by THE BOSS. Do you:')
    print('1: Throw grenade')
    print('2: shoot AK-47')
    my_choice = int(raw_input())

    #Define the attack from you
    if my_choice == 2:
        gun_ammo = gun_ammo - 3
        get_damage()
        german_sniper_hp = german_sniper_hp - damage 
        print('You dealt',german_sniper_hp,"damage to the THE BOSS")
        print('The BOSS lost',damage,'health!')

    if my_choice== 1:   
        #Define the grenade chance
        luck = random.randint(1,4) #Get a number between 1 and 4
        if luck == 1:
            grenade_ammo = grenade_ammo - 1
            get_damage()
            user_hp = user_hp - damage
            print ("You threw a grenade and  hit yourself, oops")
        else:
            grenade_ammo = grenade_ammo - 1
            get_damage()
            german_sniper_hp = german_sniper_hp - damage
            print ("You threw a grenade and hurt THE BOSS")

    get_damage()
    user_hp = user_hp - damage 
    print('THE BOSS dealt ',damage," damage to you")
    print('You lost ',damage,' health!')

       
    print('Your HP is', user_hp)
    print("BOSS's HP is", german_sniper_hp)
    print('******************************************')

if (user_hp > 0) and (german_sniper_hp < 0):
    print ("Huh.. You won. You can go home now.")





if (user_hp < 0) and (german_sniper_hp > 0):
    print ("You failed.")
