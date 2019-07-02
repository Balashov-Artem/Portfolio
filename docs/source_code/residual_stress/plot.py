import matplotlib.pyplot as plt


AS463 =		{'name': 'AS463', 	  'E1': 147.0e3, 'E2': 10.3e3, 'G12': 7.0e3,'mu12': 0.27, 'd': 0.12, 'dens': 1580e-6}
IM6 = 		{'name': 'IM6', 	  'E1': 177.0e3, 'E2': 10.8e3, 'G12': 7.6e3,'mu12': 0.27, 'd': 0.15, 'dens': 1600e-6}
Mod = 		{'name': 'Mod', 	  'E1': 216.0e3, 'E2': 5.00e3, 'G12': 4.5e3,'mu12': 0.25, 'd': 0.16, 'dens': 1540e-6}
GY70 = 		{'name': 'GY70', 	  'E1': 294.0e3, 'E2': 6.40e3, 'G12': 4.9e3,'mu12': 0.23, 'd': 0.10, 'dens': 1590e-6}
AS458 = 	{'name': 'AS458', 	  'E1': 131.0e3, 'E2': 8.70e3, 'G12': 5.0e3,'mu12': 0.28, 'd': 0.15, 'dens': 1570e-6}
AGP370_5H = {'name': 'AGP3705H',  'E1': 77.00e3, 'E2': 75.0e3, 'G12': 6.5e3,'mu12': 0.06, 'd': 0.42, 'dens': 1600e-6}
CF0604 =	{'name': 'CF0604', 	  'E1': 62.60e3, 'E2': 60.3e3, 'G12': 3.9e3,'mu12': 0.04, 'd': 0.30, 'dens': 1560e-6}
E_glass55=	{'name': 'E_glass55', 'E1': 41.00e3, 'E2': 10.4e3, 'G12': 4.3e3,'mu12': 0.28, 'd': 0.08, 'dens': 1970e-6}
E_glass45=	{'name': 'E_glass45', 'E1': 39.00e3, 'E2': 8.60e3, 'G12': 3.8e3,'mu12': 0.28, 'd': 0.15, 'dens': 2100e-6}
S_glass55=	{'name': 'S_glass55', 'E1': 43.00e3, 'E2': 8.90e3, 'G12': 4.5e3,'mu12': 0.27, 'd': 0.15, 'dens': 2000e-6}
Style = 	{'name': 'Style', 	  'E1': 29.70e3, 'E2': 29.7e3, 'G12': 5.3e3,'mu12': 0.17, 'd': 0.25, 'dens': 2200e-6}
M10E = 		{'name': 'M10E', 	  'E1': 24.50e3, 'E2': 23.8e3, 'G12': 4.7e3,'mu12': 0.11, 'd': 0.22, 'dens': 9100e-6}
Kevlar49 = 	{'name': 'Kevlar49',  'E1': 80.00e3, 'E2': 5.50e3, 'G12': 2.2e3,'mu12': 0.34, 'd': 0.15, 'dens': 1380e-6}
K120 = 		{'name': 'K120', 	  'E1': 29.00e3, 'E2': 23.0e3, 'G12': 1.8e3,'mu12': 0.05, 'd': 0.22, 'dens': 1380e-6}

materials_list = [AS463, IM6, Mod, GY70, AS458, AGP370_5H, CF0604, E_glass55, E_glass45, S_glass55, 
	Style, M10E, Kevlar49, K120]


def parser_res (res_file='abaqus.rpt'):

	results = {}
	results_l = []
	counter = 1 # it will count amount of proc iteration

	with open(res_file, 'r') as res:
		for line in res:
			lstrip = line.lstrip() #delete spaces ' '
		
			if lstrip[0:7] == 'Maximum': #find line with 'Maximum'
				tot = lstrip[7:].split(' ') #delete 'Maximum' and convert it to
				#list 'tot'
				for i in range(len(tot)):
					if '' in tot: tot.remove('') #delete an empty ('') elements in list
					if '\n' in tot: tot.remove('\n') #delete an ('/n') element if exist
			
				tot = [float(i) for i in tot]	#convert elements in 'tot' from string to list
				results[counter] = max(tot)
				results_l.append(max(tot))
				counter += 1

	return results_l

results = parser_res()
counter = 0





#	Work 1

materials_pressure = {}
for i in range(len(materials_list)):

	mat_pres_res = []
	n_name = materials_list[i]['name']

	for p in range(20):
		
		mat_pres_res.append(results[counter])
		counter += 1
	materials_pressure[n_name] = mat_pres_res


print('materials_pressure')
for i in materials_pressure:
	print(i, materials_pressure[i])

print('simlations = ', counter)
print()
print()


#	Work 2
orientation_res = {}
for i in range(0, 91, 5):
	mat_pres_res = []

	n_name = materials_list[2]['name'] + '_'+ str(i) + '°'
	for p in range(10):

		mat_pres_res.append(results[counter])
		counter += 1
	orientation_res[n_name] = mat_pres_res


print('orientation_res')
for i in orientation_res:
	print(i, orientation_res[i])
print('simlations = ', counter)
print()
print()





#	Work 3

pressure_res = {}
for nz in [0.05, 0.1, 0.25, 0.5, 1]:

	#nz_res = {}	

	for p in range(10):

		p_res = []
		for d in range(10):


			P0 = 200 + p*20

			n_name = str(materials_list[5]['name']) + '_' + str(nz) + '_' + str(P0) + '_MPa'

			p_res.append(results[counter])
			counter += 1

		pressure_res[n_name] = p_res
		#nz_res.append(p_res)

print('pressure_res')
for i in pressure_res:
	print(i, pressure_res[i])


#plot 1

x1 = range(200, 400, 10)
y1 = materials_pressure['AGP3705H']
plt.xlabel('Pressure, MPa')
plt.ylabel('Principal stress, MPa')
plt.title('Material:=  AGP-3705H')
plt.margins(0, 1)
plt.plot(x1, y1)
plt.show()


#plot 2
x2 = range(200, 400, 20)
y21 = orientation_res['Mod_0°']
y22 = orientation_res['Mod_45°']
plt.xlabel('Pressure, MPa')
plt.ylabel('Principal stress, MPa')
plt.title('Material:=  Mod')
plt.plot(x2, y21, label = 'Orientation_0°')
plt.plot(x2, y22, label = 'Orientation_45°')
plt.legend()
plt.show()


#plot 3
x3 = range(0, 95, 5)
y3 = [orientation_res[i][8] for i in orientation_res]
plt.xlabel('Orientation, °')
plt.ylabel('Principal stress, MPa')
plt.title('Pressure distribution per orientation')
plt.plot(x3, y3)
plt.show()


#plot 4
x4 = range(len(materials_list))
y4 = [materials_pressure[i][8] for i in materials_pressure]
plt.xlabel('Materials')
plt.ylabel('Principal stress, MPa')
plt.title('Pressure distribution per different materials')
plt.plot(x4, y4)
plt.show()

#plot 5
x5 = range(10, 110, 10)
y5 = pressure_res['AGP3705H_0.25_300_MPa']
plt.xlabel('Working distance')
plt.ylabel('Principal stress, MPa')
plt.title('AGP3705H_0.25_30_MPa')
plt.plot(x5, y5)
plt.margins(0, 0.1)
plt.show()

'''
#plot 5.2
x5 = range(10, 110, 10)
y5 = pressure_res['AGP3705H_0.05_300_MPa']
plt.xlabel('Working distance')
plt.ylabel('Principal stress, MPa')
plt.title('Pressure distribution according to working distance')
plt.plot(x5, y5)
plt.margins(0, 0.1)
plt.show()
'''

x6 = [0.05, 0.1, 0.25, 0.5, 1]
y6 = [pressure_res[i][1] for i in pressure_res][5::10]
plt.xlabel('Nozzle diameters')
plt.ylabel('Principal stress, MPa')
plt.title('Pressure = 30 MPa')
plt.plot(x6, y6)
plt.show()