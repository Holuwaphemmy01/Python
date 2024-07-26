def seconds_since_midnight(hour, minute, second):
 	hour_in_seconds = hour * 3600
 	minute_in_seconds = minute * 60
 	result = hour_in_seconds + minute_in_seconds + second
 	return result 
print(seconds_since_midnight(13, 30, 45))
print(seconds_since_midnight(14, 45, 17))
