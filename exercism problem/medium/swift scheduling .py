#jitne bhi comment hai and now ko sab copy-paste kiya hai by gemini...

from datetime import datetime,timedelta
from calender import monthrange

date = input("Enter date (YYYY-MM-DD h): ")

d = datetime.fromisoformat(date)

code=input("Enter the abbreviation: ").upper()
match code:
    case "NOW":
        extra=timedelta(hours=2)
        d=d+extra
    case "ASAP":
    # Step 1: Check what time it is right now
        current_hour = d.hour

    # Step 2: If it is before noon (12:00)
        if current_hour < 12:
        # Delivery is TODAY at 17:00 (5:00 PM)
            year = d.year
            month = d.month
            day = d.day
        
            d = datetime(year, month, day, 17)

    # Step 3: If it is noon or later
        else:
        # Delivery is TOMORROW at 13:00 (1:00 PM)
            tomorrow = d + timedelta(days=1)
        
            year = tomorrow.year
            month = tomorrow.month
            day = tomorrow.day
        
            d = datetime(year, month, day, 13)
    case "EOW":
        # Step 1: Find out what day of the week it is (0-6)
        day_number = d.weekday()

        # Step 2: Is it Monday(0), Tuesday(1), or Wednesday(2)?
        if day_number <= 2:
            # We want to deliver on Friday (which is day 4)
            # Math: If today is Mon(0), we add 4 days. If today is Wed(2), we add 2 days.
            days_to_add = 4 - day_number
            
            # Fast-forward to Friday
            delivery_date = d + timedelta(days=days_to_add)
            
            # Set the exact time to 17:00
            year = delivery_date.year
            month = delivery_date.month
            day = delivery_date.day
            d = datetime(year, month, day, 17)

        # Step 3: It must be Thursday(3), Friday(4), Saturday(5), or Sunday(6)
        else:
            # We want to deliver on Sunday (which is day 6)
            days_to_add = 6 - day_number
            
            # Fast-forward to Sunday
            delivery_date = d + timedelta(days=days_to_add)
            
            # Set the exact time to 20:00
            year = delivery_date.year
            month = delivery_date.month
            day = delivery_date.day
            d = datetime(year, month, day, 20)
    case "Q1":
        # Q1 ends in March (Month 3)
        target_month = 3
        
        # Step 1: Get the last day of March.
        # monthrange gives us two numbers. We want the second one [1], which is total days.
        days_in_month = monthrange(d.year, target_month)[1]
        
        # Step 2: Build the target date (Last day of March at 08:00)
        delivery_date = datetime(d.year, target_month, days_in_month, 8)
        
        # Step 3: Did we miss the deadline? If today is past the delivery date, push to next year
        if d >= delivery_date:
            delivery_year = d.year + 1
            days_in_month = monthrange(delivery_year, target_month)[1]
            delivery_date = datetime(delivery_year, target_month, days_in_month, 8)
            
        # Step 4: If it lands on a weekend, push BACKWARD to Friday (unlike months which push forward)
        day_number = delivery_date.weekday()
        if day_number == 5: # Saturday
            delivery_date = delivery_date - timedelta(days=1) # Go back 1 day to Friday
        elif day_number == 6: # Sunday
            delivery_date = delivery_date - timedelta(days=2) # Go back 2 days to Friday
            
        d = delivery_date
    case "Q2":
        # Q1 ends in March (Month 3)
        target_month = 6
        
        # Step 1: Get the last day of March.
        # monthrange gives us two numbers. We want the second one [1], which is total days.
        days_in_month = monthrange(d.year, target_month)[1]
        
        # Step 2: Build the target date (Last day of March at 08:00)
        delivery_date = datetime(d.year, target_month, days_in_month, 8)
        
        # Step 3: Did we miss the deadline? If today is past the delivery date, push to next year
        if d >= delivery_date:
            delivery_year = d.year + 1
            days_in_month = monthrange(delivery_year, target_month)[1]
            delivery_date = datetime(delivery_year, target_month, days_in_month, 8)
            
        # Step 4: If it lands on a weekend, push BACKWARD to Friday (unlike months which push forward)
        day_number = delivery_date.weekday()
        if day_number == 5: # Saturday
            delivery_date = delivery_date - timedelta(days=1) # Go back 1 day to Friday
        elif day_number == 6: # Sunday
            delivery_date = delivery_date - timedelta(days=2) # Go back 2 days to Friday
            
        d = delivery_date
    case "Q3":
        # Q1 ends in March (Month 3)
        target_month = 9
        
        # Step 1: Get the last day of March.
        # monthrange gives us two numbers. We want the second one [1], which is total days.
        days_in_month = monthrange(d.year, target_month)[1]
        
        # Step 2: Build the target date (Last day of March at 08:00)
        delivery_date = datetime(d.year, target_month, days_in_month, 8)
        
        # Step 3: Did we miss the deadline? If today is past the delivery date, push to next year
        if d >= delivery_date:
            delivery_year = d.year + 1
            days_in_month = monthrange(delivery_year, target_month)[1]
            delivery_date = datetime(delivery_year, target_month, days_in_month, 8)
            
        # Step 4: If it lands on a weekend, push BACKWARD to Friday (unlike months which push forward)
        day_number = delivery_date.weekday()
        if day_number == 5: # Saturday
            delivery_date = delivery_date - timedelta(days=1) # Go back 1 day to Friday
        elif day_number == 6: # Sunday
            delivery_date = delivery_date - timedelta(days=2) # Go back 2 days to Friday
            
        d = delivery_date
    case "Q4":
        # Q1 ends in March (Month 3)
        target_month = 12
        
        # Step 1: Get the last day of March.
        # monthrange gives us two numbers. We want the second one [1], which is total days.
        days_in_month = monthrange(d.year, target_month)[1]
        
        # Step 2: Build the target date (Last day of March at 08:00)
        delivery_date = datetime(d.year, target_month, days_in_month, 8)
        
        # Step 3: Did we miss the deadline? If today is past the delivery date, push to next year
        if d >= delivery_date:
            delivery_year = d.year + 1
            days_in_month = monthrange(delivery_year, target_month)[1]
            delivery_date = datetime(delivery_year, target_month, days_in_month, 8)
            
        # Step 4: If it lands on a weekend, push BACKWARD to Friday (unlike months which push forward)
        day_number = delivery_date.weekday()
        if day_number == 5: # Saturday
            delivery_date = delivery_date - timedelta(days=1) # Go back 1 day to Friday
        elif day_number == 6: # Sunday
            delivery_date = delivery_date - timedelta(days=2) # Go back 2 days to Friday
            
        d = delivery_date
    case _:
        # Step 1: Extract the number. "3M"[:-1] chops off the "M" and leaves "3"
        month_text = code[:-1]
        target_month = int(month_text)

        # Step 2: Figure out the year. If we are already in or past that month, push to next year.
        current_year = d.year
        current_month = d.month

        if current_month >= target_month:
            delivery_year = current_year + 1
        else:
            delivery_year = current_year

        # Step 3: Set delivery to the 1st of that month at 08:00 (8:00 AM)
        delivery_date = datetime(delivery_year, target_month, 1, 8)

        # Step 4: No weekend deliveries! If the 1st is a Saturday(5) or Sunday(6), move FORWARD to Monday
        day_number = delivery_date.weekday()
        if day_number == 5: # Saturday
            delivery_date = delivery_date + timedelta(days=2) # Jump forward 2 days
        elif day_number == 6: # Sunday
            delivery_date = delivery_date + timedelta(days=1) # Jump forward 1 day

        d = delivery_date
print(d)


#solution:

from datetime import datetime, time, timedelta
from calendar import FRIDAY, SATURDAY, SUNDAY, WEDNESDAY, monthrange


def dt(d, h):
    return datetime(d.year, d.month, d.day, h)


def delivery_date(start, description):
    d = datetime.fromisoformat(start)
    match description:
        case "NOW": d += timedelta(hours=2)
        case "ASAP" if d.hour < 12: d = dt(d, 17)
        case "ASAP": d = dt(d + timedelta(days=1), 13)
        case "EOW" if d.weekday() <= WEDNESDAY: d = dt(d + timedelta(days=FRIDAY - d.weekday()), 17)
        case "EOW": d = dt(d + timedelta(days=SUNDAY - d.weekday()), 20)
        case "Q1": d = q(d, 1)
        case "Q2": d = q(d, 2)
        case "Q3": d = q(d, 3)
        case "Q4": d = q(d, 4)
        case _: # <N>M
            m = int(description[:-1])
            d = datetime(d.year + (d.month >= m), m, 1, 8)
            if d.weekday() >= SATURDAY:
                d += timedelta(days=7 - d.weekday())  # Next Monday
    return d.isoformat()


def q(d, q_idx):
    m = 3 * q_idx
    ans = datetime(d.year, m, monthrange(d.year, m)[1], 8)
    if d >= ans:
        ans = datetime(d.year + 1, m, monthrange(d.year, m)[1], 8)
    if ans.weekday() >= SATURDAY:
        ans -= timedelta(days=ans.weekday() - FRIDAY)  # Prev Friday
    return ans
