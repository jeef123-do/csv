import csv
import operator


def line():
    print('-' * 30)


def readCsvDict(FN):
    data = []
    with open(FN, mode='r', encoding='utf-8', newline="") as fn:
        fr = csv.DictReader(fn)
        for i in fr:
            data.append(i)
    cal(data)


def cal(data):
    line()
    print('ค่าเฉลี่ย การเกิดเหตุการณ์เพลิงไหม้ ปี 2555-2557')
    line()
    dataAvg = {}
    fire = []
    dead = []
    injury = []
    for i in data:
        avg = (int(i['fire55']) + int(i['fire56']) + int(i['fire57'])) / 3
        dataAvg.update({i['month']: avg})

        if int(i['fire57']) > int(i['fire56']) > int(i['fire55']):
            fire.append(i['month'])
        if int(i['dead55']) and int(i['dead56']) and int(i['dead57']) > 0:
            dead.append(i['month'])
        if int(i['injury55']) > int(i['injury56']) > int(i['injury57']):
            injury.append(i['month'])

    sort = (sorted(dataAvg.items(), key=operator.itemgetter(1), reverse=True))
    for num, i in enumerate(sort):
        print('{}.) {} จำนวน {:.2f} ครั้ง'.format(num + 1, i[0], i[1]))

    line()
    print('เดือนที่ต้องระวังเนื่องจากมีเตุการณ์ไฟไหม์มากขึ้นทุกปีที่ผ่านมา คือ {}'.format(fire))
    line()
    print('เดือนที่มีคนตายทุกปี คือ {}'.format(dead))
    line()
    print('เดือนที่มีคนเจ็บลดลงทุกปี คือ {}'.format(injury))
    line()


if __name__ == '__main__':
    filename = 'D:/week4/File/fire.csv'
    readCsvDict(filename)
