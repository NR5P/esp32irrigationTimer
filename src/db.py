from IrrigatorModel import Irrigator
import ujson

class DB:
    def __init__(self) -> None:
        pass

    """
        returns a list of Irrigators in db 
    """
    def getIrrigators(self):
        irrigators = []
        with open("db.json") as reader:
            jsonData = ujson.load(reader)
        for irrigator in jsonData["timerSettings"]:
            irrigators.append(Irrigator(irrigator["name"],irrigator["startTime"],irrigator["secondsOn"],irrigator["minutesOn"], irrigator["pinNum"]))
        print(irrigators)
        return irrigators
    
    def getState(self):
        with open("db.json") as reader:
            jsonData = ujson.load(reader)
        return jsonData["generalSettings"]["on"]

    def getLocation(self):
        with open("db.json") as reader:
            jsonData = ujson.load(reader)
        return jsonData["generalSettings"]["location"]

    def getWifiPassword(self):
        with open("db.json") as reader:
            jsonData = ujson.load(reader)
        return jsonData["generalSettings"]["wifiPassword"]

    def saveData(self, irrigatorList):
        d = {
                "generalSettings" : {
                    "on" : self.getState(),
                    "location" : self.getLocation(),
                    "wifiPassword" : self.getWifiPassword()
                },
                "timerSettings" : [
                    {
                        "name" : irrigatorList[0].name,
                        "minutesOn" : irrigatorList[0].minutesOn,
                        "secondsOn" : irrigatorList[0].secondsOn,
                        "startTime" : irrigatorList[0].startTime,
                        "pinNum" : irrigatorList[0].pinNum
                    },
                    {
                        "name" : irrigatorList[1].name,
                        "minutesOn" : irrigatorList[1].minutesOn,
                        "secondsOn" : irrigatorList[1].secondsOn,
                        "startTime" : irrigatorList[1].startTime,
                        "pinNum" : irrigatorList[1].pinNum
                    },
                    {
                        "name" : irrigatorList[2].name,
                        "minutesOn" : irrigatorList[2].minutesOn,
                        "secondsOn" : irrigatorList[2].secondsOn,
                        "startTime" : irrigatorList[2].startTime,
                        "pinNum" : irrigatorList[2].pinNum
                    }
                ]
        }
        with open('db.json', 'w', encoding ='utf8') as json_file:
            ujson.dump(d, json_file)









