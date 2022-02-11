import calculations as calc


def print_menu(menu):
    print('What would you like to do? Please enter a number.')
    for key in menu.keys():
        print(key, '--', menu[key])


def main():
    menu_options = {
        1: 'Import CSV files.',
        2: 'Enter a balance.',
        3: 'Show max credit.',
        4: 'Show max debit.',
        5: 'Exit',
    }
    while(True):
        print_menu(menu_options)
        selection = ''
        output = ''
        try:
            selection = int(input())
        except:
            print('Wrong input, please enter a number.')

        if selection == 1:
            print('1')
        elif selection == 2:
            print('2')
        elif selection == 3:
            output = calc.get_max_credit()
        elif selection == 4:
            output= calc.get_max_debit()
        elif selection == 5:
            print('Bye!!')
            exit()
        else:
            print('Invalid selection. Please enter a number between 1 and 5.')

        print(output)
        print('\n')


if __name__ == '__main__':
    main()