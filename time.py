# time format
# 2021-12-16T13:30:00Z

import datetime
from datetime import timedelta

#current utc time
current_time = datetime.datetime.now()
print(f'\nCurrent time: {current_time}\n')

# print cisco friendly format in utc
print(current_time.strftime("%y-%m-%dT%H:%M:%SZ"))

duration = 30

endtime = current_time + timedelta(minutes=duration)

print(endtime.strftime("%Y-%m-%dT%H:%M:%SZ"))
print('-------')

start_time = '01:30'
current_time = datetime.datetime.utcnow()
utc_start = current_time.strftime("%Y-%m-%dT") + start_time + ":00Z"
utc_start_dtobj = datetime.datetime.strptime(utc_start, '%Y-%m-%dT%H:%M:%SZ')
utc_end_dtobj = utc_start_dtobj + timedelta(minutes=duration)
utc_end = utc_end_dtobj.strftime("%Y-%m-%dT%H:%M:%SZ")

print(f'Given start time: {start_time}, Duration: {str(duration)}')
print(f'utc_start: {utc_start}')
print(f'utc end: {utc_end}')