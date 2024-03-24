import csv

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def calculate_average(values):
    total = 0
    for value in values:
        total += float(value)
    return total / len(values)

def filter_data(data, key, value):
    filtered_data = []
    for item in data:
        if item[key] == value:
            filtered_data.append(item)
    return filtered_data
