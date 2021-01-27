from datetime import datetime, timedelta


def convert_csv_date(inputDate):
    return int(datetime.strptime(inputDate, "%d %B %Y").timestamp())


def convert_user_date(inputDate):
    return int(datetime.strptime(inputDate, "%Y-%m-%d").timestamp())


def convert_date_to_string(inputStamp):
    return datetime.fromtimestamp(inputStamp).strftime("%Y-%m-%d")


def calculate_hours_worked(start, stop, breakTime):
    startTime = datetime.strptime(
        start, "%I:%M %p").hour, datetime.strptime(start, "%I:%M %p").minute
    stopTime = datetime.strptime(
        stop, "%I:%M %p").hour, datetime.strptime(stop, "%I:%M %p").minute
    return stopTime[0] - startTime[0] + (stopTime[1] - startTime[1]) / 60


def calculate_break(inputTime):
    hour = 0
    minute = 0
    if len(inputTime) == 5:
        hour = int(inputTime[0:2])
        minute = int(inputTime[-2])
    return hour * 60 + minute


def format_data(data_to_format):
    formatted_data = []
    for row in data_to_format:
        formatted_data.append(
            {
                "date": convert_csv_date(row["date"]),
                "startTime": row["start"],
                "endTime": row["stop"],
                "breakLength": calculate_break(row["break"]),
                "location": row["location"],
            }
        )
    return formatted_data
