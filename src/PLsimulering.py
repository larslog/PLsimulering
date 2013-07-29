 # coding=utf-8
import numpy as np
import random_subset
import matplotlib.pyplot as plt

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

teams = 6


score1 = inputscores[0]
score2 = (inputscores[0]+inputscores[1])/2
score3 = (inputscores[0]+inputscores[1]+inputscores[2])/3
#score4 = (score2013+score2012+score2011+score2010)/4
#score5 = (score2013+score2012+score2011+score2010+score2009)/5
#score6 = (score2013+score2012+score2011+score2010+score2009+score2008)/6

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
	
print averagescores[2]
print score3
	



minrank = 11
simlength = 50000
maxrank = minrank + 2

simnr = 0
# TODO: legg alle team/totalscore/scorebins i en array med teams elementer. 
# vil støtte forskjellige antall lag. Bør være ganske rett frem med 
# en ekstra løkke og teamscore1.append(tempscore1) blir teamscores[1].append(tempscore1)
teamgroups = []
teamscore1 = []
teamscore2 = []
teamscore3 = []
teamscore4 = []
teamscore5 = []
teamscore6 = []
totalscore1 = []
totalscore2 = []
totalscore3 = []
totalscore4 = []
totalscore5 = []
totalscore6 = []
teamrank = []

while (simnr<simlength):
    temp = np.array(random_subset.random_subset(rank,teams))
    np.ndarray.sort(temp)
    tempind = temp-1
    tempscore1 = np.array(score1[tempind])
    tempscore2 = np.array(score2[tempind])
    tempscore3 = np.array(score3[tempind])
    tempscore4 = np.array(score4[tempind])
    tempscore5 = np.array(score5[tempind])
    tempscore6 = np.array(score6[tempind])
    tempscoretot1 = np.sum(tempscore1)
    tempscoretot2 = np.sum(tempscore2)
    tempscoretot3 = np.sum(tempscore3)
    tempscoretot4 = np.sum(tempscore4)
    tempscoretot5 = np.sum(tempscore5)
    tempscoretot6 = np.sum(tempscore6)
    if (np.mean(temp)>=minrank) and (np.mean(temp)<maxrank):
        teamgroups.append(temp)
        teamscore1.append(tempscore1)
        teamscore2.append(tempscore2)
        teamscore3.append(tempscore3)
        teamscore4.append(tempscore4)
        teamscore5.append(tempscore5)
        teamscore6.append(tempscore6)
        totalscore1 = np.append(totalscore1,tempscoretot1)
        totalscore2 = np.append(totalscore2,tempscoretot2)
        totalscore3 = np.append(totalscore3,tempscoretot3)
        totalscore4 = np.append(totalscore4,tempscoretot4)
        totalscore5 = np.append(totalscore5,tempscoretot5)
        totalscore6 = np.append(totalscore6,tempscoretot6)
        teamrank = np.append(teamrank,np.mean(temp))
        simnr +=1

# scoreave = np.mean(totalscore)
# scorestd = np.std(totalscore)
# scoresplit = np.max(totalscore)-np.min(totalscore)
# averagerank = np.mean(teamrank)
# scoremax = np.max(totalscore)

rankbins = np.arange(11,13.05,0.1)
binindex = np.digitize(teamrank,rankbins)
scorebins1 = {'temp':[]}
scorebins2 = {'temp':[]}
scorebins3 = {'temp':[]}
scorebins4 = {'temp':[]}
scorebins5 = {'temp':[]}
scorebins6 = {'temp':[]}

for n in range(len(rankbins)):
    scorebins1[n] =[]
    scorebins2[n] =[]
    scorebins3[n] =[]
    scorebins4[n] =[]
    scorebins5[n] =[]
    scorebins6[n] =[]
del scorebins1['temp']
del scorebins2['temp']
del scorebins3['temp']
del scorebins4['temp']
del scorebins5['temp']
del scorebins6['temp']

for i in range(len(totalscore1)):
    scorebins1[binindex[i]].append(totalscore1[i])
    scorebins2[binindex[i]].append(totalscore2[i])
    scorebins3[binindex[i]].append(totalscore3[i])
    scorebins4[binindex[i]].append(totalscore4[i])
    scorebins5[binindex[i]].append(totalscore5[i])
    scorebins6[binindex[i]].append(totalscore6[i])



# print('Minimum average rank:', minrank)
# print('Maximum average rank:', maxrank)
# print('Average rank:', averagerank)
# print('Average score:', scoreave)
# print('Score standard deviation:', scorestd)
# print('Difference between maximum and minimum score:', scoresplit)
# print('Number of team groups:', simlength)
# print('Max score:', scoremax)

#plt.figure(num=1)
# plt.subplot(311)
# plt.plot(teamrank,totalscore,'ro')
# plt.axis([2,18,400,900])
# plt.ylabel('Total score')
# plt.xlabel('Average team rank')
#  
# plt.subplot(312)
# plt.hist(teamrank,np.arange(0,20.5,0.5))
# plt.ylabel('Simulated combinations')
# plt.xlabel('Average team rank')
#  
# plt.subplot(313)

resolution=300
plt.figure(num=1)
plt.boxplot(scorebins1)
plt.setp(plt.gca(), 'xticklabels',rankbins)
plt.setp(plt.xticks()[1], rotation=90)
plt.title('Last season (12-13)')
plt.ylim([450,700])
plt.savefig('PLavg1.png',bbox_inches=0,dpi=resolution)
plt.clf()

plt.figure(num=2)
plt.boxplot(scorebins2)
plt.setp(plt.gca(), 'xticklabels',rankbins)
plt.setp(plt.xticks()[1], rotation=90)
plt.title('Average 2 last seasons (11-13)')
plt.ylim([450,700])
plt.savefig('PLavg2.png',bbox_inches=0,dpi=resolution)
plt.clf()

plt.figure(num=3)
plt.boxplot(scorebins3)
plt.setp(plt.gca(), 'xticklabels',rankbins)
plt.setp(plt.xticks()[1], rotation=90)
plt.title('Average 3 last seasons (10-13)')
plt.ylim([450,700])
plt.savefig('PLavg3.png',bbox_inches=0,dpi=resolution)
plt.clf()

plt.figure(num=4)
plt.boxplot(scorebins4)
plt.setp(plt.gca(), 'xticklabels',rankbins)
plt.setp(plt.xticks()[1], rotation=90)
plt.title('Average 4 last seasons (09-13)')
plt.ylim([450,700])
plt.savefig('PLavg4.png',bbox_inches=0,dpi=resolution)
plt.clf()

plt.figure(num=5)
plt.boxplot(scorebins5)
plt.setp(plt.gca(), 'xticklabels',rankbins)
plt.setp(plt.xticks()[1], rotation=90)
plt.title('Average 5 last seasons (08-13)')
plt.ylim([450,700])
plt.savefig('PLavg5.png',bbox_inches=0,dpi=resolution)
plt.clf()