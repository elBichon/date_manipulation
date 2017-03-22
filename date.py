import math
import datetime
from time import gmtime, strftime

#this method will convert any given date in seconds
#into (dd/mm/aaaa)
def convert_second_to_date(second, datePattern):
    format_date = strftime("%b/%d/%Y", gmtime(float(second)))
    print(format_date)
    return format_date

#this method will convert any given date with the format(dd/mm/aaaa)
#into 3 variables, mois, anne, jour
def exctract_day_from_date(datetime):
    day = datetime[4:5]
    print(day)    
    return day

def exctract_month_from_date(datetime):
    month = datetime[0:3]
    if month == "Jan":
        month_num = 1
    elif month == "Feb":
        month_num = 2
    elif month == "Mar":
        month_num = 3
    elif month == "Apr":
        month_num = 4
    elif month == "May":
        month_num = 5
    elif month == "Jun":
        month_num = 6
    elif month == "Jul":
        month_num = 7
    elif month == "Aug":
        month_num = 8
    elif month == "Sep":
        month_num = 9
    elif month == "Oct":
        month_num = 10
    elif month == "Nov":
        month_num = 11
    elif month == "Dec":
        month_num = 12
    print(month_num)    
    return month_num

def exctract_year_from_date(datetime):
    year = datetime[5:6]
    print(year)    
    return year

#this methods will convert any date into the day of the week
#corresponding to this date
def convert_date_to_day(mois, annee, jour):
    c = 0

    if mois == 1:
        c = 1
    elif mois == 2:
        c = 1
    else:
        c = 0

    a = annee - c
    m = mois + 12*c - 2
    j = math.floor((jour + a + a/4 - a/100 + a/400 +(31*m)/12) % 7)

    if j == 0:
        day = "dimanche"
    elif j == 1:
        day = "lundi"
    elif j == 2:
        day = "mardi"
    elif j == 3:
        day = "mercredi"
    elif j == 4:
        day = "jeudi"
    elif j == 5:
        day = "vendredi"
    elif j == 6:
        day = "samedi"

    print(day)
    return day

#this method will convert any given day name (lundi, mardi...)
#into the corresponding period, week or week end
def convert_period(day_name):
    if day_name == "dimanche":
        period = "week_end"
    elif day_name == "samedi":
        period = "week_end"
    else:
        period = "week"

    print(period)
    return period



#implementation
day = "day"
period = "period"
format_date = "format_date"

exctract_month_from_date(convert_second_to_date("1390019818", "%b %d %Y"))
#convert_period(convert_date_to_day(1, 1994, 14))
