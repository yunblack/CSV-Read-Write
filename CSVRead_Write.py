# name: Juyoung Daniel Yun
# email: juyoung.yun@stonybrook.edu
# id: 112368205

import csv

def readcsv():
    with open('./data/worldpopulation.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            print(f'\t{row["Flag"]} {row["Country"]} has population of {row["Population2018"]} in 2018, and will have population of {row["Population2030"]} in 2030.')
            line_count += 1


def writecsv():
    with open('./data/worldpopulationchange.csv', mode='w', newline='') as csv_file:
        fieldnames = ['Flag', 'Country', 'Population2018','Population2030','ratio']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        with open('./data/worldpopulation.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                writer.writerow(
                    {'Flag': row["Flag"],
                     'Country': row["Country"],
                     'Population2018': row["Population2018"],
                     'Population2030': row["Population2030"],
                     'ratio': float(row["Population2030"]) / float(row["Population2018"])})
                line_count += 1

def main():
    readcsv()
    writecsv()

if __name__ == '__main__':
    main()