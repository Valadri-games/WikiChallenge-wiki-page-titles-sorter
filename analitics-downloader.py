import json
import requests
import time

def openFile(fileName, mode):
    file = open(fileName, mode, encoding = "utf-8")
    return file

def readFile(file):
    return file.read()

def getLines(file):
    return file.readlines()

def readLine(fileLines, lineNumber):
    return fileLines[lineNumber]

def writeLine(file, string):
    file.write(string + '\n')

def writeFile(fileName, string):
    file = open(fileName, "w")
    file.write(string)
    file.close()

def closeFile(file):
    file.close()


def fetch(url):
    headers = {'User-Agent': 'TestBot/0.0 (https://example.org/TestBot/; TestBot@example.org)'}

    try:
        return requests.get(url = url, headers = headers).json()
    except Exception as e: 
        print(e)
        return False

def getStateData():
    stateFile = openFile("computed/state.json", "r+")
    stateDataJson = readFile(stateFile)
    closeFile(stateFile)

    return json.loads(stateDataJson)


def getIpnutData():
    inputDataParsed = openFile("data/parsed-titles-list.txt", "r")
    inputDataLines = getLines(inputDataParsed)
    closeFile(inputDataParsed)

    return inputDataLines


def getPageView(data):
    pageView = 0

    if data == False:
        return "Request error"

    if "items" not in data:
        return 0

    for monthData in data["items"]:
        pageView += monthData["views"]

    return pageView

def main():
    print('Loading state data')
    stateData = getStateData()

    print('Loading input data')
    inputDataLines = getIpnutData()

    print('Loading output file')
    outputFile = openFile("computed/computed.csv", "a+")

    running = True
    while running == True:
        for i in range(0, 100):
            title = inputDataLines[i + stateData['currentIndex']].strip()
            data = fetch("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/fr.wikipedia.org/all-access/user/" + title + "/monthly/20220101/20221231")

            pageView = getPageView(data)
            writeLine(outputFile, title + ";" + str(pageView))

        stateData['currentIndex'] += 100
        writeFile("computed/state.json", json.dumps(stateData))

    print('Done')

main()