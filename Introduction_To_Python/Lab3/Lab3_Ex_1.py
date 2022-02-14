import os


if __name__ == '__main__':
    # Getting list of Files from directory
    files = os.listdir('zadanie1')
    # Getting path to directory
    path = os.path.abspath('zadanie1')
    for file in files:
        # Sorting files into certain directory
        try:
            os.rename(path + '/' + file, path + '/' + file[0].upper() + '/' + file)
        # Creating new directory and moving into new directory
        except FileNotFoundError:
            os.mkdir(path + '/' + file[0].upper())
            os.rename(path + '/' + file, path + '/' + file[0].upper() + '/' + file)
