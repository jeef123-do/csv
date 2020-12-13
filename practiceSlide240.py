import csv


def line():
    print('=' * 30)


def addInfo(FN):
    num = int(input('Enter Number of New Product : '))
    product = []
    for i in range(num):
        print('\nProduct Number [{}]'.format(i + 1))
        line()
        name = input('Enter product name : ')
        price = input('Enter product price : ')
        stock = input('Enter product stock : ')
        product.append([name, price, stock])
    print(product)
    with open(FN, mode='a', encoding='utf-8', newline="") as fn:
        fw = csv.writer(fn, delimiter=',')
        fw.writerows(product)


if __name__ == '__main__':
    filename = 'D:/week4/File/products.csv'
    addInfo(filename)
