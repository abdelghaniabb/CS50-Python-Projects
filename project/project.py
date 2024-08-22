#!/usr/bin/python3

import csv

# global variable
total = dict()


# 1 Get the data.
def read_file():
    """reads the file and returns the the data"""
    with open('data.csv', 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        indata = list()
        for row in reader:
            indata.append(row)

        return indata


# 2 Extract the roommates' names from the data .
def extract_names(indata):
    """extracts roommates' names """
    names = indata[0][0].split(';')

    data = list()
    for row in indata[1:]:
        data.append(row[0].split(';'))
    
    return names, data


# 3 Calculate the amount of money that each person should receive or pay.
def calculate(names, data):
    """Calculates the amount of money that each person should receive or pay"""
    for name in names:
        total[name] = 0
    
    for row in data:
        person_index = 0
        for spent in row:
            name = names[person_index]
            person_index += 1
            check_contributed(names, name, spent)
            #print(total)
            #print(sum(total.values()))


def check_contributed(names, name_spender, spent):
    """Checks and calculates contributions"""
    spent_list = spent.split('-')

    if len(spent_list) == 1:
        value = float(spent_list[0]) / len(names)
        for name in names:
            if name == name_spender:
                total[name] += value * (len(names) - 1)
            else:
                total[name] -= value

    else:
        # get the non contributed names
        non_contributed_names = list()
        for item in spent_list[1:]:
            non_contributed_names.append(item.replace(' ', '').lower())

        # check if all the non contributed names where correct
        for name in non_contributed_names:
            if name not in names:
                print("Name error: <<{}>>".format(name))
                exit(0)
        value = float(spent_list[0]) / (len(names) - len(non_contributed_names))
        if name_spender in non_contributed_names:
                total[name_spender] += value * (len(names) - len(non_contributed_names))

        for name in names:
            if name in non_contributed_names:
                pass
            elif name == name_spender:
                total[name] += value * (len(names) - len(non_contributed_names) - 1)
            else:
                total[name] -= value

def main():
    """this is the main function"""
    indata = read_file()
    names, data = extract_names(indata)
    calculate(names, data)

    print('*********************************')
    for key, val in total.items():
        print(key, ': {:.2f}'.format(val))
    print(sum(total.values()))

if __name__ == '__main__':
    main()

