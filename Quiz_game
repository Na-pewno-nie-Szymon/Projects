"""
Quiz game!

quizy naukowe powiązane z odpowiednimi tematami
Na teraz plany są na:
    - Podstawy chemii dla bioinformatyków
    - Bioróżnorodność i podstawy taksonomii
    - Analiza matematyczna
    - Sztuka krytycznego myślenia

Na każde pytanie będą wyświetlane 4 losowe odpowiedzi gdzie conajmniej jedna z nich będzie poprawna
-|-PRZYKŁAD-|-
a) prawda
b) fałsz
c) fałsz
d) prawda
odpowiedź: ad

Póki co trzeba ręcznie uzupełnić bazę pytań

"""

"""TODO
|   in progress |   Osobna baza pytań do każdej stworzonej kategorii razem z odpowiedziami
|      DONE     |   Maszyna losująca pytania i odpowiedzi, w losowej kolejności
|   in progress |   GUI prawdziwe, nie konsolowe
|   in progress |   Zrób installer który załatwi większość skomplikowanych rzeczy za użytkownika 
                    https://www.advancedinstaller.com
|   in progress |   Naucz się robić nowe foldery, tak żeby działało w PyCharm
"""
import os
import random
import time

kategorie = {
    'chemia': 'bazy_pytan\chemia.txt',
    'bipt'  : 'bazy_pytan\Bipt.txt',
    'matma' : 'bazy_pytan\matma.txt',
    'sztuka': 'bazy_pytan\sztuka.txt'
}


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def pytania(kategoria):  #maszyna losująca pytania i odpowiedzi
    with open(kategoria, 'r') as file:
        dane = file.readlines()

    los = random.randint(0, len(dane)-1)

    pytanie, prawda, falsz = dane[los].split(';')
    prawda = prawda.split()
    falsz = falsz.split()

    los_prawda = prawda[random.randint(0, len(prawda)-1)]
    los_falsz = [falsz[random.randint(0, len(falsz))-1]]
    while len(los_falsz) < 3:
        wylosowana = random.randint(0, len(falsz)-1)
        if wylosowana not in los_falsz:
            los_falsz.append(falsz[wylosowana])

    odpowiedzi = [los_prawda, *los_falsz]
    temp = odpowiedzi
    print(pytanie)
    odpowiedz = 0
    for i in range(len(temp)):
        odp = random.randint(0, len(temp)-1)
        if temp[odp] == los_prawda:
            odpowiedz = i+1
        print(i+1, temp[odp])
        temp.pop(odp)

    odp = input('Odp: ')

    if odp == str(odpowiedz):   return 1
    else:                       return 0


def homescreen():
    print('\t-|-----------------------|-')
    print('\t-|      Zdaj Sesje!      |-')
    print('\t-|-----------------------|-')
    print('\t-| 1.Chemia              |-')
    print('\t-| 2.BiPT                |-')
    print('\t-| 3.Matematyka          |-')
    print('\t-| 4.Sztuka kryt.        |-')
    case = int(input('\t-| Czego się uczymy?: '))
    return case


def quiz(cat):
    ilosc_punktow = 0
    max_punktow = 5

    start = input('Gotów żeby zacząć? (Y/N)')
    if start == 'N' or start == 'n':
        return 0
    elif start == 'Y' or start == 'y':
        clear()
        print('To zaczynajmy!')
        time.sleep(0.5)
        for i in range(3,0,-1):
            print(f'{i}...')
            time.sleep(0.5)
        clear()
        for i in range(5):
            ilosc_punktow += pytania(kategorie[cat])
            clear()

        return ilosc_punktow

def main():
    punkty = 0
    while True:
        print('')
        print(f'\t-|      Wynik: {punkty}/5!      |-')
        case = homescreen()
        if case == 1:
            punkty = quiz('chemia')


if __name__ == "__main__":  main()
