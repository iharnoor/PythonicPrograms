# Converts time in 12 hour format to 24 hours

def timeConversion(s):
    # Complete this function
    time = s.split(':')
    # print(ans)
    am_pm = time[2][2:4]
    hour = int(time[0])
    minute = int(time[1])
    sec = int(time[2][0:2])
    if am_pm == 'AM' and hour == 12:
        hour = 0
    elif am_pm == 'PM' and hour < 12:
        hour += 12
    hour = ("%02d" % hour)
    minute = ("%02d" % minute)
    sec = ("%02d" % sec)
    # return hour, ':', minute, ':', sec
    ans = str(hour) + ":" + str(minute) + ':' + str(sec)
    return ans

s = input().strip()
result = timeConversion(s)
