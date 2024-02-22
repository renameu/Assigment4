import csv
import json
from stuff import House, Flat


def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['type', 'name', 'description', 'price', 'brand']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item.to_dict())


def load_from_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['type'] == 'House':
                data.append(House(row['name'], row['description'], float(row['price']), row['address']))
            elif row['type'] == 'Flat':
                data.append(Flat(row['name'], row['description'], float(row['price']), row['floor']))
    return data


def save_to_json(data, filename):
    serialized_data = []
    for item in data:
        serialized_data.append(item.to_dict())

    with open(filename, 'w') as jsonfile:
        json.dump(serialized_data, jsonfile, indent=4)


def load_from_json(filename):
    data = []
    with open(filename) as jsonfile:
        serialized_data = json.load(jsonfile)
        for item_data in serialized_data:
            if item_data['type'] == 'House':
                data.append(
                    House(item_data['name'], item_data['description'], item_data['price'], item_data['address']))
            elif item_data['type'] == 'Flat':
                data.append(
                    Flat(item_data['name'], item_data['description'], item_data['price'], item_data['floor']))
    return data
