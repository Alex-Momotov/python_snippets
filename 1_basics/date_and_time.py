#%% datetime.date.today()
#   Returns today's date as date object (determined by laptop's current date)
import datetime
today = datetime.date.today()
print(today)
print(type(today))

#%% datetime.date(year,month,day)
#   Returns a date on a given day as date object.
#   day.year           Will only return year
#   day.month          Will only return month
#   day.day            Will only return day
#   day.weekday()      Will only return weekday (Mon - 0, Sun - 6)
#   day.isoweekday()   Will only return weekday (Mon - 1, Sun - 7)
import datetime
day = datetime.date(1995,10,28)
print(day)
print('year is:', day.year)
print('month is:', day.month)
print('day is:', day.day)
print('weekday is:', day.weekday())
print('isoweekday is:', day.isoweekday())

#%% datetime.timedelta(days=x)
#   This represents a desired difference in time as a timedelta object.
#   If we add or subtract timedelta to/from datetime object we will get a new datetime object.
#   If we add or subtract two datetime objects to/from each other we will get a timedelta.
#   day + timedelta        Will return new date shifted forward by timedelta.
#   day - timedelta        Will return new date shifted backward by timedelta.
import datetime
day = datetime.date(2000,1,7)
tdelta = datetime.timedelta(days=7)
print(day)
print(day - tdelta)
print(day + tdelta, '\n')

day2 = datetime.date(2000,10,28)
tdelta2 = day2 - day
print(tdelta2)

#%% Example of how to calculate number of days until your birthday
#   timedelta.days              Will only return number of dayy
#   timedelta.totalseconds()    Will return total number of seconds
import datetime
today = datetime.date.today()
bday = datetime.date(2018,10,28)
till_bday = bday - today
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

#%% datetime.time(hours, minutes, seconds, microseconds)
#   Returns a time object with specified time.
import datetime
time = datetime.time(23,59,45)
print(type(time))
print(time)
print(time.hour)
print(time.minute)

#%% datetime.datetime(year, month, day, hours, minutes, seconds, microseconds)
#   Returns a datetime object specifying both date and time.
import datetime
now = datetime.datetime(2017,12,31,23,59,59)
print(type(now))
print(now)
print(now.date())
print(now.time())
print(now.date().year)
print(now.time().hour)

#%% datetime.datetime.today()   Returns current local datetime object.
#   datetime.datetime.now()     Returns current local datetime object with the ability to shift to specific timezone.
import datetime
print(datetime.datetime.today())
print(datetime.datetime.now())

#%% Applying timedelta to datetime objects to shift both time and date.
import datetime
now = datetime.datetime(2017,12,30,22,59,59)
tdelta = datetime.timedelta(days=1, hours=1)
print(now+tdelta)

#%% pytz module allows to create time-zone aware datetime objects.
#   We need to pass tzinfo=pytz.UTC as a parameter to datetime constructor.
#   This results in the datetime having time-zone offset appended at the end.
import datetime
import pytz
dt = datetime.datetime(2020,12,31,23,59,59, tzinfo=pytz.UTC)
print(dt)

#%% datetime_obj.isoformat()
#   Allows to display datetime objects in iso format which is international standard.
import datetime
import pytz
dt = datetime.datetime(2017,12,30,22,59,59, tzinfo=pytz.UTC)
print(dt.isoformat())

#%% dt_obj.strftime(format)
#   Converts datetime object into any desirable string representation of date or time.
#   Check out https://docs.python.org/3/library/datetime.html table to see specific convertions.
import datetime
dt = datetime.datetime(2017,12,30,22,59,59)
dt_formated = dt.strftime('%d/%m/%Y\t%H:%M')
print(dt_formated)

#%% datetime.datetime.strptime(string, format)
#   Parses a given string and returns a datetime object using the specified format.
import datetime
text = '30/12/2017	22:59'
dt = datetime.datetime.strptime(text, '%d/%m/%Y\t%H:%M')
print(dt)

#%%
text = '4:59PM UTC'
dt = datetime.datetime.strptime(text, '%I:%M%p UTC').time().strftime('%H:%M')
print(dt)

