import datetime
#import day_math

#Doomsday is at 03:14:07 UTC 19 Jan 2038

doomsday = datetime.datetime(2038, 1, 19, 3, 14, 7)
now = datetime.datetime.now()
clock = {
    "year": (doomsday.year - now.year) - 1,
    "month": ((doomsday.month - now.month) % 12) - 1,
    "day": (doomsday.day - now.day) - 1,
    "hour": ((doomsday.hour - now.hour) % 24) - 1,
    "minute": ((doomsday.minute - now.minute) % 60) - 1,
    "second": ((doomsday.second - now.second) % 60) - 1,
}

# Commented out because I'm still testing
# print(f"Year: {clock["year"]}, Month: {clock["month"]}, Day: {clock["day"]}, Hour: {clock["hour"]}, Minute: {clock["minute"]}, Second: {clock["second"]}")
