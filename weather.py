import csv
import math

months = []
temp = []
countTable = []

with open('weather.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count =0;
    for row in csv_reader:
        if count != 0:
            months.append(int(row[0]))
            temp.append(int(row[1]))
            countTable.append(int(row[2]))
        count =1

probabilities = [count / sum(countTable) for count in countTable]


# Uncertainty of the temperature

tempProbabilities = []
#tempProbabilities[5] = a  --> a is the probability of 2 degrees happening

for tempreture in range(-3,29):
	tempTotal = 0
	for i in range(130):
		if(tempreture == temp[i]):
			tempTotal +=  probabilities[i]
	tempProbabilities.append(tempTotal)


hx = []
for p in tempProbabilities:
	hx.append(p*math.log2(p)*-1)
h = sum(hx)

print("Uncertainty of the Temperature: ")
print(str(h) + " bits")

# Joint entropy of temperature and month

jointEntholpy =0
for month in range(1,13):
	monthTotal =0
	for i in range(130):
		if months[i] == month:
			#print(str(months[i]) + " " + str(temp[i]) + " " + str(countTable[i]) + " " + str(probilities[i]))
			monthTotal += probabilities[i]*math.log2(probabilities[i])*(-1)
	jointEntholpy += monthTotal

print("Joint entropy of temperature and month: ")
print(str(jointEntholpy) + " bits")






