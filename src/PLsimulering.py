 # coding=utf-8
import numpy as np
import random_subset
import matplotlib.pyplot as plt
import sys

inputscores = []

rank = range(1,21)
points2013 = np.array([89,78,75,73,72,63,61,49,46,46,44,43,42,41,41,41,39,36,28,25])
goals2013 = np.array([86,66,75,72,66,55,71,53,47,45,41,50,34,49,47,45,41,47,43,30])
inputscores.append(points2013 + goals2013)

points2012 = np.array([89,89,70,69,65,64,56,52,52,47,47,47,45,45,43,38,37,36,31,25])
goals2012 = np.array([93,89,74,66,56,65,50,47,48,45,44,52,45,36,42,37,43,46,48,40])
inputscores.append(points2012 + goals2012)

points2011 = np.array([80,71,71,68,62,58,54,49,48,47,47,46,46,46,43,42,40,39,39,33])
goals2011 = np.array([78,69,60,72,55,59,51,49,48,45,56,56,46,52,46,40,46,37,55,43])
inputscores.append(points2011 + goals2011)

points2010 = np.array([86,85,75,70,67,64,63,61,50,50,47,46,44,39,38,36,35,30,30,28])
goals2010 = np.array([103,86,83,67,73,52,61,60,38,41,34,39,48,42,32,37,47,42,34,34])
inputscores.append(points2010+goals2010)

points2009 = np.array([90,86,83,72,63,62,53,51,51,50,45,45,41,41,41,36,35,34,32,32])
goals2009 = np.array([68,77,68,68,55,54,39,45,42,58,34,38,41,38,40,34,39,40,28,36])
inputscores.append(points2009+goals2009)

points2008 = np.array([90,86,83,72,63,62,53,51,51,50,45,45,41,41,41,36,35,34,32,32])
goals2008 = np.array([68,77,68,68,55,54,39,45,42,58,34,38,41,38,40,34,39,40,28,36])
inputscores.append(points2008+goals2008)

teams = 5

scores = []
averagescores = []
for n in range(0, teams):
	scores.append(inputscores[n])
	
for n in range(0,teams):
	average = scores[0]
	divider = 1
	for m in range(1, n+1):
		average = average + scores[m]
		divider = divider + 1
	averagescores.append(average/divider)


minrank = 11
if len(sys.argv) == 2: 
	simlength = sys.argv[0]
	maxrank = sys.argv[1]
else:
	simlength = 50000
	maxrank = minrank + 2

simnr = 0
# TODO: legg alle team/totalscore/scorebins i en array med teams elementer. 
# vil støtte forskjellige antall lag. Bør være ganske rett frem med 
# en ekstra løkke og teamscore1.append(tempscore1) blir teamscores[1].append(tempscore1)

teamgroups = []
teamscores = []
totalscores = []
for n in range(0, teams):
	totalscores.append([])
teamrank = []

while (simnr<simlength):
	temp = np.array(random_subset.random_subset(rank,teams))
	np.ndarray.sort(temp)
	tempind = temp - 1
	tempscoretotals = []
	tempscores = []
	for n in range(0, teams):
		tempscores.append(np.array(scores[n][tempind]))
		tempscoretotals.append(np.sum(tempscores[n]))

	if (np.mean(temp)>=minrank) and (np.mean(temp)<maxrank):
		teamgroups.append(temp)
		for n in range(0, teams):
			teamscores.append(tempscores[n])
			empty = []
			totalscores[n].append(np.append(empty,tempscoretotals[n]))
		teamrank = np.append(teamrank,np.mean(temp))
		simnr +=1

# scoreave = np.mean(totalscore)
# scorestd = np.std(totalscore)
# scoresplit = np.max(totalscore)-np.min(totalscore)
# averagerank = np.mean(teamrank)
# scoremax = np.max(totalscore)

rankbins = np.arange(11,13.05,0.1)
binindex = np.digitize(teamrank,rankbins)
scorebins = [{'temp':[]}]
for n in range(0, teams):
	scorebins.append({'temp':[]})

for m in range(0, teams):
	for n in range(len(rankbins)):
		scorebins[m][n] =[]

for m in range(0, teams):
	del scorebins[m]['temp']


for m in range(0, teams):	
	for i in range(len(totalscores[0])):
		scorebins[m][binindex[i]].append(totalscores[m][i])



newesttable = 13
maxscore = 100*teams + 150
minscore = 75*teams
for n in range(0, teams):
	title = "Season {0} - {1}, {2} teams and {3} simulations".format((newesttable-1)-n,newesttable-n, teams, simlength)
	resolution=300
	num = n+1
	plt.figure(num=num)
	plt.boxplot(scorebins[n])
	plt.setp(plt.gca(), 'xticklabels',rankbins)
	plt.setp(plt.xticks()[1], rotation=90)
	plt.title(title)
	plt.ylim([minscore,maxscore])
	file = 'PLscores' + str(n) + 'Teams' + str(teams) +'.png'
	plt.savefig(file,bbox_inches=0,dpi=resolution)
	plt.clf()
