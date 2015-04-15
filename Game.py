import random
opponent_health = 400;

player_health = 400;

player_name = ""

game_level = 0;

damage = 0;

player_action = 0

def calc_damage(action):
    if(action == 1):
        damage = random.randrange(20,40)
    if(action == 2):
        damage = random.randrange(30,50)
    if(action == 3):
        damage = random.randrange(10,100)
    return damage
    
def printScreen():
    global player_health
    global opponent_health
    print("Your Health : " , player_health)
    print("Opponent Health : " , opponent_health)
    print("********************************************************************")
    global player_action
    print("1. Poke")
    print("2. Smack")
    print("3. Kick")
    print("********************************************************************")
    player_action = eval(input("Choose your move"))

def startScreen():
    global player_name 
    player_name = input("What is your name?")

def main():
    global player_action
    global player_health
    global opponent_health
    startScreen()
    while (player_health > 0 and opponent_health > 0) :
        printScreen()
        opponent_health = opponent_health - calc_damage(player_action)
        opponent_action = random.randint(1,3)
        player_health -= calc_damage(opponent_action)
    if(player_health > 0):
        print("Congratulation, you won!")
    else:
        print("I am sorry.")

main()

