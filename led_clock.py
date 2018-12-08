import RPi.GPIO as GPIO
import time
from datetime import datetime
import requests
#from json import loads
##import random


class LEDcircle():

    def __init__(self):
        super().__init__()
        self.pins = []
        self.pwms = {}

    def init_pins(self):
        for i in range(len(self.pins)):
            GPIO.setup(self.pins[i], GPIO.OUT)
            GPIO.output(self.pins[i], GPIO.HIGH)
            self.pwms[str(i)] = GPIO.PWM(self.pins[i], 2**10)
            self.pwms[str(i)].start(0)

    def do_lighting(self,percent):
        tpercent = percent*len(self.pins)
        pinsp = [min(1,max(0,tpercent-x+1)) for x in range(1,len(self.pins)+1)]
        pinsp = [int(x*100) for x in pinsp]
        for i in range(len(self.pins)):   
            #pwms[str(i)] = pinsp[i]
            self.pwms[str(i)].ChangeDutyCycle(pinsp[i]) # I think this is the function
            
    def destroy(self):
        for i in range(len(self.pins)): 
            self.pwms[str(i)].stop()
            GPIO.output(self.pins[i], GPIO.LOW)

# for testing purposes
def do_lighting(percent):
    pins = [18,23]
    tpercent = percent*len(pins)   
    pwms = {}
    for i in range(len(pins)):
        pwms[str(i)] = 0    
    pinsp = [min(1,max(0,tpercent-x+1)) for x in range(1,len(pins)+1)]
    pinsp = [int(x*100) for x in pinsp]
    for i in range(len(pins)):   
        pwms[str(i)] = pinsp[i]
    return pwms


	
#if __name__ == '__main__':
 


sec_circle = LEDcircle()
sec_circle.pins = [18,23,24]
sec_circle.init_pins()

min_circle = LEDcircle()
min_circle.pins = []
min_circle.init_pins()

hour_circle = LEDcircle()
hour_circle.pins = []
hour_circle.init_pins()

day_circle = LEDcircle()
day_circle.pins = []
day_circle.init_pins()

 def destroy_all():
    # turn the power off to the pins
    sec_circle.destroy()
    min_circle.destroy()
    hour_circle.destroy()
    day_circle.destroy()
    GPIO.cleanup()


sih = 60*60
sid = sih*24

# set the actual time here
atime = "14:27:00"
atime = ""
try:
    # url = "http://worldclockapi.com/api/json/est/now"
    # thepage = requests.get(url)
    # atime = thepage.text.split("currentDateTime\":")[-1].split("\",\"")[0].split("T")[-1].split("-")[0] + ":" + time.strftime("%S")
    # ats = time.mktime(datetime.strptime(time.strftime("%Y.%m.%d") + "." + atime,"%Y.%m.%d.%H:%M:%S").timetuple())

    url = "https://www.timeanddate.com/worldclock/fullscreen.html?n=77"
    thepage = requests.get(url)
    atime = thepage.text.split("<div id=i_time>")[-1].split("</div>")[0][:8]
    ats = time.mktime(datetime.strptime(time.strftime("%Y.%m.%d") + "." + atime,"%Y.%m.%d.%H:%M:%S").timetuple())
except:
    try:
        ats = time.mktime(datetime.strptime(time.strftime("%Y.%m.%d") + "." + atime,"%Y.%m.%d.%H:%M:%S").timetuple())
    except:
        ats = time.time()

cts = time.time()
tsdif = ats - cts

# don't need this stuff
#sdif = tsdif + 0
#Hdif = int(tsdif/(60*60))
#sdif += - Hdif*60*60
#Mdif = int(sdif/(60))
#sdif += - Mdif*60
#Sdif = int(sdif)

try:
    while True:
        
        ts = str(time.time() + tsdif)
        ts_time = datetime.fromtimestamp(float(ts)).strftime("%H:%M:%S")

        H = ts_time.split(":")[0]
        M = ts_time.split(":")[1]
        S = ts_time.split(":")[2]
        MS = datetime.now().strftime("%f")
        
        cumulative_seconds = 0
        percents = []

        # percent through a second
        percents.append(int(MS)/1000000)
        cumulative_seconds += int(MS)/1000000
    
        # percent through a minute
        cumulative_seconds += int(S)
        percents.append((cumulative_seconds)/60) # / number of seconds in a minute

        # percent through an hour
        cumulative_seconds += int(M)*60
        percents.append((cumulative_seconds)/(sih)) # / number of seconds in an hour

        # percent through a day
        cumulative_seconds += int(H)*sih
        percents.append((cumulative_seconds)/(sid)) # / number of seconds in a day
        
        # actual calls for doing the lighting
        sec_circle.do_lighting(percents[0])
        min_circle.do_lighting(percents[1])
        hour_circle.do_lighting(percents[2])
        day_circle.do_lighting(percents[3])


        # for debugging
        # p_S = do_lighting(percents[0])
        # p_M = do_lighting(percents[1])
        # p_H = do_lighting(percents[2])
        # p_D = do_lighting(percents[3])
        # print(ts_time)
        # print(" ".join([str(p_S[x]) for x in p_S]).rjust(15) + " - percent " + str(percents[0]) + " - millisecond " + MS)
        # print(" ".join([str(p_M[x]) for x in p_M]).rjust(15) + " - percent " + str(percents[1]) + " - second " + S)
        # print(" ".join([str(p_H[x]) for x in p_H]).rjust(15) + " - percent " + str(percents[2]) + " - minute " + M)
        # print(" ".join([str(p_D[x]) for x in p_D]).rjust(15) + " - percent " + str(percents[3]) + " - hour " + H)
        #time.sleep(.5)


    
except KeyboardInterrupt:
    destroy_all()
    pass

