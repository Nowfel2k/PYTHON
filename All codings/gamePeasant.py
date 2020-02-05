# 1300's simulator!
from termcolor import colored
from os import system, name
import random

global piety
global bruh

bruh = 'alive'
piety = 0
record = 0

family = random.randint(3, 5)
chance = 0

endings = []


def cprint(text, color):
    print(colored(text, color))


def familydie():
    global family
    if family == 0:
        cprint('Oh no! All of your family members have died. You are now sad and very alone.', 'cyan')


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def intro():
    cprint(
        "Welcome to the 1300's! You are a peasant who works on a farm. If you die, you lose. You cannot win. Make choices to survive as long as possible. \nPress enter to begin.",
        'cyan')


def familysick():
    global family
    global chance
    global piety
    cprint(
        'A family member has caught the plague. Do do you wish to treat them? You can hire a doctor [1], pray [2], or leave them to die [3]',
        'cyan')
    choice = input()
    clear()
    if choice == '1':
        cprint('You have hired a doctor from the local apothecary.', 'cyan')
        hmmm = random.randint(1, 4)

        piety += -1
        if hmmm == 1:
            cprint('Miraculously, your family member was saved! Press enter to continue.', 'cyan')
            input()
            clear()
        else:
            cprint('Unfortunately, your family member died. Press enter to continue.', 'cyan')
            family += -1
            chance += 1
            familydie()
            input()
            clear()
    elif choice == '2':
        cprint('You have decided to pray to God.', 'cyan')
        piety += 1
        hmm = random.randint(1, 6)
        if hmm == 1:
            cprint('Miraculously, your family member was saved! Press enter to continue.', 'cyan')
            input()
            clear()
        else:
            cprint("Unfortunately, you weren't holy enough and your family member died. Press enter to continue.",
                   'cyan')
            chance += 1
            family -= 1
            familydie()
            input()
            clear()

    else:
        cprint('You have left them to die. Press enter to continue', 'cyan')
        family -= 1
        chance += 1
        familydie()
        input()
        clear()


def selfsick():
    global endings
    global chance
    if chance <= 0:
        chance = 1
    hmm = random.randint(1, chance + 1)
    if hmm != 1:
        options = ['hire a doctor.', 'hire a doctor.', 'pray.', 'pray.', 'leave you to die.']
        h = random.randint(0, 4)
        if family > 0:
            cprint('Oh no! You have the plague. Your family decided to ' + options[h], 'cyan')
        else:
            h = 4
            cprint('Oh no! You have the plague but you have no family to care for you.', 'cyan')
            if not 'Forever alone' in endings:
                endings.append('Forever alone')

        if h == 4:
            cprint('Oh dear. You have died. Press enter to continue.', 'cyan')
            input()
            clear()
            if family > 0 and not 'Left to die' in endings:
                endings.append('Left to die')
            return ('dead')
        else:
            hm = random.randint(1, 4)
            if hm == 1:
                cprint('Miraculously, you lived! Press enter to continue.', 'cyan')
                input()
                clear()
            else:
                cprint('Oh dear. Your family could not save you and you have died. Press enter to continue.', 'cyan')
                input()
                clear()
                if not 'Failed cure' in endings:
                    endings.append('Failed cure')
                return ('dead')
    else:
        cprint('Nothing happened today. Press enter to continue.', 'cyan')
        input()
        clear()


def burglary():
    global endings
    global family
    cprint('Oh no! Your house is being burgled. Do you fight [1] or give up [2]? ', 'cyan')
    choice = input()
    if choice == '1':
        h = random.randint(0, 2)
        if h == 0:
            cprint(
                'You decided to fight but lost. The burglar ran away with some of your money. Press enter to continue.',
                'cyan')
            input()
            clear()
        elif h == 1:
            cprint('You decided to fight and were killed in the process. Press enter to continue.', 'cyan')
            if not 'Home invasion' in endings:
                endings.append('Home invasion')
            input()
            clear()
            return ('dead')
        else:
            cprint('You decided to fight and won! Press enter to continue.', 'cyan')
            input()
            clear()
    else:
        h = random.randint(0, 2)
        if h == 0:
            cprint('You dedcided to give up and surrender, but you were killed anyways. Press enter to continue.',
                   'cyan')
            if not 'Surrender' in endings:
                endings.append('Surrender')
            input()
            clear()
            return ('dead')
        else:
            cprint('You decided to surrender and the burglar took a lot of your stuff. Press enter to continue.',
                   'cyan')
            input()
            clear()


def flagellants():
    global chance
    cprint(
        'The flagellants have come to town! They beat themselves mercilessly to appease God in the town square. Press enter to continue.',
        'cyan')
    chance += 1
    input()
    clear()


def cleaners():
    global chance
    global endings
    h = random.randint(1, 3)
    if h != 1:
        cprint(
            "The Baron's workers have come to clean the streets of dead bodies and human waste. Yay! Press enter to continue.",
            'cyan')
        input()
        clear()
        chance -= 1
    else:
        cprint(
            "The Baron's workers came to clean up dead bodies and waste, and while you were sleeping they took you by mistake. Press enter to continue.",
            'cyan')
        input()
        clear()
        if not 'Lazy workers' in endings:
            endings.append('Lazy workers')
        return ('dead')


def herbs():
    global chance
    cprint(
        'You decided to go out and buy some herbs to protect you from the plague. At the apothecary, you see a some bottles with leaves and grab a few.',
        'cyan')
    m = random.randint(0, 3)
    if m == 0:
        cprint(
            'Unfortunately, you cannot read and pick a bottle named "Hemlock". You die after consuming it. Press enter to continue.',
            'cyan')
        input()
        clear()
        if not 'Home doctor' in endings:
            endings.append('Home doctor')
        return ('dead')
    else:
        cprint(
            'You cannot read and pick a nice smelling bottle of leaves. It may not do much, but now the house smells better.',
            'cyan')
        h = random.randint(0, 2)
        chance -= h
        input()
        clear()


def blessing():
    global endings
    h = random.randint(0, 3)
    if h == 0:
        cprint('You were found to be a heretic and were executed. Press enter to continue', 'cyan')
        input()
        clear()
        if not 'Heresy' in endings:
            endings.append('Heresy')
        return ('dead')
    else:
        cprint('A bishop has come to town to bless it. Press enter to continue.', 'cyan')
        input()
        clear()


def witches():
    global endings
    cprint('The village has decided to hold a witch hunt.', 'cyan')
    h = random.randint(1, 3)
    if piety > 0 and h == 1:
        h = 2
    if h == 1:
        cprint('You were found guilty of witchcraft and were burned at the stake. Press enter to continue.', 'cyan')
        input()
        clear()
        if not 'Kentucky Fried Witch' in endings:
            endings.append('Kentucky Fried Witch')
        return ('dead')
    else:
        cprint('A few villagers were burnt to death on account of their witchcraft. Press enter to continue.', 'cyan')
        input()
        clear()


def fight():
    global endings
    cprint('You got into a fight!', 'cyan')
    h = random.randint(1, 5)
    if h == 1:
        cprint('You lost the fight and went home bruised. Press enter to continue.', 'cyan')
        input()
        clear()
    elif h == 2:
        cprint('You died in the fight. Press enter to continue.', 'cyan')
        input()
        clear()
        if not 'To Valhalla' in endings:
            endings.append('To Valhalla')
        return ('dead')
    else:
        cprint('You won the fight and came home victorious. Press enter to continue.', 'cyan')
        input()
        clear()


def event():
    ID = random.randint(1, 10)
    if ID == 1:
        if family > 0:
            familysick()
        else:
            cprint('Nothing happened today. Press enter to continue.', 'cyan')
            input()
            clear()
    elif ID == 2:
        return (selfsick())
    elif ID == 3:
        return (burglary())
    elif ID == 4:
        flagellants()
    elif ID == 5:
        return (cleaners())
    elif ID == 6:
        return (herbs())
    elif ID == 7:
        return (blessing())
    elif ID == 8:
        return (witches())
    elif ID == 9:
        return (fight())
    else:
        cprint('Nothing happened today. Press enter to continue.', 'cyan')
        input()
        clear()


day = 0


def game():
    global day
    global bruh
    global record
    intro()
    input()
    clear()
    day = 0
    while bruh != 'dead':
        day += 1
        cprint('Day ' + str(day), 'magenta')
        bruh = event()
    if day > record:
        record = day
    cprint('You survived ' + str(day) + ' days.', 'red')
    cprint('Your record is ' + str(record) + ' days survived.', 'red')


record = 0
game()

while 1 == 1:
    if day == 1 and not 'Speedrunner' in endings:
        endings.append('Speedrunner')
    if day >= 50 and not 'Fifty day gang' in endings:
        endings.append('Fifty day gang')

    cprint('You have unlocked the following endings:', 'cyan')
    for item in endings:
        cprint(item, 'red')
    cprint('Press enter to replay.', 'cyan')
    input()
    clear()
    bruh = ''
    pious = 0
    family = random.randint(3, 5)
    game()