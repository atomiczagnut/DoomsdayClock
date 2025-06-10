import datetime
from datetime import date

# Day Math... fighter of the Night Math...

# But seriously, the day_math function is nessecary because of the stupid way our calendar works
# Certain months have different days, there's leap years to account for, etc.
# This was probably the hardest part of coding this!

# So, for anyone studying this code in the future, you can't just call datetime.datetime.now().date()
# I don't know why, but for some reason, you have to store datetime.datetime.now() into a variable
# and then call now.date()

def day_math():
    doomsday = date(2038, 1, 19)
    now = datetime.datetime.now()
    now = now.date()

    delta = doomsday - now

    return(delta.days)

