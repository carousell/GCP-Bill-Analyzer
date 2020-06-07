import csv
import sys
from collections import defaultdict


PROJ_NAME = 'Project name'
SERV_DESC = 'Service description'
SKU_DESC = 'SKU description'
COST = 'Cost ($)'


def compute(fnames):
    all_data = {}
    headers = [PROJ_NAME, SERV_DESC, SKU_DESC]
    for fname in fnames:
        data = []
        with open(fname, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(dict(row))

            month_name = fname.replace('.csv', '')
            headers.append(month_name)
        all_data[month_name] = data

    rs = lambda: defaultdict(rs)
    results = rs()

    for name, data in all_data.items():
        for row in data:
            results[row[PROJ_NAME]][row[SERV_DESC]][row[SKU_DESC]][name]\
                = row[COST]

    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)

        for project_name, val1 in results.items():
            for service_desc, val2 in val1.items():
                for sku_desc, val3 in val2.items():
                    row = [project_name, service_desc, sku_desc]
                    for fname in fnames:
                        cost = val3.get(fname.replace('.csv', ''), 0.0)
                        row.append(cost)
                    writer.writerow(row)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Please supply at least two filenames, ' +
              'eg. python analyze.py month1.csv month2.csv')

    compute(sys.argv[1:])
