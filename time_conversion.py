# Given a time in AM/PM format, convert it to military (-hour) time.
#
# Note: Midnight is  on a -hour clock, and  on a -hour clock. Noon is  on a -hour clock, and  on a -hour clock.
#
# Input Format
#
# A single string containing a time in -hour clock format (i.e.:  or ), where .
#
# Output Format
#
# Convert and print the given time in -hour format, where .
#
# Sample Input
#
# 07:05:45PM
# Sample Output
#
# 19:05:45


#!/bin/python

import sys


time = raw_input().strip()
time_zone = time[8:]
hrs,minutes,seconds=time[:8].split(":")


if(time_zone=="PM" and int(hrs) < 12):
    hrs = 12 + int(hrs)
if hrs == "12" and time_zone=="AM":
    hrs = "00"

final_output= str(hrs) + ":" + str(minutes) + ":" + str(seconds)

print final_output



