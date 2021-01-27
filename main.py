from DbOperation import DBOperations
import csv
from utility import format_data

db = DBOperations()
db.create_DB()


def load_from_csv():
    data_to_load = []
    formatted_data = []
    with open("time_sheet.csv", "r", newline="") as my_data:
        reader = csv.DictReader(my_data)
        for row in reader:
            data_to_load.append(row)
    formatted_data = format_data(data_to_load)
    db.write_to_db(formatted_data)


# load_from_csv()


def read_from_db():
    data = db.read_from_db()
    print(data)


read_from_db()
