import csv as c
import operator as o
import os

if __name__ == '__main__':
    # Opening input and temporary file
    with open('zadanie2.csv', 'r') as inp, open('temporary.csv', 'w', newline='') as out:
        # Creating reader of csv file
        reader = c.reader(inp)
        # Creating writer of csv file
        writer = c.writer(out)
        # Taking header row from input file
        header = next(reader)
        # Writing header row into temporary file
        writer.writerow(header)
        # Removing rows with empty values and changing all letters into lowercase
        for row in reader:
            if row[1] != '':
                row = [elem.lower() for elem in row]
                writer.writerow(row)
    # Opening result and temporary file
    with open('temporary.csv', 'r') as inp, open('result_of_ex2.csv', 'w', newline='') as out:
        # Creating reader of csv file
        reader = c.reader(inp)
        # Taking header row from input file
        header = next(reader)
        # Creating a list that will allow us to work on id column
        temporary_list = [row for row in reader]
        # Changing id from strings into integers
        for value in temporary_list:
            value[0] = int(value[0])
        # Sorting file by id
        list_form_reader = sorted(temporary_list, key=o.itemgetter(0), reverse=False)
        # Repairing id numeration
        for i in range(len(list_form_reader)):
            for values in list_form_reader[:i]:
                if values[0] == list_form_reader[i][0]:
                    list_form_reader[i][0] = list_form_reader[i - 1][0] + 1
        # Removing words that matches condition of exercise
        for row in list_form_reader:
            for i in range(1, len(row)):
                words = row[i].split(' ')
                for word in words:
                    try:
                        if abs(ord(word[0])-ord(word[1])) == 1:
                            print('Removed word: \"{}\" form id: {}'.format(word, row[0]))
                            words.remove(word)
                    except IndexError:
                        pass
        # Creating writer of csv file
        writer = c.writer(out)
        # Writing header row into temporary file
        writer.writerow(header)
        # Saving final file
        writer.writerows(list_form_reader)
    # Removing temporary file
    os.remove('temporary.csv')
