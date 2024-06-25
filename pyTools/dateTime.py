def isLeapYear(x):
    if x%400==0:
        return(1)
    if x%100==0:
        return(0)
    if x%4==0:
        return(1)
    return(0)

##for i in [1,2,300,400,2000,2020,2024,2025]:
##    print(isLeapYear(i))

from datetime import datetime
import pytz

def fetchDateTime(y=0):
    if y=="timeSpecific":
        return (datetime.now().time())
    if y=="time":
        return (datetime.now().time().strftime("%H:%M:%S"))
        # return (dateTime.strftime("%H:%M:%S"))
    if y=="date":
        return (datetime.now().date())
    if y is 0:
        return (datetime.now())

def fetchDateTime2(y,x="Asia/Kolkata"):
    tz = pytz.timezone(x)
    dateTime = datetime.now(tz)
    if y=="time":
        return (dateTime.strftime("%H:%M:%S"))
    if y=="date":
        return (dateTime)

print(fetchDateTime())

