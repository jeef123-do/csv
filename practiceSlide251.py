import csv


def readCSV(FN):
    with open(FN, mode='r', encoding='utf-8', newline="") as fn:
        fr = csv.reader(fn)
        sort = sorted(fr, reverse=True)
        for i, v in enumerate(sort):
            print('{}.) {}'.format(i + 1, v[0]).upper())


if __name__ == '__main__':
    filename = 'D:/week4/File/MarvelComics.txt'
    # writeCSV(filename)
    readCSV(filename)
