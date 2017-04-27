import sys
import csv
import os


def main():

    with open("dictionary.csv", mode='r') as infile:
        reader = csv.reader(infile)
        my_dict = {rows[0]: (rows[1], rows[2]) for rows in reader}

    os.system('clear')

    print('Dictionary for a little programmer:')
    print('1 - search explanation by appellation')
    print('2 - add new definition')
    print('3 - show all appellations alphabetically')
    print('0 - exit')

    numbers = ['1', '2', '3', '0']
    chosen_number = input("Enter selected number from the list above: ")

    while chosen_number not in numbers:
        print ('Invalid number!')
        chosen_number = input("Enter correct number from the list above: ")

    if chosen_number == '1':

        os.system('clear')
        appelation = input("Enter an appelation: ").upper()

        if appelation in my_dict:
            def_source = '  '.join(my_dict[appelation])
            print(def_source)
        elif appelation not in my_dict:
            os.system('clear')
            print("No such appellation in a dictionary. Try again.")

        menu_return()

    elif chosen_number == '2':

        os.system('clear')
        add_appelation = input('Enter new appelation: ').upper()
        add_explanation = input('Enter explanation: ')
        add_source = input('Enter a source: ')
        with open('dictionary.csv', 'a', newline='') as csvfile:
            new_appelation = ', '.join([add_appelation, add_explanation, add_source])
        new_appel = open("dictionary.csv", 'a')
        new_appel.write(new_appelation)
        new_appel.write("\n")
        new_appel.close

        menu_return()

    elif chosen_number == '3':

        os.system('clear')
        dict_alphabet = sorted(my_dict)
        for i in dict_alphabet:
            print (i)

        menu_return()

    elif chosen_number == '0':
        print('See You later!')
        sys.exit()


def menu_return():

    decision = input("Press 'q' to quit program or to come back to the main menu - press any other key:  ").lower()
    if decision == "q":
        print('See You later!')
        sys.exit()
    else:
        main()

main()

