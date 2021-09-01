from collections import Counter
import csv

with open('height-weight.csv', newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
weightData = []

for x in range(len(fileData)):
    weightNumber = fileData[x][2]
    weightData.append(float(weightNumber))

def mean():
    divisor = len(weightData)
    weightTotal = 0

    for y in weightData:
        weightTotal += y

    meanWeight = weightTotal/divisor

    print(f"The mean weight is {meanWeight}.")

def median():
    length = len(weightData)
    weightData.sort()

    if length % 2 == 0:
        medianWeight = (weightData[length//2] + weightData[length//2 - 1])/2
    else:
        medianWeight = float(weightData[length//2])

    print(f"The median weight is {medianWeight}.")

def mode():
    weightData2 = Counter(weightData)

    weightModeData = {
        "90-100": 0,
        "100-110": 0,
        "110-120": 0,
        "120-130": 0,
        "130-140": 0,
        "140-150": 0,
        "150-160": 0,
        "160-170": 0,
        "170-180": 0
    }

    for weight, occurence in weightData2.items():
        if 90 < float(weight) < 100:
            weightModeData["90-100"] += occurence
        elif 100 < float(weight) < 110:
            weightModeData["100-110"] += occurence
        elif 110 < float(weight) < 120:
            weightModeData["110-120"] += occurence
        elif 120 < float(weight) < 130:
            weightModeData["120-130"] += occurence
        elif 130 < float(weight) < 140:
            weightModeData["130-140"] += occurence
        elif 140 < float(weight) < 150:
            weightModeData["140-150"] += occurence
        elif 150 < float(weight) < 160:
            weightModeData["150-160"] += occurence
        elif 160 < float(weight) < 170:
            weightModeData["160-170"] += occurence
        elif 170 < float(weight) < 180:
            weightModeData["170-180"] += occurence

    weightModeRange, weightModeOccurence = 0, 0

    for numberRange2, occurence2 in weightModeData.items():
        if occurence2 > weightModeOccurence:
            weightModeRange, weightModeOccurence = [int(numberRange2.split("-")[0]), int(numberRange2.split("-")[1])], occurence2

    weightMode = float((weightModeRange[0] + weightModeRange[1])/2)

    print(f"The mode of the weights is {weightMode:2f}.")

choice = input('Please enter what you would like to calculate - "mean", "median", or "mode": ')

if choice == "mean":
    mean()
elif choice == "median":
    median()
elif choice == "mode":
    mode()
else:
    print('Please enter something compatible with the program.')

print('Please restart the program to find out something else.')