import os
import time

def main():
    
    


# Blocks chosen apps for a set time period (E.G. 2 hours)
def block_duration( time_period_h = 0, time_period_m = 0 ):
    #This function will take in a time period and then when the block button is
    #pressed, the function will lock applications for that time period or until
    #the user decides to force unblocking
    #Function automatically assumes 0 for any values unless specified by caller.
    #That way, if user does not set one of the values, no error is given
    min_left = (time_period_h * 60) + time_period_m
    while( min_left <= 0 ):
        time.sleep(1)
        min_left -= 1
        print("Time left: ", min_left, " minutes.")
    
    


# Blocks chosen apps for a segment of time (E.G. 10:00 to noon)
def block_segment( start_hour, start_min, start_time_flag, end_hour, end_min, end_time_flag ):
    #Function checks to see if current time is equal to or later than the start time
    #If later, then funciton checks to see if current time is after end time. If not,
    #Function calls app_locking until time is equal to or later than end time
    localtime = time.localtime(time.time())
    print("Local time: ", localtime)
    
    
#  Dummy app_lock function
def app_lock():
    print("Locking")
    block_type = input("duration or segment? ")
    if( block_type == "duration" ):
        hours = int(input("Hours to block: "))
        minutes = int(input("Min to block: "))
        block_duration( hours, minutes )
    else: #segment
        start_h = int(input("Starting hour: "))
        start_m = int(input("Starting minute: "))
        start_ampm = input("am or pm: ")
        end_h = int(input("Ending hour: "))
        end_m = int(input("Ending minute: "))
        end_ampm = input("am or pm: ")
        if( start_ampm == "pm" ):
            start_h += 12
        if( end_ampm == "pm" ):
            end_h += 12
        
        
        
main()
