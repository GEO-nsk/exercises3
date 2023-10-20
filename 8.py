date = str(input())
time = str(input())

def str_change(date,time):
    Flag = True
    month = int(date[0:2])
    day = int(date[3:5])
    year1 = date[6:8]
    year_full = int(date[6:10])
    HR = int(time[0:2])
    AMPM = time[2:4]
    min = int(time[5:7])
    sec = int(time[8:12])

    if month > 12 or month < 1:
        Flag = False
    if day > 31 or day < 1:
        Flag = False
    if year_full > 2023 or year_full < 1:
        Flag = False
    if HR > 12 or month < 1:
        Flag = False
    if AMPM != 'AM' and AMPM != 'PM':
        Flag = False
    if min > 60 or year_full < 1:
        Flag = False
    if sec > 60 or month < 1:
        Flag = False

    if Flag:
        print(str(day)+'.'+str(month)+'.'+year1+time)

str_change(date,time)