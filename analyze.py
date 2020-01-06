import csv
import sys
from collections import defaultdict


def compute(fnames):
    all_data = {}
    for fname in fnames:
        data = []
        with open(fname, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(dict(row))

            month_name = fname.replace('.csv', '')
        all_data[month_name] = data

    rs = lambda: defaultdict(rs)
    results = rs()

    for name, data in all_data.items():
        for row in data:
            results[row['Project name']][row['Service description']][row['SKU description']][name] = row['Cost ($)']

    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        headers = ['Project name', 'Service Description', 'SKU Description']
        for fname in fnames:
            headers.append(fname.replace('.csv', ''))
        writer.writerow(headers)

        for project_name, val1 in results.items():
            for service_desc, val2 in val1.items():
                for sku_desc, val3 in val2.items():
                    row = [project_name, service_desc, sku_desc]
                    for month, cost in val3.items():
                        row.append(cost)
                    writer.writerow(row)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Please supply at least two filenames, eg. python calc.py month1.csv month2.csv')

    compute(sys.argv[1:])
