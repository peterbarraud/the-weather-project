from csv import DictReader
def main():
    with open('monthly-data/delhi-temp-rains.csv') as f:
        w_data = DictReader(f)
        x = 0
        for row in w_data:
            try:
                max_temp = float(row['Temp Max'])
            except ValueError:
                x += 1
                print(row['Date'])
        print(x)


if __name__ == '__main__':
    main()
    print('ALL DONE')
    