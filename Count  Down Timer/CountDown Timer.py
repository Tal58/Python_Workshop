import time
def countdown(time_sec):
    while time_sec:
        min, sec = divmod(time_sec, 60)
        timeformat = f"{min} minutes and {sec} seconds have left"
        print(timeformat, end="\r")
        time.sleep(1)
        time_sec-=1
   
num = int(input("Set Your Timer in Sec : "))
countdown(num)