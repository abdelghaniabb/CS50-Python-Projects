import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression to match the 12-hour time format
    pattern = r'^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$'
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # If minute is None, set it to "00"
    start_minute = start_minute or "00"
    end_minute = end_minute or "00"

    # Convert start time
    start_24 = to_24_hour_format(start_hour, start_minute, start_period)
    # Convert end time
    end_24 = to_24_hour_format(end_hour, end_minute, end_period)

    return f"{start_24} to {end_24}"

def to_24_hour_format(hour, minute, period):
    hour = int(hour)
    minute = int(minute)

    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    if hour > 23 or minute > 59:
        raise ValueError("Invalid time")

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
