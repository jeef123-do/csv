import csv


def readCsv(FN, FN2):
    products = []
    config = {}
    with open(FN, mode='r', encoding='utf-8', newline="") as fn:
        fr = csv.reader(fn)
        for i in fr:
            products.append(i)
    with open(FN2, mode='r', encoding='utf-8', newline="") as fn2:
        fr2 = csv.reader(fn2)
        for i in fr2:
            sp = i[0].split("=")
            config[sp[0]] = sp[1]
    CalValue(products, config)


def CalValue(products, config):
    sumall = 0
    for i in products:
        sum = float(i[1]) * float(i[2])
        comma = ""
        if config["comma"] == "yes":
            comma = ","
        print('{:<15} {a:>15{b}.{c}f} '.format(i[0], a=sum, b=comma, c=config["decimal_places"]))

        sumall += sum
    print(config["line"] * 40)
    print('Total Value {a:>19{b}.{c}f} {unit}'.format(a=sumall, b=comma, c=config["decimal_places"],
                                                      unit=config['currency_unit']))


if __name__ == '__main__':
    filename = 'D:/week4/File/products.csv'
    filename2 = 'D:/week4/File/appConfig.ini'
    readCsv(filename, filename2)
