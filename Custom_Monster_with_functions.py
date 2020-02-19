import sys
monster = ['Kratos', '100', '20', '10']
stats = ['name:', 'hp:', 'def:', 'atk:']
question = ['', 'Enter the monsters health point value:', 'Enter the monsters defence value:', 'Enter the monsters attack value:']

def MonsterStats():
    for i in range(1, 4):
        while True:
            print(question[i])
            answer = input()
            if answer.upper().isnumeric():
                monster[i] = answer.upper()
                break
            else:
                print('Please enter a number!')
                continue

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
        MonsterStats()
        print('The stats of your defined monster are:')
        for i in range(0, 4):
            print(stats[i])
            print(monster[i])
        break
else:
    print('The predefined monster is:')
    for i in range(0, 4):
        print(stats[i])
        print(monster[i])
    sys.exit()