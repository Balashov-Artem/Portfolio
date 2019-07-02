#main.py

import os
import time
from math import *



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




n = 1
n_name = ''
radius = 100
'''
mat1 = {'name': 'carbon_1', 'dens': 2400, 'E1': 96000, 
        'E2': 96000, 'mu12': 0.26, 'G12': 7000, 'd': 0.12}

mat2 = {'name': 'carbon_2', 'dens': 2800, 'E1': 196000, 
        'E2': 69000, 'mu12': 0.28, 'G12': 7000, 'd': 0.12}
'''

str_ang = [0, 45, -45, 90]
str_mat = [AGP370_5H, AGP370_5H, AGP370_5H, AGP370_5H]

dist_P = [300, 268, 194, 105, 32.02, 0]
dist = [0, 0.055, 0.11, 0.165, 0.22, 0.275]
stp_dist = [1, 0.8, 0.9, 0.75, 0.8, 0.9, 1]


params = {
	'radius': radius, 
	'mat1': AGP370_5H,
	'mat2': AGP370_5H,
	'str_ang': str_ang, 
	'str_mat': str_mat,
	'dist_P': dist_P, 
	'dist': dist, 
	'stp_dist': stp_dist}


cur_dir = os.getcwd() + os.sep
script_name = 'output.py'

command = 'abaqus cae noGUI=' + script_name

works = ['materials', 'orientation', 'pressure']
exceptions = ['plate.py', 'output.py', 'template_output.py', 'template_plate.py', 'main.py', 'reserv', 'abaqus.rpt']







def Generate_scripts(params, n_name, n=1):
	
	with open('plate.py', 'w') as script, open ('template_plate.py', 'r') as template:
		for param in params:
			print (param, '=' , str(params[param]), end='\n', file = script)
		print('\n'*5, file=script)
		for line in template:
			print(line, end='', file=script)

	with open('output.py', 'w') as output, open ('template_output.py', 'r') as template_out:
		print('n = ', str(n), file=output)
		print('n_name = ', '"', end = '', file=output)
		print(n_name, end = '', file=output)
		print('"', file=output)
		print('\n'*5, file=output)
		
		for line in template_out:
			print(line, end='', file=output)

	return 'output.py'


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

	return results_l[-1]


def find_or_delay (path, name):
	list_dir = os.listdir(path)
	#print('waiting for ', name)
	#print('in ', list_dir)
	for i in range(50):
		list_dir = os.listdir(path)
		if name in list_dir:
			#time.sleep(1)
			print ('done in ', i)
			print ()
			break
		else:
			print('·' * (i+1), end='')
			print('\r', end='')
			print(i, end='')
			print('\r\r\r', end='')
			time.sleep(1)

def clear_dir ():
	global exceptions
	#pic_exceprions1 = ['picture_' + str(i) + '.png' for i in range(10000)]
	#pic_exceprions2 = ['awesome_picture_' + str(i)  + '.png' for i in range(10000)]
	#exceptions = ['plate.py', 'output.py', 'template_output.py', 'template_plate.py', 'main.py', 'reserv', 'abaqus.rpt'] + pic_exceprions1 + pic_exceprions2
	for file in os.listdir():
		if file in exceptions:
			pass
		else:
			#print ('deleting...    ', file)
			os.remove(file)


def Pressure_distribution(P0, h, rn):
	points = [0, 0.2, 0.4, 0.6, 0.8, 1]
	pressure_distr = [0 for i in points]
	points_distr = [0 for i in points]

	al = 0.5*2*pi/360
	ra = rn + h*sin(al)
	#print('ra =   ', ra)

	for i in range(len(points)):
		point = points[i] * ra
		#print(point)
		P = P0 * ( 2*(point/ra)**3 - 3*(point/ra)**2 + 1 )
		pressure_distr[i] = P
		points_distr[i] = ra*points[i]

	return pressure_distr, points_distr


'''
for i in range(len(materials_list)-12):
	print(exceptions)
	params['mat1'] = materials_list[i]
	params['mat2'] = materials_list[i]
	params['str_mat'] = [materials_list[i], materials_list[i], materials_list[i], materials_list[i]]
	indicator_name1 = 'picture_' + str(n_name) + '_' + str(i) + '.png'
	indicator_name2 = 'picture_zoom_' + str(n_name) + '_' + str(i) + '.png'

	exceptions.append(indicator_name1)
	exceptions.append(indicator_name2)

	clear_dir()
	Generate_scripts(params, n_name, i)

	os.popen (command, 'w')
	print(indicator_name1)
	find_or_delay (cur_dir, indicator_name1)
	time.sleep(5)
	print(parser_res ())
'''

#	Work 1

counter = 0

material_res = []
for i in range(len(materials_list)):
	params['mat1'] = materials_list[i]
	params['mat2'] = materials_list[i]
	params['str_mat'] = [materials_list[i], materials_list[i], materials_list[i], materials_list[i]]
	mat_pres_res = []

	for p in range(20):

		counter += 1

		P0 = 200 + p*10
		params['dist_P'] = Pressure_distribution(P0, 20, 0.3)[0]
		params['dist'] = Pressure_distribution(P0, 20, 0.3)[1]
		
		n_name = materials_list[i]['name']
		print('Starting  ', n_name, '  .....')
		n = P0
		indicator_name1 = 'picture_' + str(n_name) + '_' + str(n) + '.png'
		indicator_name2 = 'picture_zoom_' + str(n_name) + '_' + str(n) + '.png'


		exceptions.append(indicator_name1)
		exceptions.append(indicator_name2)

		clear_dir()
		Generate_scripts(params, n_name, n)

		os.popen(command, 'w')
		find_or_delay(cur_dir, indicator_name1)
		time.sleep(5)

		print('simulation #', counter, 'has done')

		mat_pres_res.append(parser_res())
	material_res.append(mat_pres_res)



#	Work 2
orientation_res = []
for i in range(0, 91, 5):
	params['mat1'] = materials_list[2]
	params['mat2'] = materials_list[2]
	params['str_mat'] = [materials_list[2], materials_list[2], materials_list[2], materials_list[2]]
	params['str_ang'] = [i, -i, -i, i]
	mat_pres_res = []

	for p in range(10):

		counter += 1

		P0 = 200 + p*20
		params['dist_P'] = Pressure_distribution(P0, 20, 0.3)[0]
		params['dist'] = Pressure_distribution(P0, 20, 0.3)[1]
		
		n_name = str(materials_list[2]['name']) + '_' + str(i) + 'deg_orientation'
		print('Starting  ', n_name, '  .....')
		n = P0
		indicator_name1 = 'picture_' + str(n_name) + '_' + str(n) + '.png'
		indicator_name2 = 'picture_zoom_' + str(n_name) + '_' + str(n) + '.png'


		exceptions.append(indicator_name1)
		exceptions.append(indicator_name2)

		clear_dir()
		Generate_scripts(params, n_name, n)

		os.popen(command, 'w')
		find_or_delay(cur_dir, indicator_name1)
		time.sleep(5)
		
		print('simulation #', counter, 'has done')

		mat_pres_res.append(parser_res())
	orientation_res.append(mat_pres_res)




#	Work 3

pressure_res = []
for nz in [0.05, 0.1, 0.25, 0.5, 1]:

	nz_res = []	
	params['mat1'] = materials_list[5]
	params['mat2'] = materials_list[5]
	params['str_mat'] = [materials_list[5], materials_list[5], materials_list[5], materials_list[5]]
	params['str_ang'] = [0, 45, -45, 90]

	for p in range(10):

		p_res = []
		for d in range(10):

			counter += 1

			P0 = 200 + p*20
			dist = 10 + d*10
			params['dist_P'] = Pressure_distribution(P0, dist, nz)[0]
			params['dist']   = Pressure_distribution(P0, dist, nz)[1]

			n_name = str(materials_list[5]['name']) + '_' + str(int(nz*100)) + '_' + str(P0) + 'MPa_'
			print('Starting  ', n_name, '  .....')
			n = dist
			indicator_name1 = 'picture_' + str(n_name) + '_' + str(n) + '.png'
			indicator_name2 = 'picture_zoom_' + str(n_name) + '_' + str(n) + '.png'

			exceptions.append(indicator_name1)
			exceptions.append(indicator_name2)


			clear_dir()
			Generate_scripts(params, n_name, n)

			os.popen(command, 'w')
			find_or_delay(cur_dir, indicator_name1)
			time.sleep(5)

			print('simulation #', counter, 'has done')

			p_res.append(parser_res())
		nz_res.append(p_res)
	pressure_res.append(nz_res)