def add_time(start, duration, day="na"):
  #initialize variables
  day = day.lower()
  new_time_list = []
  dayspast = 0
  daystemp = 0
  newday = 0
  week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
  starttemp = 0
  startfull = 0
  durationtemp = 0
  durationfull = 0
  newtime = 0
  splittime = 0
  meridian = 0
  hours = 0
  minutes = 0
  x = 0

  #remove AM/PM from start time
  splittime = start.split()
  meridian = splittime[1]
  
  #turn start and duration into minutes
  starttemp = splittime[0].split(":", 1)
  startfull = (int(starttemp[0]) * 60) + int(starttemp[1])
  if (meridian == "PM"):
      startfull += 720

  durationtemp = duration.split(":", 1)
  durationfull = (int(durationtemp[0]) * 60) + int(durationtemp[1])
  
  #add duration to start
  new_time_full = durationfull + startfull

  #reduce hrs to days
  dayspast = int(new_time_full) // 1440
  new_time_full %= 1440
  
  #adjust meridian
  if (int(new_time_full) >= 720):
    meridian = "PM"
  elif (int(new_time_full) < 720):
    meridian = "AM"

  hours = (new_time_full // 60)
  if (hours > 12):
    hours -= 12
  if (hours == 0):
    hours = 12
  minutes = new_time_full % 60

  #check what day it is
  if(day != "na"):
    if (dayspast >= 7):
      daystemp = dayspast // 7
    if day in week:
      x = week.index(day)
    if (x + daystemp >= 7):
      daystemp -= 7
    newday = week[daystemp + x]
  
  #build list
  new_time_list.append(hours)
  new_time_list.append(str(minutes).zfill(2))
  new_time_list.append(meridian)
  new_time_list.append(newday)
  new_time_list.append(dayspast)
  
  #format time  
  newtime = str(new_time_list[0]) + ":" + str(new_time_list[1]) + " " + str(new_time_list[2])
  if (day != "na"):
    newtime = newtime + ", " + str(new_time_list[3])
  if (dayspast != 0):
    newtime = newtime + " (" + str(new_time_list[4]) + " days have passed)"
  return newtime
