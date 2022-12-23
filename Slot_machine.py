""" |---| READ ME |---|

Cześć jest to projekt, w którym staram się napisać maszynę losującą niczym z kasyn.

Program ma przechowywać dane pomiędzy uruchomieniami, tzn że jak raz się zarejestrujemy to
będziemy mogli już do końca naszych dni (albo do końca dobrej woli admina) kożystać z tego konta

Do maszyny wprowadzamy nasze dane logowania, wpłacamy wirtualne pieniądze i możemy grać!

Projekt jest cały czas w trakcie rozwijania także jakbyś natrafił/a na jakiś bug/error to można się
ze mną kontaktować przez Discord: Access#2933

Instrukcja obsługi:
    - Na początku trzeba ręcznie zrobić sobie 3 pliki tekstowe:
        - database.txt - tam będziemy przechowywać dane użytkowników RAZEM Z ICH HASŁAMI!!!
        - earnings.txt - tutaj przechowujemy informacje ile nasza maszyna zarobiła pieniędzy
        - logs.txt - JESZCZE nie jest potrzebny ale niebawem będziemy mogli znaleźć tam logi użytkowników
    - należy też pozmieniać nazwy ścieżek tak aby pasowały wyżej stworzonym folderom
    - do przemieszczania się po tym prostym GUI używamy odpowiednich cyfr
    - aby dostać się do panelu administratora należy wylogować się ze wszystkich kont
      a następnie wpisać "Admin1"
"""


"""TODO
|     DONE!     |   Implement simple txt database
|     DONE!     |   Implement total earning counter
|  in progress  |   Implement logs only last 200 interactions
|  in progress  |   Implement deposit value database
|  in progress  |   Make BIG RED BUTTON that clears every database
|  in progress  |   User stats - games played - money gain - admin access only
"""

import random

print('\n\t\tWORK STILL IN PROGRESS\n\n\n')


def database_assignment():
    with open("venv/slm_data/database.txt", "r") as database:
        user_dataBase = database.readlines()
    for idx, val in enumerate(user_dataBase):
        user_dataBase[idx] = val.split()
    return user_dataBase


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
    user = f'{username} {passwd} {money}'
    return user


def log_in(username, passwd, user):
    if username == user[0] and passwd == user[1]:
        return 1
    return 0


def deposit():
    while True:
        current_money = 0.0
        with open('venv/slm_data/earnings.txt', 'r') as money_file:
            current_money = float(money_file.read())
        depo = float(input('Deposit at least 5$: '))
        print(current_money)
        if depo >= 5:
            current_money += depo
            with open('venv/slm_data/earnings.txt', 'w') as file:
                file.write(f'{current_money}')
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
    while True:
        case = int(input(f'Welcome {username}, you have {money_amount}$!\nLet{chr(92)}s play!\n\n1. Deposit\n2. '
                         f'Play\n3. Quit\n'))
        if case == 1:
            money_amount += deposit()
        elif case == 2:
            money_amount = slot_machine(money_amount)
        elif case == 3:
            return money_amount


def p_user_database(DB):
    print('username - passwd - wallet')
    for user in DB:
        print(*user, sep='\t | \t')
    return 0


def admin_panel(DB):
    while True:
        case = input('1. User Database\n2. Earnings\n3. Logs\n4. Exit admin panel\n213769420. RED_BUTTON_(DO NOT USE!!)\n')
        if case == '1':
            p_user_database(DB)
        elif case == '2':
            with open('venv/slm_data/earnings.txt', 'r') as money:
                cash = money.read()
                print(f'users deposited {cash}$')
        elif case == '4':
            break


def simple_start_interface():
    while True:
        user_dataBase = database_assignment()
        case = input('1. Login\n2. Sign in\n3. Close program\n')
        if case == '1':
            flag = False
            username = input('Username:\t')
            passwd = input('Password:\t')
            for i in user_dataBase:
                if log_in(username, passwd, i):
                    i[2] = simple_logged_interface(username, float(i[2]))
                    flag = True
                    break
            if not flag:
                print('Wrong username or password :(')
        elif case == '3':
            exit()
        elif case == '2':
            with open('venv/slm_data/database.txt', 'a') as database:
                database.write(sing_in(user_dataBase)+'\n')

        elif case == 'Admin1':
            admin_panel(user_dataBase)
        else:
            print('Error!!!')


def main():
    simple_start_interface()


main()
