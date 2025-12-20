import datetime

class YearRangeError(Exception):
    pass

def parse_date(year_str, month_str, day_str):
    # Attempt to convert strings to integers
    try:
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
    except ValueError:
        raise ValueError("Year, month, and day strings must contain integers.")
    
    # Validate that the year is between 1900 and 2100
    if year < 1900 or year > 2100:
        raise YearRangeError("Year must be between 1900 and 2100.")
    
    # Use datetime.date to validate and create the date
    # This will raise ValueError for invalid dates (e.g., April 31, month=13, day=0)
    try:
        date = datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date specified.")
    
    # Return the date as a string in format "YYYY-MM-DD"
    return date.strftime("%Y-%m-%d")

