import csv


def readCSV(FN):
    with open(FN, mode='r', encoding='utf-8', newline="") as fn:
        fr = csv.reader(fn)
        for i, v in enumerate(fr):
            print('{}. - {}'.format(i + 1, v[0]).upper())


if __name__ == '__main__':
    filename = 'D:/week4/File/ilovesea.txt'
    # writeCSV(filename)
    readCSV(filename)
