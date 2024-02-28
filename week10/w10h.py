from datetime import timedelta
import datetime
from calendar import monthrange
from math import ceil
import calendar


#: Possible dates
def midTerm( date_time_obj: datetime ):
    if date_time_obj.month == 1 and date_time_obj.day > 21: return 1
    if date_time_obj.month == 2 and date_time_obj.day < 21: return 1
    return 0
# method: weekOfMonth
# Returns the week of month
# @dt, datetime: The input
# @return, int: The output
# @completed
def weekOfMonth(date_time_obj: datetime) -> int:
    first_day = date_time_obj.replace(day=1)
    dom = date_time_obj.day
    adjusted_dom = dom + first_day.weekday()
    return int(ceil(adjusted_dom/7.0))

# method: lastFriday
# Returns the day index of the last friday
# @year, int: The input year
# @month, int: The input month
# @return, int: The output
# @completed
def lastFriday(year: int, month: int) -> int:
    return max(week[calendar.FRIDAY] for week in calendar.monthcalendar(year, month))

# method: firstMonday
# Returns the day index of the first monday
# @year, int: The input year
# @month, int: The input month
# @return, int: The output
# @completed
def firstMonday(year: int, month: int) -> int:
    return min(week[calendar.MONDAY] for week in calendar.monthcalendar(year, month))


#: Generic
LAMBDA_hour = lambda date_time_obj: date_time_obj.hour
LAMBDA_midnighttime = lambda date_time_obj: int(1 if date_time_obj.hour in [0,1,2,3,4,5,6] else 0)
LAMBDA_morningtime = lambda date_time_obj: int(1 if date_time_obj.hour in [7,8,9,10] else 0)
LAMBDA_noontime = lambda date_time_obj: int(1 if date_time_obj.hour in [11,12,13] else 0)
LAMBDA_afternoontime = lambda date_time_obj: int(1 if date_time_obj.hour in [14,15,16,17] else 0)
LAMBDA_eveningtime = lambda date_time_obj: int(1 if date_time_obj.hour in [18,19,20] else 0)
LAMBDA_nighttime = lambda date_time_obj: int(1 if date_time_obj.hour in [21,22,23] else 0)
LAMBDA_lunchtime = lambda date_time_obj: int(1 if date_time_obj.hour in [12,13,14] else 0)
LAMBDA_worktime1 = lambda date_time_obj: int(1 if date_time_obj.hour in [8,9,10,11,12,13,14,15,16,17] else 0)
LAMBDA_worktime2 = lambda date_time_obj: int(1 if date_time_obj.hour in [8,9,10,11,12,13,14,15,16] else 0)
LAMBDA_worktime3 = lambda date_time_obj: int(1 if date_time_obj.hour in [9,10,11,12,13,14,15,16,17] else 0)
LAMBDA_worktime4 = lambda date_time_obj: int(1 if date_time_obj.hour in [9,10,11,12,13,14,15,16] else 0)
LAMBDA_afterwork = lambda date_time_obj: int(1 if date_time_obj.hour in [18,19,20,21,22,23,0] else 0)
LAMBDA_justafterwork = lambda date_time_obj: int(1 if date_time_obj.hour in [18,19] else 0)
#: Around
ROW_asunrise = lambda date_time_obj, row: int(1 if abs( float(date_time_obj.hour) - row['tsunrise'] ) < 1.5 else 0)
ROW_anoon = lambda date_time_obj, row: int(1 if abs( float(date_time_obj.hour) - row['tnoon'] ) < 1.5 else 0)
ROW_asunset = lambda date_time_obj, row: int(1 if abs( float(date_time_obj.hour) - row['tsunset'] ) < 1.5 else 0)
#: Between
ROW_brisenoon = lambda date_time_obj, row: int(1 if float(date_time_obj.hour) > row['tsunrise'] and float(date_time_obj.hour) < row['tnoon'] else 0)
ROW_briseset = lambda date_time_obj, row: int(1 if float(date_time_obj.hour) > row['tsunrise'] and float(date_time_obj.hour) < row['tset'] else 0)
ROW_bnoonset = lambda date_time_obj, row: int(1 if float(date_time_obj.hour) > row['tnoon'] and float(date_time_obj.hour) < row['tset'] else 0)

#: The functions which require date only
LAMBDA_day = lambda date_time_obj: date_time_obj.day
LAMBDA_month = lambda date_time_obj: date_time_obj.month
LAMBDA_year = lambda date_time_obj: date_time_obj.year
LAMBDA_weekend = lambda date_time_obj: int(1 if date_time_obj.weekday() in [5,6] else 0)
LAMBDA_weekday = lambda date_time_obj: int(date_time_obj.weekday())
LAMBDA_weekOfYear = lambda date_time_obj: int(date_time_obj.isocalendar()[1])
LAMBDA_lastFriday = lambda date_time_obj: int(1 if lastFriday( date_time_obj.year, date_time_obj.month ) == date_time_obj.day else 0)
LAMBDA_firstMonday = lambda date_time_obj: int(1 if firstMonday( date_time_obj.year, date_time_obj.month ) == date_time_obj.day else 0)
LAMBDA_lastDays = lambda date_time_obj: int(1 if date_time_obj.day >= 25 else 0)
LAMBDA_firstDays = lambda date_time_obj: int(1 if date_time_obj.day <= 5 else 0)
LAMBDA_monthPercentage = lambda date_time_obj: float(float(date_time_obj.month) / 12.0)
LAMBDA_weeksInMonth = lambda date_time_obj: len(calendar.monthcalendar(date_time_obj.year, date_time_obj.month))
LAMBDA_dayOfYear = lambda date_time_obj: float(date_time_obj.timetuple().tm_yday) / 366.0
LAMBDA_summerBreak = lambda date_time_obj: int(1 if date_time_obj.month in [5,6,7,8] else 0)
LAMBDA_possibleMidTermBreak = lambda date_time_obj: midTerm( date_time_obj )
LAMBDA_middle = lambda date_time_obj: int(1 if date_time_obj.day in [14, 15, 16] else 0)
#: The functions which require the row
ROW_dayPercentage = lambda date_time_obj, row: float(row['@day']) / float(row['@daysInMonth'])
ROW_weekPercentage = lambda date_time_obj, row: float( row['@weekOfMonth'] ) / float(row['@weeksInMonth'])
ROW_lastDayFriday = lambda date_time_obj, row: 1 if row['@weekday'] == 4 and row['@day'] == row['@daysInMonth'] else 0

#! usage
df['day'] = df['date'].apply( LAMBDA_day )
df['month'] = df['date'].apply( LAMBDA_month )
