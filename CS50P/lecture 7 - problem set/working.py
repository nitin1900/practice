#solve by ai...

import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # The Regex Trap: 
    # (\d{1,2}) captures 1 or 2 digits for the hour
    # (?::(\d{2}))? captures an optional colon followed by exactly 2 digits for the minute
    # (AM|PM) captures the exact text AM or PM
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)
    
    # The Bouncer
    if not match:
        raise ValueError("Invalid format")

    # Step 1: Extract the Start Time variables
    start_hour = int(match.group(1))
    # If group 2 is None (e.g., "9 AM"), default the minutes to 0
    start_minute = int(match.group(2)) if match.group(2) else 0
    start_ampm = match.group(3)

    # Step 2: Extract the End Time variables
    end_hour = int(match.group(4))
    end_minute = int(match.group(5)) if match.group(5) else 0
    end_ampm = match.group(6)

    # Step 3: Validate the numbers make sense on a clock
    if start_hour > 12 or end_hour > 12 or start_minute >= 60 or end_minute >= 60:
        raise ValueError("Invalid time")

    # Step 4: 24-Hour Math Conversion
    start_hour_24 = format_24h(start_hour, start_ampm)
    end_hour_24 = format_24h(end_hour, end_ampm)

    # Step 5: Format the final string perfectly with leading zeros
    return f"{start_hour_24:02}:{start_minute:02} to {end_hour_24:02}:{end_minute:02}"

def format_24h(hour, ampm):
    """Helper function to convert a 12-hour clock integer to a 24-hour clock integer."""
    if ampm == "AM":
        if hour == 12:
            return 0  # 12 AM is 00:00
        return hour   # 1 AM to 11 AM stays the same
    else: # PM
        if hour == 12:
            return 12 # 12 PM is 12:00
        return hour + 12 # 1 PM to 11 PM adds 12

if __name__ == "__main__":
    main()