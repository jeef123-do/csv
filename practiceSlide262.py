import csv


def readCsv(FN, FN2):
    comment = []
    rude = set()
    with open(FN, mode='r', encoding='utf-8', newline="") as fn:
        fr = csv.reader(fn)
        for i in fr:
            comment.append(i[0].lower())
    with open(FN2, mode='r', encoding='utf-8', newline="") as fn2:
        fr2 = csv.reader(fn2)
        for i in fr2:
            rude.add(i[0].lower())
    writeCsv(comment, rude)


def writeCsv(comment, rude):
    word = []  # word can't show
    word2 = []  # word can show
    for i in comment:
        show = True
        n = set(i.split(" "))
        if len(rude.intersection(n)) > 0:
            show = False
        if show:
            word2.append([i])
        else:
            word.append([i])

    # print(word2)
    canShow = 'D:/week4//File/canshow.txt'
    cantShow = 'D:/week4/File/cannotshow.txt'
    with open(cantShow, mode='a', encoding='utf-8', newline="") as cnt:
        fw = csv.writer(cnt)
        fw.writerows(word)
    with open(canShow, mode='a', encoding='utf-8', newline="") as cn:
        fw2 = csv.writer(cn)
        fw2.writerows(word2)

    # show feedback
    feedback = (word.__len__() / comment.__len__()) * 100
    print('Bad Feedback = {}%'.format(feedback))


if __name__ == '__main__':
    filename = 'D:/week4/File/practice-comment.txt'
    filename2 = 'D:/week4/File/rude_word.txt'
    readCsv(filename, filename2)
