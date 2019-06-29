#Main.py

import os
import time

'''
Mat = {'E1': 147000.0, 'E2': 8000.0, 'mu': 0.23, 'G12': 4500, 'F1t': 1600, 'F1c': -1450, 'F2t': 50, 'F2c': -10, 'F12': 75}
Pl_th = {'Ply1': 0.1, 'Ply2': 0.1, 'Ply3': 0.1, 'Ply4': 0.1, 'Ply5': 0.1, 'Ply6': 0.1, 'Ply7': 0.1, 'Ply8': 0.1}

Mat = {'E1': 58000.0, 'E2': 57200.0, 'mu': 0.06, 'G12': 10500.0, 
		'F1t': 904, 'F1c': -904, 'F2t': 128, 'F2c': -128, 'F12': 89}

Pl_th = {'Ply1': 0.42, 'Ply2': 0.42, 'Ply3': 0.42, 'Ply4': 0.42, 
		'Ply5': 0.42, 'Ply6': 0.42, 'Ply7': 0.42, 'Ply8': 0.42}

'''


Dim = {'x0': -250, "y0": -250, 'x1': 250, 'y1': 250}
Mat = {'E1':41000.0, 'E2':10400.0, 'mu':0.28, 'G12':40300, 'F1t':1140, 'F1c':-620, 'F2t':39, 'F2c':-128, 'F12':89}
Pl_or = {'Ply1': 0, 'Ply2': 90, 'Ply3': -45, 'Ply4': 45, 
		'Ply5': 45, 'Ply6': -45, 'Ply7': 90, 'Ply8': 0}
Pl_th = {'Ply1': 0.08, 'Ply2': 0.08, 'Ply3': 0.08, 'Ply4': 0.08, 'Ply5': 0.08, 'Ply6': 0.08, 'Ply7': 0.08, 'Ply8': 0.08}
Pressure = {'Magnitude': 1}		#MPa
BC = {'u1': 0, 'u2': 0, 'u3': 0, 'r1': 0, 'r2': 0, 'r3': 0}
Mesh = {'Size': 50}		#mm

n = 0



params = {
	'Dim': Dim,
	'Mat': Mat,
	'Pl_or': Pl_or,
	'Pl_th': Pl_th,
	'Pressure': Pressure,
	'BC': BC,
	'Mesh': Mesh}


def Generate_scripts (params = params, n = '1'):
	'''This will create a files from templates for Script.py and Output_script.py
	It will take a parameters in condition of dicts and 
	insert them at the start of the files'''

	with open('Script.py', 'w') as script, open('Template.py', 'r') as template:
		for param in params:
			print(param, '=', str(params[param]), end='\n', file=script)
		print('\n', file=script)
		for line in template:
			print(line, end='', file=script)

	with open('Output_script.py', 'w') as Output_script:
		with open('Output_template.py', 'r') as template_output:
			print('n = ', str(n), file=Output_script)
			for line in template_output:
				print(line, end='', file=Output_script)
	return 'Output_script.py'

def parser_res (res_file='abaqus.rpt'):

	'''
	Function, that takes a name of result file (abaqus.rpt for default)
	and will give a tuple, which is:
	1) a dict with all maximum value per ply ----- for ALL iterations
	2) maximum value per ply 				 ----- for LAST iteration
	output = ({1: max, 2: max, ... }, max)
	'''
	results = {}
	counter = 1			# it will count amount of proc iteration
	with open(res_file, 'r') as res:	
		for line in res:
			lstrip = line.lstrip()			#delete spaces ' '
			if lstrip[0:7] == 'Maximum':		#find line with 'Maximum'
				tot = lstrip[7:].split(' ')		#delete 'Maximum' and convert it to list 'tot'

				for i in range(len(tot)):		
					if '' in tot: tot.remove('')	#delete an empty ('') elements in list
					if '\n' in tot: tot.remove('\n') #delete an ('/n') element if exist

				tot = [float(i) for i in tot]		#convert elements in 'tot' from string to list
				results[counter] = max(tot)
				counter += 1

	return results, results[max(results.keys())]

'''
def condition (res, expect):
	if res < expect : return True
	else: return False
'''


def find_key_value (dict, val):
	'''will find a FIRST key according to value, if not -> None
	'''
	for i in dict:
		if dict[i] == val: return i
	return None



def find_or_delay (path, name):
	#list_dir = os.listdir(path)
	#print('waiting for ', name)
	#print('in ', list_dir)

	for i in range(500):
		list_dir = os.listdir(path)
	
		if name in list_dir:
			print ('done in ', i*3, 'sec')
			print ()
			break
		else:
			print('·' * (i+1), end='')
			print('\r', end='')

			print(i, end='')
			print('\r\r\r', end='')
			time.sleep(3)
	#print('time is over, calculation is not done')

def clear_dir ():
	list_dir = os.listdir()
	r_files = ['Main.py', 'Output_template.py', 'Template.py']
	for file in list_dir:
		if file not in r_files:
			os.remove(file)
			print('clear ...', file)


#********************************************************
#			main body
#********************************************************

def find_opymal_orient (params, angle_range):
	global n

	for fi in angle_range:
		n += 1

		print('Set up Ply3 and Ply6 as {}°, and Plyes 4 and 5 as {}°'.format(fi, -fi))
		params['Pl_or']['Ply3'] = fi
		params['Pl_or']['Ply4'] = -fi
		params['Pl_or']['Ply5'] = -fi
		params['Pl_or']['Ply6'] = fi

		print('Generate scripts')
		sctipt_name = Generate_scripts(params, n)

		print('Start a calculation in Abaqus')
		command = 'abaqus cae noGUI=' + sctipt_name
		os.popen (command, 'w')		#DELEGATION OPERATION TO ABAQUS
		find_or_delay (None, 'Print' + str(n) + '.png')

		print('\nCalculation ', n, 'is done\n')
		print('THSAI =', '\n', parser_res('abaqus.rpt')[1], '\n')


	results = parser_res('abaqus.rpt')[0]
	min_THSAI = min(results.values())
	iter_num_min_val = find_key_value(results, min_THSAI)
	fi_min_val = iter_num_min_val -1
	fi_opt = angle_range[fi_min_val]
	print('\n', iter_num_min_val, ' -- number of iteration with the smallest value of result')
	print('this iteration correspond to angle of ', fi_opt, '\n')
	return fi_opt, results, min_THSAI


def add_layers (params, fi_opt, min_THSAI):
	global n
	monolay = params['Pl_th']['Ply3']


	while min_THSAI > 1 :
		
		n += 1
		print('\nas THSAI >= 1, need more thickness\n')


		params['Pl_or']['Ply3'] = fi_opt
		params['Pl_or']['Ply4'] = fi_opt
		params['Pl_or']['Ply5'] = fi_opt
		params['Pl_or']['Ply6'] = fi_opt

		params['Pl_th']['Ply3'] += monolay
		params['Pl_th']['Ply4'] += monolay
		params['Pl_th']['Ply5'] += monolay
		params['Pl_th']['Ply6'] += monolay

		print('Generate a scripts')
		sctipt_name = Generate_scripts(params, n)
		print('Start a calculation in Abaqus')
		command = 'abaqus cae noGUI=' + sctipt_name
		os.popen (command, 'w')		#DELEGATION OPERATION TO ABAQUS
		find_or_delay (None, 'Print' + str(n) + '.png')
		print('\nCalculation ', n, 'is done')
		print('layers thickness is ', params['Pl_th']['Ply3'])
		min_THSAI = parser_res('abaqus.rpt')[1]
		print('Result is ', min_THSAI, '\n')

		'''
		while min_THSAI > 1:
			n += 1
			print('\nas THSAI still >= 1, need more thickness\n')
			
			params['Pl_th']['Ply3'] += monolay
			params['Pl_th']['Ply4'] += monolay
			params['Pl_th']['Ply5'] += monolay
			params['Pl_th']['Ply6'] += monolay


			print('Generate a scripts')
			sctipt_name = Generate_scripts(params, n)

			print('Start a calculation in Abaqus')
			command = 'abaqus cae noGUI=' + sctipt_name
			os.popen (command, 'w')		#DELEGATION OPERATION TO ABAQUS
			find_or_delay (None, 'Print' + str(n) + '.png')
			print('\nCalculation ', n, 'is done\n')
			print('layers thickness is ', params['dict_variables_for_layout_thickness']['Ply3'])
			'''
	

	results = parser_res('abaqus.rpt')[0]
	return params['Pl_th']['Ply3'], results



clear_dir ()
opt_angle, results, min_THSAI = find_opymal_orient(params, [0, 15, 30, 45, 60, 75, 90])
print('optimal layer orientation is ', opt_angle, '°')

opt_lay_thic, results = add_layers(params, opt_angle, min_THSAI)
print('optimal layer orientation is ', opt_angle, '°')
print('layers thickness is ', opt_lay_thic)
print('Result is ', results)