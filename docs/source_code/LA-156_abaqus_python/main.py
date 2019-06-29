#main.py

import os
import time


dict_variables_for_part_bar = {'back_side':0.05, 'r_bar':0.65, 'l_bar':0.75, 'front_side':0.95}
dict_variables_for_part_rib = {'rib_1s':0.065, 'rib_1f':0.08, 'rib_2s':0.265, 'rib_2f':0.28, 
							   'rib_3s':0.47, 'rib_3f':0.485, 'rib_4s':0.635, 'rib_4f':0.65, 
							   'rib_5s':0.9, 'rib_5f':0.915}

dict_variables_for_material = {'E1':58000.0, 'E2':57200.0, 'mu':0.06, 'G12':10500, 
							   'F1t':904, 'F1c':-904, 'F2t':904, 'F2c':-904, 'F12':94}
dict_variables_for_material_filler = {'E1':105.0, 'E2':105.0, 'mu':0.3, 'G12':42, 
								      'F1t':2.2, 'F1c':-1.7, 'F2t':2.2, 'F2c':-1.7, 'F12':1.4}
dict_variables_for_layout_thickness = {'Ply1':0.001, 'Ply2':0.001, 'Ply3':0.42, 'Ply4':0.42,
								       'Ply5':0.42, 'Ply6':0.42, 'Ply7':0.001, 'Ply8':0.001, 'Filler': 3}
dict_variables_for_layout_orientation = {'Ply1':0, 'Ply2':90.0, 'Ply3':45.0, 'Ply4':-45.0, 
										 'Ply5':-45.0, 'Ply6':45.0, 'Ply7':90.0, 'Ply8':0, 'Filler': 0}

dict_variables_for_load = {'pressure': 0.309, 'u1':0, 'u2':0, 'u3':0, 'r1':0, 'r2':0, 'r3':0}
Mesh = {'size':44}


params = {'dict_variables_for_part_bar':dict_variables_for_part_bar,
			'dict_variables_for_part_rib':dict_variables_for_part_rib,
			'dict_variables_for_material':dict_variables_for_material,
			'dict_variables_for_material_filler': dict_variables_for_material_filler,
			'dict_variables_for_layout_thickness':dict_variables_for_layout_thickness,
			'dict_variables_for_layout_orientation':dict_variables_for_layout_orientation,
			'dict_variables_for_load':dict_variables_for_load,
			'Mesh':Mesh}

def Generate_scripts(params=params, n='1'):
	'''This will create a files from templates for script.py and script_outp.py
	It will take a parameters in condition of dicts and insert them at the start of the files
	'''
	with open('script.py', 'w') as script, open('template.py', 'r') as template:
		for param in params:
			print(param, '=', str(params[param]), end='\n', file=script)
		print('\n', file=script)
		for line in template:
			print(line, end='', file=script)

	with open('script_outp.py', 'w') as script_outp:
		with open('template_output.py', 'r') as template_output:
			print('n = ', str(n), file=script_outp)
			for line in template_output:
				print(line, end='', file=script_outp)
	return 'script_outp.py'


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


def condition (res, expect):
	if res < expect: return True
	else: return False


def find_key_value (dict, val):
	'''will find a FIRST key according to value, if not -> None
	'''
	for i in dict:
		if dict[i] == val: return i
	return None


def status_bar (delay):
	''' This will generate a status-bar for fixture delay
	'''
	step = delay/100
	print()
	print('....status....')
	print()
	for i in range(100):
		print('·' * (i+1), end='')
		print('\r', end='')
		time.sleep(step)
	print()
	print()

#********************************************************
#			main body
#********************************************************

fi = [0, 15, 30, 45, 60, 75, 90]		#degrees range
n = 0				#iteration counter
for i in fi:
	n += 1
	print('set up Ply3/6 as {}, Ply4/5 as -{}'.format(i, i))
	params['dict_variables_for_layout_orientation']['Ply3'] = i
	params['dict_variables_for_layout_orientation']['Ply4'] = -i
	params['dict_variables_for_layout_orientation']['Ply5'] = -i
	params['dict_variables_for_layout_orientation']['Ply6'] = i

	print('Generate a scripts')
	sctipt_name = Generate_scripts(params, n)

	print('Start a calculation in Abaqus')
	command = 'abaqus cae noGUI=' + sctipt_name
	os.popen (command, 'w')		#DELEGATION OPERATION TO ABAQUS
	status_bar (150)		#this is approximately time for abaqus making a calculation
	print('\nCalculation ', n, 'is done\n')
	print('THSAI =', parser_res('abaqus.rpt')[1], '\n\n\n')

results = parser_res('abaqus.rpt')[0]
iter_num_min_val = find_key_value(results, min(results.values()))
fi_min_val = iter_num_min_val
print('\n', iter_num_min_val, ' -- number of iteration with the smallest value of result')
print('this iteration correspond to angle of ', fi[fi_min_val - 1], '\n')


if not condition (results[iter_num_min_val], 1):
	n += 1
	print('\nas THSAI >= 1, need more thickness\n')
	params['dict_variables_for_layout_thickness']['Ply3'] += 0.42
	params['dict_variables_for_layout_thickness']['Ply4'] += 0.42
	params['dict_variables_for_layout_thickness']['Ply5'] += 0.42
	params['dict_variables_for_layout_thickness']['Ply6'] += 0.42

	print('Generate a scripts')
	sctipt_name = Generate_scripts(params, n)

	print('Start a calculation in Abaqus')
	command = 'abaqus cae noGUI=' + sctipt_name
	os.popen (command, 'w')		#DELEGATION OPERATION TO ABAQUS
	status_bar (150)		#this is approximately time for abaqus making a calculation
	print('\nCalculation ', n, 'is done\n')
	print('Result is ', parser_res('abaqus.rpt')[1], '\n\n\n')

	while not condition(parser_res('abaqus.rpt')[1], 1):
		n += 1
		print('\nas THSAI still >= 1, need more thickness\n')
		
		params['dict_variables_for_layout_thickness']['Ply3'] += 0.42
		params['dict_variables_for_layout_thickness']['Ply4'] += 0.42
		params['dict_variables_for_layout_thickness']['Ply5'] += 0.42
		params['dict_variables_for_layout_thickness']['Ply6'] += 0.42


		print('Generate a scripts')
		sctipt_name = Generate_scripts(params, n)

		print('Start a calculation in Abaqus')
		command = 'abaqus cae noGUI=' + sctipt_name
		os.popen (command, 'w')		#DELEGATION OPERATION TO ABAQUS
		status_bar (125)		#this is approximately time for abaqus making a calculation
		print('\nCalculation ', n, 'is done\n')
		print('Result is ', parser_res('abaqus.rpt')[1], '\n\n\n')