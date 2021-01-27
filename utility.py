from datetime import datetime


def convert_date(inputDate):
    return datetime.strptime(inputDate, "%d %B %Y").strftime("%Y/%m/%d")


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
                "date": convert_date(row["date"]),
                "startTime": row["start"],
                "endTime": row["stop"],
                "breakLength": calculate_break(row["break"]),
                "location": row["location"],
            }
        )
    return formatted_data
