import csv
import random

random.seed(42)  # For reproducibility

def augment(k):
    """Augment a single row."""
    final = []
    for i in range(0, 7):
        final.append(round(random.uniform(33.33, 66.66) + float(k[i]), 2))
    return final + [int(k[7])]

# Open CSV files
with open('data.csv', mode='r') as data1, open('data1.csv', mode='r') as data0, open('final_data.csv', mode='w', newline='') as f:
    reader1 = csv.reader(data1)
    reader0 = csv.reader(data0)
    writer = csv.writer(f, delimiter=',')

    # Optional: skip header if present
    # next(reader1)
    # next(reader0)

    for row1 in reader1:
        writer.writerow(row1)
        for _ in range(19):
            writer.writerow(augment(row1))

    for row0 in reader0:
        writer.writerow(row0)
        for _ in range(19):
            writer.writerow(augment(row0))
