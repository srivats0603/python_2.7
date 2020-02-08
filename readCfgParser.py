#read config file all lines

import ConfigParser

configFile = r'C:\Users\ADMIN\Documents\PythonScripts\generalexamples\config files\deployment_cfg2'
Config = ConfigParser.ConfigParser()
Config.read(configFile)

farmIDList = Config.get('SolarFarms','FarmIDs').split(',')
print farmIDList

for farmID in farmIDList:
    farmGeog = Config.get('FarmGeography',farmID).split(',')[0]
    farmCap = Config.get('FarmGeography',farmID).split(',')[1]
    print farmID,farmGeog,farmCap
