# %%
import time
import sys


def type_text(text, delay=0.075):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def main():
    type_text('Welcome to this little adventure!')
    type_text(
        'You find yourself inside your cave during the Ice Age. Your tribe has not \neaten in weeks and is only days away from starving to death. You prepare to go \nhunting to find some food. In a dusty corner you find (1) a bow (with some \narrows) \U0001F3F9, (2) a sword \U0001F5E1, and (3) a simple leather armour \U0001F9E5. \nHowever, the amount of gear you can carry is limited and you can only take two \nthings with you at a time.')
    type_text('''Your options are:
    option 1: Bow (with arrows) \U0001F3F9 & Sword \U0001F5E1
    option 2: Sword \U0001F5E1 & Armour \U0001F9E5
    option 3: Bow (with arrows) \U0001F3F9 & Armour \U0001F9E5''')
    time.sleep(1)


def decision1():
    while True:
        decision1 = input('Which option are you choosing?')
        time.sleep(1)

        if decision1 == 'option 1':
            type_text(
                'You are packing both bow \U0001F3F9 and sword \U0001F5E1. You kiss your mother goodbye and \nhead into the forest heavily armed.')
            time.sleep(1)
            break
        elif decision1 == 'option 2':
            type_text(
                'You protect yourself with the simple armour \U0001F9E5 and grab the sword \U0001F5E1. \nYou kiss you mother goodbye and head into the forest.')
            time.sleep(1)
            break
        elif decision1 == 'option 3':
            type_text(
                'You protect yourself with the simple armour \U0001F9E5 and grab bow and arrow \U0001F3F9. \nYou kiss your mother goodbye and head into the forest.')
            time.sleep(1)
            break
        elif decision1 == 'help':
            print('''You can type:
            "option 1" for Bow (with arrows) \U0001F3F9 & Sword \U0001F5E1
            "option 2" for Sword \U0001F5E1 & Armour \U0001F9E5
            "option 3" for Bow (with arrows) \U0001F3F9 & Armour \U0001F9E5''')
            time.sleep(1)
        else:
            print('Unknown command. Type "help" for help.')
            time.sleep(1)


print('Warning! Explicit content ahead. You must be 18 years old to play this game.')
time.sleep(2)
while True:
    input0 = input('Enter your age.')
    try:
        AGE = int(
            input0)  # AGE as a constant (sadly it must be defined within this step of the code and cannot be put at the top of the code)

        if AGE < 0:
            print('Your age cannot be negative.')
            time.sleep(1)
            continue

        if AGE < 18:
            print('You are to young to continue. Make sure you are 18 years old to play this game.')
            time.sleep(1)
            continue

        if AGE >= 18:
            type_text('You have successfully verified your age. Type "start" to start the game!\n')
            break

    except ValueError:
        print('Your age is usually a number.')
        time.sleep(1)

while True:
    input1 = input('Type "start" to start game.')
    time.sleep(1)

    if input1 == 'start':
        break
    elif input1 == 'help':
        print('''You can type:
        "start" to start game''')
    else:
        print('Unknown command. Type "help" for help.')

    time.sleep(1)

print('---------------------GAME START---------------------')

# beginning of code execution from functions
main()

decision1()

type_text(
    '\nShortly after you encounter a huge woolly mammoth \U0001F9A3. You decide not to disturb the \nanimal as it is much stronger than you are. However, as you move backwards you step on a stick \nand break it. The mammoth instantly notices you and charges at you.\n')
time.sleep(1)

while True:
    decision2 = input('You can "flee" \U0001F4A8 or "fight" \U0001F4A5. What are you doing?')
    time.sleep(1)

    if decision2 == 'flee':
        scream1 = input('What do you want to scream while fleeing?')
        if decision1 == 'option 1':
            type_text(
                '\U0001F4A8 You decide to live to fight another day, yelling "' + scream1 + '". You are fast enough to get away \nas you quickly drop your gear. You return home safely without food to provide your tribe with. Although \nyou survived the encounter, you have failed to feed your people.')
            time.sleep(1)
        elif decision1 == 'option 2':
            type_text(
                '\U0001F4A8 As you flee, the weight of the armour slows you down. As you desperately yell "' + scream1 + '", the \nmammoth catches up with you, and tramples you to death. Your body will never be found.')
            time.sleep(1)
        elif decision1 == 'option 3':
            type_text(
                '\U0001F4A8 As you flee, the weight of the armour slows you down. As you desperately yell "' + scream1 + '", the \nmammoth catches up with you, and tramples you to death. Your body will never be found.')
            time.sleep(1)
        break
    if decision2 == 'fight':
        scream2 = input('What do you want to scream for battle?')
        if decision1 == 'option 1':
            type_text(
                '\U0001F4A5 You face the mammoth and grab your bow. To frighten the beast you yell "' + scream2 + '" as loud as you can. \nSince you are a great archer, you hit the animal multiple times. It drops before you, unable \nto reach you in time. You use your sword to finish it off. You have provided your tribe with \nenough food for generations, so that they can survive and will eventually become our ancestors.')
            time.sleep(1)
        elif decision1 == 'option 2':
            type_text(
                '\U0001F4A8 As you charge into battle with your sword drawn you loudly scream "' + scream2 + '" to frighten the beast. \nAs the mammoth hits you, the armour holds off enough damage for you to execute one powerful \nstrike with your sword. The mammoth drops dead, but sadly you succumb to your wounds. \nHaving heard your battle scream, your tribe members will find your body as well as the beast you have so heroically slain. \nThey will honour your sacrifice for centuries to come.')
            time.sleep(1)
        elif decision1 == 'option 3':
            type_text(
                '\U0001F4A5 You face the mammoth and grab your bow. To frighten the beast you yell "' + scream2 + '" as loud as you can. \nSince you are a great archer, you hit the animal multiple times. It drops before you, \nunable to reach you in time. You have provided your tribe with enough food for generations, \nso that they can survive and will eventually become our ancestors.')
            time.sleep(1)
        break
    if decision2 == 'help':
        print('''You can type:
           "flee" to flee \U0001F4A8
           "fight" to fight \U0001F4A8''')
        time.sleep(1)
    else:
        print('Unknown command. Type "help" for help.')
        time.sleep(1)

type_text('----------------END OF GAME------------------')
# %%
