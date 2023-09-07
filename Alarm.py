# Importing required libraries
from datetime import datetime,timedelta   #To set date and time
from playsound import playsound     #To play sound
print("------Welcome to Alarm Clock-------")
print("Current time: ",datetime.now())

alarm_hour = int(input("Enter hours: ")) #take hours input from user 
alarm_min = int(input("Enter minutes: ")) #take mins input from user
alarm_sec = int(input("Enter seconds: ")) #take secs input from user

total_alarm_minutes = int(alarm_hour * 60) + alarm_min # calculate and save total minutes for alert 
half_time = int(total_alarm_minutes/2)  # calculate and save half time 
before_time = int(total_alarm_minutes-5)  #75 calculate 2nd alert (5 mins before ending time)

print("Time Entered: ", total_alarm_minutes ,' mins')
print("Halftime time ringer: ", half_time ,' mins')
print("Before times end ringer: 5 mins")

#Alert function
def Alert(alertTime): 
    now = datetime.now() #get current date and time in the form of : 2023-11-24 03:15:00.000123
    alert_time = now + timedelta(minutes=alertTime)  # add alert minutes in the current date and time in the form of 2023-11-24 03:15:00.000123
    
    # extract and save the value of current hour,min and second
    alert_time_hour = alert_time.strftime("%I")  # E.g output: 03
    alert_time_min = alert_time.strftime("%M")   # E.g output: 15
    alert_time_sec = alert_time.strftime("%S")   # E.g output: 00

    print("Next alert at: ", alert_time_hour,':',alert_time_min) # print alert time E.g output: "Alert at: 03:15"
    
    # while loop will run until the current time not match with the alert time. When match, the alert sound will start.
    # The while loop will run on every second count until the time match. 
    while True:
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_sec = now.strftime("%S")
        if alert_time_hour == current_hour: # when hour match then it will check mins
            if alert_time_min == current_min: # when mins match then it will check secs
                if alert_time_sec == current_sec: # when secs match, alert will start(the alert time match here) 
                    print("Alerted at: ", current_hour,':',current_min) # E.g output: "Alert at: 03:20"
                    playsound('./alarm.wav') 
                    break        #break the loop after alert.

#Alert function called with halftime and before five minutes if mins >= 5.
Alert(half_time)
if total_alarm_minutes >= 5:
    Alert(before_time)
