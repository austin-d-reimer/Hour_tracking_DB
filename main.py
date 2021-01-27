from DbOperation import DBOperations
import csv
from utility import format_data, convert_user_date, convert_date_to_string, calculate_hours_worked

db = DBOperations()
db.create_DB()
dateformat = 'YYYY-MM-DD'


def load_from_csv():
    data_to_load = []
    formatted_data = []
    with open("time_sheet.csv", "r", newline="") as my_data:
        reader = csv.DictReader(my_data)
        for row in reader:
            data_to_load.append(row)
    formatted_data = format_data(data_to_load)
    db.write_to_db(formatted_data)


def read_from_db():
    data = db.read_from_db()
    print(data)


def manual_data_entry():
    date = convert_user_date(input(f'Date {dateformat}: '))
    startTime = input('Start time 10:00 am: ')
    endTime = input('End time 5:00 pm: ')
    location = input('Location: ')
    breakTime = int(input('Number of minutes on break: '))

    db.write_to_db([{
        'date': date,
        'startTime': startTime,
        'endTime': endTime,
        'location': location,
        'breakLength': breakTime
    }])


def read_rows():
    startDate = convert_user_date(input(f'startDate {dateformat}: '))
    endDate = convert_user_date(input(f'EndDate {dateformat}: '))
    results = db.get_rows_from_db(startDate, endDate)

    for row in results:
        date = convert_date_to_string(row[0])
        start = row[1]
        end = row[2]
        location = row[3]
        breakTime = row[4]
        hoursWorked = calculate_hours_worked(start, end, breakTime)
        print(
            f'{date}, {start}, {end}, {location}, {breakTime}, {hoursWorked}')


def getUserInput():
    print("""
    0. Exit
    1. Import Hours worked
    2. Read All from HoursWorkedDB
    3. Enter data for day worked
    4. Read data for hours worked from date to date.
    """)
    user_input = input("What task do you want to do? ")
    if user_input == "0":
        return
    elif user_input == "1":
        load_from_csv()
    elif user_input == "2":
        read_from_db()
    elif user_input == "3":
        manual_data_entry()
    elif user_input == "4":
        read_rows()
    else:
        print("Please enter a valid number")
    getUserInput()


getUserInput()
