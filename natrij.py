from datetime import datetime
from datetime import timedelta

start = str(input())
detonate = str(input())
FMT = "%H:%M:%S"
countdown = datetime.strptime(detonate, FMT) - datetime.strptime(start, FMT)

if countdown.days < 0:
    countdown = timedelta(days=0, seconds=countdown.seconds, microseconds=countdown.microseconds)

printing = str(countdown)
if printing == "0:00:00":
    print("24:00:00")
elif len(printing) == 7:
    print("0"+printing)
else:
    print(printing)
