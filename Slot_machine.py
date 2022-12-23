"""TODO
* Implement simple txt database                               | in progress   |
* Implement logs only last 200 interactions                   | in progress   |
* Implement deposit value database                            | in progress   |
* Make BIG RED BUTTON that clears every database              | in progress   |
* User stats - games played - money gain - admin access only  | in progress   |
"""

import random
print('\n\t\tWORK STILL IN PROGRESS\n\n\n')
user_dataBase = [['Admin1', 'Admin1', 10000000.0]]
total_deposits = 0.0


def sing_in(database):
    flag = True
    while flag:
        flag = False
        username = input('username:\t')
        passwd = input('Password:\t')
        for user in database:
            if user[0] == username:
                flag = True
                print('Username already exist')
    while True:
        money = float(input('Place your first deposit, at least 5$\nAmount in $: '))
        if money >= 5:
            break
        else:
            print('Wrong amount, please try again.')
    user = [username, passwd, money]
    return user


def log_in(username, passwd, user):
    if username == user[0] and passwd == user[1]: return 1
    return 0


def deposit():
    while True:
        depo = float(input('Deposit at least 5$: '))
        if depo >= 5:
            return depo
        else:
            print('Wrong amount! \nIf You do not want to deposit press (q)')


def slot_machine(money):
    options = {
        '0': 'A',
        '1': 'B',
        '2': 'C',
        '3': 'D'
    }

    row = []
    while True:
        bet = float(input('Place bet: '))
        if money - bet < 0:
            print('You do not have enough $$ :(')
        else:
            money -= bet
            break

    while True:
        times = int(input('How many rows? (1-3): '))
        if times in range(1, 4):
            for i in range(times):
                a, b, c = str(random.randint(0, 3)), str(random.randint(0, 3)), str(random.randint(0, 3))
                row.append([a, b, c])
            break
        else:
            print('Wrong number!')

    print(f'/-----------{chr(92)}')
    for i in range(times):
        print(f'| {options[str(row[i][0])]} | {options[str(row[i][1])]} | {options[row[i][2]]} |')
    print(f'{chr(92)}-----------/')

    win_count = 0
    for r in row:
        if r[0] == r[1] and r[0] == r[2]:
            win_count += 1

    if win_count:
        print(f'You have won {bet * (2 ** win_count)}$!\nLet{chr(92)}s goo!')
        money += bet * (2**win_count)
    else:
        print('So close!\nBetter luck next time ;)')

    return money


def simple_logged_interface(username, money_amount):
    money_amount = money_amount
    while True:
        case = int(input(f'Welcome {username}, you have {money_amount}$!\nLet{chr(92)}s play!\n\n1. Deposit\n2. Play\n3. '
                         f'Quit\n'))
        if case == 1:
            depo = deposit()
            money_amount += depo
           # total_deposits += depo
        elif case == 2:
            money_amount = slot_machine(money_amount)
        elif case == 3:
            return money_amount


def p_user_database():
    print('username - passwd - wallet')
    for user in user_dataBase:
        print(*user, sep='\t | \t')
    return 0


def admin_panel():
    while True:
        case = input('1. User Database\n2. Earnings\n3. Logs\n4. RED_BUTTON_(DO NOT USE!!)')
        if case == '1':
            p_user_database()
            break


def simple_start_interface():
    while True:
        case = input('1. Login\n2. Sign in\n3. Close program\n')
        if case == '1':
            flag = False
            username = input('Username:\t')
            passwd = input('Password:\t')
            for i in user_dataBase:
                if log_in(username, passwd, i):
                    i[2] = simple_logged_interface(username, i[2])
                    flag = True
                    break
            if not flag:
                print('Wrong username or password :(')
        elif case == '3':
            exit()
        elif case == '2':
            user_dataBase.append(sing_in(user_dataBase))
        elif case == 'Admin1':
            admin_panel()
        else:
            print('Error!!!')


def main():
    simple_start_interface()


main()
