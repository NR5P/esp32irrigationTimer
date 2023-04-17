from machine import Pin
import time

class Irrigator:
    def __init__(self, name, startTime, secondsOn, minutesOn, pinNum) -> None:
        self.name = name # name of irrigator
        self.startTime = self._convertStringTimeToTime(startTime) # time seconds
        self.secondsOn = secondsOn # int
        self.minutesOn = minutesOn # int
        self.endTime = self._getEndTime(self.startTime, self.minutesOn, self.secondsOn) # time seconds
        self.pin = Pin(pinNum,Pin.OUT) 

    def irrigate(self):
        if self._shouldIBeRunning():
            self.pin.value(1)
        else:
            self.pin.value(0)

    def getCurrentState(self):
        return self._shouldIBeRunning()

    """
        takes in hh:mm in 24 hour format and converts to time gmt
    """
    def _convertStringTimeToTime(self, startTime):
        hour, minute = startTime.split(":")
        currentTimeTuple = time.gmtime(time.time())
        currentTimeList = list(currentTimeTuple)
        currentTimeList[3] = int(hour)
        currentTimeList[4] = int(minute)
        newTime = time.mktime(tuple(currentTimeList))
        return newTime

    def getTimeString(self):
        return str(time.gmtime(self.startTime)[3])+":"+str(time.gmtime(self.startTime)[4])

    """
        takes start time in seconds and run time in minutes and seconds and gets end time in seconds 
    """
    def _getEndTime(self, startTime, minutesOn, secondsOn):
        return startTime + (minutesOn * 60) + secondsOn

    def _resetSelfStartTimeForToday(self, startTime):
        oldTimeTuple = time.gmtime(startTime)
        currentTimeTuple = time.gmtime(time.time())
        currentTimeList = list(currentTimeTuple)
        currentTimeList[3] = oldTimeTuple[3]
        currentTimeList[4] = oldTimeTuple[4]
        self.startTime = time.mktime(tuple(currentTimeList))
        return self.startTime

    """
        return true or false if should be on or not
    """
    def _shouldIBeRunning(self):
        self._resetSelfStartTimeForToday(self.startTime)
        if time.time() >= self.startTime or time.time() <= self._getEndTime(self.startTime, self.minutesOn, self.secondsOn):
            return True
        return False

    

        

