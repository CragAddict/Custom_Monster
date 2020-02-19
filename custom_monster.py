#This is for creating a custom character in a game

import sys
monster = ['Kratos', '100', '20', '10']
stats = ['name:', 'hp:', 'def:', 'atk:']
print('Do you want to change any of the monsters values?')
answer1 = input()
if answer1.upper() == 'YES':
    while True:
        print('Enter the monsters name:')
        answer2 = input()
        if answer2.upper().isalpha():
            monster[0] = answer2.upper()
        else:
            print('Please enter a name, that consists of letters!')
            continue

        while True:
            print('Enter the monsters health point value:')
            answer3 = input()
            if answer3.upper().isnumeric():
                monster[1] = answer3.upper()
                break
            else:
                print('Please enter a number!')
                continue

        while True:
            print('Enter the monsters defence value:')
            answer4 = input()
            if answer4.upper().isnumeric():
                monster[2] = answer4.upper()
                break
            else:
                print('Please enter a number!')
                continue

        while True:
            print('Enter the monster attack value:')
            answer5 = input()
            if answer5.upper().isnumeric():
                monster[3] = answer5.upper()
                break
            else:
                print('Please enter a number!')
                continue
        print('The stats of your defined monster are:')
        for i in range(0,4):
            stat = stats[i]
            own = monster[i]
            print(stat)
            print(own)
        break
else:
    print('The predefined monster is, '+ str(monster))
    sys.exit()