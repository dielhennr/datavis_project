import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.cbook as cbook
import pandas as pd

def top_consumers_2014():
	ifile = open('energy.csv', 'r')

	states = {}

	for i in range(2755):
		ifile.readline()

	for line in ifile:

		line = line.split(',')
		state = line[-2]
		petrol_consumption = int(float(line[9]))

		if petrol_consumption > 4000:
			states[state] = petrol_consumption

	fig, ax = plt.subplots()


	y_pos = np.arange(len(states))
	x_pos = states.values()

	ax.barh(y_pos, x_pos, align='center',
	        color='blue')
	ax.set_yticks(y_pos)
	ax.set_yticklabels(states)
	ax.invert_yaxis() 
	ax.set_xlabel('Consumption\nUnits = 1 Billion British Thermal Units ~ 1055.06*billion Joules')
	ax.set_title('States with highest commercial liquid petroleum consumption in 2014')

	plt.show()
	ifile.close()

def cali_consumption():
	fig, ax = plt.subplots()
	ifile = open('energy.csv', 'r')

	cali_years = []
	nc_years = []

	ifile.readline()

	for line in ifile:
		line = line.split(",")
		if line[-2] == "California":
			petrol_consumption = int(float(line[9]))
			cali_years.append(petrol_consumption)

		elif line[-2] == "North Carolina":
			petrol_consumption = int(float(line[9]))
			nc_years.append(petrol_consumption)

	plt.hist(cali_years, bins = 10, histtype="step", fill=True, color= "green", label="North\nCarolina")
	plt.hist(nc_years, bins = 10, histtype="step", fill=False, color= "red", label="California")
	plt.legend()

	ax.set_xlabel('Commercial Consumption in Billion BTU')
	ax.set_ylabel('Years of this much consumption')
	ax.set_title("Commercial liquid petroleum consumption from 1960 - 2014")
	plt.show()
	ifile.close()

def cali_line():
	fig, ax = plt.subplots()
	ifile = open('energy.csv', 'r')

	cali_years = {}
	nocar_years = {}

	ifile.readline()

	for line in ifile:
		line = line.split(",")
		if line[-2] == "California":
			petrol_consumption = int(float(line[9]))
			cayear = int(line[-1])
			cali_years[cayear] = petrol_consumption

		elif line[-2] == "North Carolina":
			petrol_consumption = int(float(line[9]))
			ncyear = int(line[-1])
			nocar_years[ncyear] = petrol_consumption

	cali = plt.plot(list(cali_years.keys()), list(cali_years.values()), "o-", label="CA", color = "g")
	ncar = plt.plot(list(nocar_years.keys()), list(nocar_years.values()), "o-", label="NC", color = "m")
	plt.legend()
	ax.set_xlabel('Year')
	ax.set_ylabel('Commercial Consumption in Billion BTU')
	ax.set_title("Commercial liquid petroleum consumption in California and North Carolina\nFrom 1960 - 2014")
	plt.show()
	ifile.close()

	np.random.seed(0)

def us_totals():
	ifile = open('energy.csv', 'r')
	fig, ax = plt.subplots()

	ifile.readline()
	averages = {}
	previous = 1960
	wood_avg =coal_avg = lpg_avg = counter = 0
	for line in ifile:
		line = line.split(",")
		year = int(line[-1])
		if year == previous:
			counter += 1
			wood_avg += int(float(line[5]))
			coal_avg += int(float(line[6]))
			lpg_avg += int(float(line[9]))

		else:
			
			averages[int(previous)] = [wood_avg,coal_avg,lpg_avg]
			previous = year
			wood_avg = coal_avg = lpg_avg = counter = 0

	averages_list = list(averages.values())
	years_list = list(averages.keys())
	wood_avg_list = []
	coal_avg_list = []
	lpg_avg_list = []
	natgas_avg_list = []

	for i in averages_list:
		wood_avg_list.append(i[0])
		coal_avg_list.append(i[1])
		lpg_avg_list.append(i[2])
		

	plt.plot(years_list, wood_avg_list,  label = "Wood")
	plt.plot(years_list, coal_avg_list, label= "Coal", linestyle=":", linewidth = 3.)
	plt.plot(years_list, lpg_avg_list, label="LPG", linestyle = "--")
	ax.set_xlabel("Year")
	ax.set_ylabel("Energy consumed")
	ax.set_title("Wood, Coal, and LPG consumption in commercial sector\nUnits in billion BTU")
	plt.legend()

	plt.show()

	ifile.close()

def box_plot():
	ifile = pd.read_csv("energy.csv")
	ifile = ifile.tail(50)
	ifile.plot(kind="box", y='Consumption.Commercial.Liquefied Petroleum Gases', title="Commercial LPG Consumption in US during 2014\nEvery peice of data represents a state's consumption in Billion BTU")
	

	plt.show()

top_consumers_2014()
cali_consumption()
cali_line()
us_totals()
box_plot()
