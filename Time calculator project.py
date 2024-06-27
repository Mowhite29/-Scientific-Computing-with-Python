#Build a Time Calculator Project
#
#Write a function named add_time that takes in two required parameters and one
#optional parameter:
# -A start time in the 12-hour clock format (ending in AM or PM);
# -A duration time that indicates the number of hours and minutes;
# -(Optional) a starting day of the week, case insensitive;
#
#The function should add the duration time to the start time and return the
# result.
#
#If the result will be the next day, it should show (next day) after the time.
#If the result will be more than one day later, it should show (n days later)
# after the time, where "n" is the number of days later.
#
#If the function is given the optional starting day of the week parameter, then
# the output should display the day of the week of the result. The day of the
# week in the output should appear after the time and before the number of days
# later.
#
#Below are some examples of different cases the function should handle. Pay
# close attention to the spacing and punctuation of the results.
#
#add_time('3:00 PM', '3:10')
# Returns: 6:10 PM
#
#add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday
#
#add_time('11:43 AM', '00:20')
# Returns: 12:03 PM
#
#add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)
#
#add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)
#
#add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
#
#Do not import any Python libraries. Assume that the start times are valid
# times. The minutes in the duration time will be a whole number less than 60,
# but the hour can be any whole number.


def add_time(start, duration, day=None):
    start_hours = int(start[:-6])
    start_minutes = int(start[-5:-3])
    start_period = start[-2:]

    duration_hours = int(duration[:-3])
    duration_minutes = int(duration[-2:])
    new_day = ''

    new_minutes = start_minutes + duration_minutes

    if new_minutes >= 60:
        duration_hours += new_minutes // 60
        new_minutes = new_minutes % 60

    if len(str(new_minutes)) != 2:
        new_minutes = f'0{new_minutes}'

    new_hours = start_hours + duration_hours
    remainder = new_hours % 12
    cycles = new_hours // 12
    days = new_hours // 24 

    if remainder == 0:
        remainder = 12
    
    if start_period == 'PM' and cycles > 1:
        days += 1

    while day != None:
        days_of_week = {
            'monday' : 1,
            'tuesday' : 2,
            'wednesday' : 3,
            'thursday' : 4,
            'friday' : 5,
            'saturday' : 6,
            'sunday' : 7
        }
        start_day = days_of_week[day.lower()]
        index = start_day + days % 7
        while index > 6:
            index -= 7
        new_day = list(days_of_week)[index - 1]
        new_day = f', {new_day.title()}'
        break

    if cycles == 0:
        new_time = f'{remainder}:{new_minutes} {start_period}{new_day}'
    elif cycles == 1:
        if start_period == 'AM':
            new_time = f'{remainder}:{new_minutes} PM{new_day}'
        else:
            new_time = f'{remainder}:{new_minutes} AM{new_day} (next day)'
    elif cycles == 2:
        new_time = f'{remainder}:{new_minutes} {start_period}{new_day} (next day)'
    elif cycles % 2 != 0:
        if start_period == 'AM':
            new_time = f'{remainder}:{new_minutes} PM{new_day} ({days} days later)'
        elif start_period == 'PM':
            new_time = f'{remainder}:{new_minutes} AM{new_day} ({days} days later)'
    else:
        new_time = f'{remainder}:{new_minutes} {start_period}{new_day} ({days} days later)'



    print(new_time)
    return(new_time)

add_time('8:16 PM', '466:02', 'tuesday') 
