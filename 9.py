date = str(input())
time = str(input())

def sec_year(date,time):

    days_in_month = 0

    AMPM = time[2:4]
    month = int(date[0:2])
    day = int(date[3:5])
    year_full = int(date[6:10])
    HR = int(time[0:2])
    min = int(time[5:7])
    sec = int(time[8:12])

    if month == 1:
        days_in_month = 31
    if month == 2:
        days_in_month = 59
    if month == 3:
        days_in_month = 90
    if month == 4:
        days_in_month = 120
    if month == 5:
        days_in_month = 150
    if month == 6:
        days_in_month = 181
    if month == 7:
        days_in_month = 212
    if month == 8:
        days_in_month = 243
    if month == 9:
        days_in_month = 273
    if month == 10:
        days_in_month = 304
    if month == 11:
        days_in_month = 334
    if month == 12:
        days_in_month = 365

    if year_full % 4 == 0 and month > 1:
        days_in_month += 1

    if AMPM == 'PM':
        HR += 12

    days = day + days_in_month
    hours = days * 24 + HR
    mins = hours * 60 + min
    secs = mins * 60 + sec

    print(secs)

sec_year(date,time)