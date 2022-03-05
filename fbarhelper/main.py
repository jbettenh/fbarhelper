import calculations as calc


def print_menu(menu):
    print('What would you like to do? Please enter a number.')
    for key in menu.keys():
        print(key, '--', menu[key])


def main():
    stored = False
    menu_options = {
        1: 'Import CSV files.',
        2: 'Enter a balance.',
        3: 'Show max credit.',
        4: 'Show max debit.',
        5: 'Show max balance.',
        6: 'Exit',
    }
    while True:
        print('\n')
        print_menu(menu_options)
        output = ''
        try:
            selection = int(input())
        except:
            print('Input invalid, please enter a number.')
            continue

        if selection == 1:
            print('1')
        elif selection == 2:
            while stored is not True:
                balance_date = input('Please input the date of the known balance. (Format YYYY-MM-DD)\n')
                balance_amount = input('Please input the amount of the known balance. (Format 1,000.00)\n')
                stored = calc.input_balance(balance_date, balance_date, balance_amount)
        elif selection == 3:
            output = calc.get_max_credit()
        elif selection == 4:
            output = calc.get_max_debit()
        elif selection == 5:
            output = calc.get_max_balance()
        elif selection == 6:
            print('Bye!!')
            exit()
        else:
            print('Invalid selection. Please enter a number between 1 and 5.')

        print(output)
        print('\n')


if __name__ == '__main__':
    main()
