def basicTextFile(FN):
    fn = open(FN, mode='a')
    fn.write('aaa')
    fn.close()


def createCSV(FN):
    with open(FN, mode='a', encoding='utf-8') as fn:
        fn.write('{},{},{}'.format('adf', 99, 40))

def readCSV(FN):
    with open(FN, mode='r', encoding='utf-8') as fn:
        age=0
        weight=0
        count=0
        for i in fn:
            j=i.split(',')
            #print(j[1])
            #print('{}'.format(i),end="")
            #print('{}'.format(type(i)))
            print('คุณชื่อ {}'.format(j[0]))
            print('คุณหนัก {}'.format(int(j[1])))
            print('คุณอายุ {}'.format(int(j[2])))
            print('-'*30)
            age+=int(j[1])
            weight+=int(j[2])
            count+=1
        print('weight avg: {:.2f}'.format(weight/count))
        print('age avg: {:.2f}'.format(age/count))

if __name__ == '__main__':
    filename = '/python/File/test.csv'
    #basicTextFile(filename)
    #createCSV(filename)
    readCSV(filename)