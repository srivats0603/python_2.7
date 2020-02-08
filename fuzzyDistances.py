import csv
from fuzzywuzzy import fuzz
import copy

bdDescListOr = []
actTaknList = []
bdToAct = {}
classifierDict = {}


def FuzzyRatios(bdDescList):
    targetSubRatio = 0
    if len(bdDescList) > 0:
        firstItem = bdDescList[0]
        bdDescList.remove(firstItem)
        for subNames in bdDescList:
            targetSubRatio = fuzz.ratio(firstItem,subNames)
            if targetSubRatio > 5:
                if firstItem not in classifierDict.keys():
                    classifierDict[firstItem] = []
                if subNames not in classifierDict[firstItem]:
                    classifierDict[firstItem].append(subNames)
                    #bdDescList.remove(subNames)
        #print len(bdDescList), "=length at now"
        FuzzyRatios(bdDescList)
    #print len(bdDescList), "=length at the end"
    return classifierDict

def main():
    eventFileName = r'C:\Users\ADMIN\PythonScripts\general examples\fuzzy distance\brk_down.csv'
    with open(eventFileName, 'rb') as eventData:
        eventBuffer = csv.DictReader(eventData)
        for row in eventBuffer:
            if row['BD Description'] not in bdDescListOr:
                bdDescListOr.append(row['BD Description'])
            if row['Action Taken'] not in actTaknList:
                actTaknList.append(row['Action Taken'])
            if row['BD Description'] not in bdToAct.keys():
                bdToAct[row['BD Description']] = []
            bdToAct[row['BD Description']].append(row['Action Taken'])
    eventData.close()
    bdDescList = copy.deepcopy(bdDescListOr)
    print len(bdDescList), "=length at start"
    FuzzyRatios(bdDescList)
    return
            

if __name__ == "__main__":
    print "calling main"
    main()
    print bdDescListOr[0:5]
    """print actTaknList[0:5]
    print bdToAct[bdDescList[2]]"""
    outpath = r'C:\Users\ADMIN\PythonScripts\general examples\fuzzy distance\brkDownRes5.csv'
    with open(outpath, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in classifierDict.items():
            writer.writerow([key, value])
