import string as s
import time as t


if __name__ == '__main__':
    # Enter the text from keyboard
    text = input('Enter text:')
    # Removing punctuation marks
    text = text.translate(str.maketrans('', '', s.punctuation))
    # Changing all letters into lowercase
    text = text.lower()
    # Splitting the text into single words
    words = text.split()
    # Deleting duplicates words
    words = list(set(words))
    # Checking if the text is one word
    if len(words) == 1:
        print('You enter one word.')
    # Start measuring time of searching in SJP
    s_time = t.time()
    # Searching if words form text are in SJP
    for word in words:
        with open('SJP.txt', 'r', encoding='utf8') as file:
            if word in file.read():
                print('\"{}\" is in SJP.'.format(word))
            else:
                print('\"{}\" is not in SJP.'.format(word))
    # Printing the time of searching
    print('Searching took: ', t.time() - s_time, 's')
