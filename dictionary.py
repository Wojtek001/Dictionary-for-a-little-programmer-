import sys
import csv

def main_menu():

    print('Dictionary for a little programmer:')
    print('1 - search explanation by appellation')
    print('2 - add new definition')
    print('3 - show all appellations alphabetically')
    print('0 - exit')


appelations = ['ARGUMENT', 'ASCII TABLE', 'DICTIONARY', 'FOR LOOP', 'FUNCTION', 'GIT', 'LIST', 'LOOP', 'MODULE',\
               'PARAMETER', 'STRING', 'TUPLE', 'VARIABLE', 'VERSION CONTROL', 'WHILE LOOP']

def definitions():
    import linecache
    if appelation == 'FUNCTION':
        print(linecache.getline('dictionary.csv', 1))
    elif appelation == 'PARAMETER':
        print(linecache.getline('dictionary.csv', 2))
    elif appelation == 'VARIABLE':
        print(linecache.getline('dictionary.csv', 3))
    elif appelation == 'ARGUMENT':
        print(linecache.getline('dictionary.csv', 4))
    elif appelation == 'DICTIONARY':
        print(linecache.getline('dictionary.csv', 5))
    elif appelation == 'TUPLE':
        print(linecache.getline('dictionary.csv', 6))
    elif appelation == 'ASCII TABLE':
        print(linecache.getline('dictionary.csv', 7))
    elif appelation == 'MODULE':
        print(linecache.getline('dictionary.csv', 8))
    elif appelation == 'STRING':
        print(linecache.getline('dictionary.csv', 9))
    elif appelation == 'GIT':
        print(linecache.getline('dictionary.csv', 10))
    elif appelation == 'VERSION CONTROL':
        print(linecache.getline('dictionary.csv', 11))
    elif appelation == 'LIST':
        print(linecache.getline('dictionary.csv', 12))
    elif appelation == 'LOOP':
        print(linecache.getline('dictionary.csv', 13))
    elif appelation == 'WHILE LOOP':
        print(linecache.getline('dictionary.csv', 14))
    elif appelation == 'FOR LOOP':
        print(linecache.getline('dictionary.csv', 15))
    else:
        print('Incorrect word!')
        main_menu()

main_menu()
numbers = ['1', '2', '3', '0']
chosen_number = input("Enter selected number from the list above: ")

while chosen_number not in numbers:
    print ('Invalid number!')
    chosen_number = input("Enter correct number from the list above: ")

if chosen_number == '1':
    appelation = input("Enter an appelation: ").upper()
    definitions()

elif chosen_number == '2':
    add_appelation = input('Enter new appelation: ')
    add_explanation = input('Enter explanation: ')
    add_source = input('Enter a source: ')
    with open('dictionary.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([add_appelation, add_explanation, add_source])

elif chosen_number == '3':
    print(appelations)

elif chosen_number == '0':
    print('See You later!')
    sys.exit()