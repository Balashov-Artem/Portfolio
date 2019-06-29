+++
draft = false
image = "img/portfolio/LA-156_Abaqus_python_opt/1.png"
date = "2019-06-05T18:25:22+05:30"
title = "Wing panel optimization using python script for Abaqus FEA"
showonlyimage = false
description = " Optimization of LA-156 Wing skin upper panel using script on python to automatize Abaqus FEA"
+++


In this paper I will give a short overview to the project I made of optimization of LA-156 Wing skin upper panel [from this work](https://balashov-artem.github.io/Portfolio/projects/la-156_wing/) using Abaqus FEA and [python scripting](https://balashov-artem.github.io/Portfolio/projects/automatization-of-abaqus-fea-using-python/).


<img src="../../img/portfolio/LA-156_Abaqus_python_opt/1.png " width="75%" alt="Here shall be picture of wing" /> 

## Contents
---

-   [Initial data](#initial-data)
-   [Task observation](#task-observation)
-   [Iteration optimization](#iteration-optimization)
-   [Conclusion](#conclusion)  



---
### Initial data

In this paper, was observed analysis of a composite three-layer panel of the La-156 wing skin lower panel loaded with uniformly distributed pressure. It is necessary to carry out the design calculation by the finite element method (hereinafter FEM) with iterative change of some initial data. Initial data were taken from the work [LA-156 Wing skin]( https://balashov-artem.github.io/Portfolio/projects/la-156_wing/).

<img src="../../img/portfolio/LA-156_Abaqus_python_opt/2.png " width="75%" alt="Here shall be picture of wing scheme" />

 
*Aircraft wing design Scheme*


Wing airfoil – NACA 2216.

<table border="1" width="50%">
   <caption>Table 1. Overall dimensions</caption>
   <tr>   <th>Root chord, mm</th>	<th>1925</th>
   <tr>   <td>Edge chord, mm</td>   <th>1025</th>
   <tr>   <td>Console length</td>   <th>270</th>
   </table>


The model for the analysis was imported from the CATIA V5 system, so before starting the analysis it is necessary to specify the lines of the beginning and ends of the spar, walls and ribs. Luckily, these softwares were developed with one company, so I don't need to convert my model to another format. The percentages are shown in table 2:

<table border="1" width="70%">
	<caption>Table 2. Parts' dimensions</caption>
	<tr>	<th>Lead edge, %*</th>		<th>5</th>		<th>Back edge, %5</th>		<th>95</th>		</tr>
	<tr>	<th>1 rib opening, %**</th>	<th>6,5</th>	<th>1 rib ending, %**</th>	<th>8</th>		</tr>
	<tr>	<th>2 rib opening, %**</th>	<th>26,5</th>	<th>2 rib ending, %**</th>	<th>28</th>		</tr>
	<tr>	<th>3 rib opening, %**</th>	<th>47</th>		<th>3 rib ending, %**</th>	<th>48,5</th>	</tr>
	<tr>	<th>4 rib opening, %**</th>	<th>63,5</th>	<th>4 rib ending, %**</th>	<th>65</th>		</tr>
	<tr>	<th>5 rib opening, %**</th>	<th>90</th>		<th>5 rib ending, %**</th>	<th>91,5</th>	</tr>
	</table>

where, %* - along chord, %** - along console.
The pressure varies from 0.92 MPa on the wing tip to 0.07 MPa on the rear panels. In this paper, the maximum was taken into account.

<table border="1" width="80%">
	<caption>Table 3. CM characteristics</caption>
	<tr>	<th>Tension elastic modulus</th>					<th>Et, GPa</th>	<th>58</th>		</tr>
	<tr>	<th>Compression elastic modulus</th>				<th>Ec, GPa</th>	<th>57,8</th>	</tr>
	<tr>	<th>Transversal elastic modulus</th>				<th>G, GPa</th>		<th>10,49</th>	</tr>
	<tr>	<th>Tension critical stress along fiber</th>		<th>Ft1, MPa</th>	<th>904</th>	</tr>
	<tr>	<th>Compression critical stress along fiber</th>	<th>Fc1, MPa</th>	<th>128</th>	</tr>
	<tr>	<th>Tension critical stress across fiber</th>		<th>Ft2, MPa</th>	<th>904</th>	</tr>
	<tr>	<th>Compression critical stress across fiber</th>	<th>Fc2, MPa</th>	<th>128</th>	</tr>
	<tr>	<th>Transversal critical stress</th>				<th>F12, MPa</th>	<th>176</th>	</tr>
	<tr>	<th>Poisson coefficient </th>						<th>nu_xy</th>		<th>0,06</th>	</tr>
	<tr>	<th>Mono-layer thickness</th>						<th>d0, mm</th>		<th>0,42</th>	</tr>
	<tr>	<th>Density</th>									<th>po, kg/mm3</th>	<th>1335</th>	</tr>
	</table>

---

### Task observation

In the modeling three-layered composite (hereinafter CM) panel has been taken some assumptions. Since the panel is connected to the spar, 2 walls and 5 ribs, in these places there can not be filler, since it is not able to transfer the load between the skin and the power sets, in these areas filler is truncated. The structure of the panel becomes segmented – 12 segments of foam filler are placed within the panel.
Modeling such a structure for FEM analysis is a very time-consuming and not entirely justified task, since it takes a lot of time both for modeling and calculation, and the results can be incorrectly interpreted due to incorrect display of the operating stresses in the areas of stress concentrators – at the boundaries of segments. 

In this regard, the modeling of a three-layer panel in this work takes place by introducing a filler as one of the layers of the composite. Abaqus allows to create layered profiles with the “Create composite layer”command.

The load is modeled as a uniform pressure , the boundary conditions (hereinafter, BC) – by fixing all the movements and rotations of the connection sections of the wing skin panel with the power elements Such GU correspond to reality, because the type of connection – adhesive, provides load transfer without displacements and turns.

The type of finite elements is set to quadrangular – since the panel has no stress concentrators, and it itself presented as curved in the plane quadrangular surface. The type of finite element approximation is the quadratic approximation of displacements within a single element.
The size of the finite elements (FE) is given by the variable between iterations. For design iterations, the size of the FE set to be not more than 5% of the minimum (1025) overall panel size – 44mm – value set by ABAQUS as default for the initial iterations fits quite fine.


#### Loads and BC

This panel has usual for most composite wing panel connection type - glue connection with ribs and longeron, so BC for this panel is next: 

<img src="../../img/portfolio/LA-156_Abaqus_python_opt/3.png " width="75%" alt="Here shall be picture of set for BC " />

---

### Iteration optimization
When the scripts generation from variables and templates is configured, the results search in results file is configured, in fact it is enough to write a cycle of successive calls of these functions in the executable file in order to automate the process. But in this project it is necessary to optimize the result by changing initial parameters.

There are many ways of optimization, their number depends only on engineer imagination. For example, we can set the stability calculation, and change the filler thickness based on the results from stress loss of stability. We can record the results of successive thickness increasing and reinforcement layers (RL) increasing, output the results as a graph with the axes of the resulting strength and mass, and select a point with a minimum mass.
But in this project we will change only the number of layers and their orientation. The thickness of the filler is selected as 12 mm. Assume that this parameter is immutable.

The orientation angle optimization looks as follows:

1. Set the number of layers in each group to 1
2. Setting the angle search range from 0° to 90° with 15°increments.
3. Result file analyses and determination the angle with maximum margin of safety (at which iteration).
4. A sequential set of layers in a given group.


As can be seen from the requirement abowe, it is necessary to implement 2 different iterative systems, one without the condition – the search of the angle regardless from results, and one conditional, the search of thicknesses depending on results. This was implemented 2 functions, conditionals (next code fragment) and unconditional.

```python
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
```


Optimization Function of the orientation angle

The function of thickness increasing won’t be given here, because it is not too different from this. However, the full code and the executable file, will be provided in the [Application](https://github.com/Balashov-Artem/Portfolio/blob/master/static/source_code/LA-156_abaqus_python) 
What this feature does in detail:

* Shortens the name “angle range” to “fi”;
* Initiate cycle through the list of angles, where i – number of iteration, and the angle;
* Increases the iteration counter by 1
* Sets 3 and 6 angles to fi and 4 and 5 to -fi, writes these values to the dictionary and reports about it to the terminal;
* Starts the script generation function and reports about it;
* Generates a command to run the script from the script name;
* Delegates this command to the abaqus interpreter and reports it;
* Starts the delay function until abaqus finished calculation;
* Reports about completion of the n-th iteration of Abaqus and displays the result. After that, the cycle ends, but the function still works;
* Calls the search function for results from a file and writes them into the dictionary;
* Specifies the iteration number with the maximum safety margin;
* Defines the angle at this iteration;
* Reports the iteration number and the optimal angle to the terminal;
* Outputs the tuple from the optimal angle, the dictionary of all results, and the last iteration number as a result

---

### Conclusion
This panel with a thickness of 12 mm filler withstands specified loads and pressure with the number of layers equal to 2 pieces, and since it was a textile, its optimal stacking angle is 0°. It is obvious that this program will not optimize the panel, it will check all the angles, make sure that at 0° and 90° the results are equal and minimal, and the second function will not even starts at all, because the margin of safety is greater than 1.

In this regard, as an example, was analyzed model with a glass fiber material (E-glass 55%) with a filler thickness of 12mm. Characteristics of which are given in table 4.

<table border="1" width="80%">
	<caption>Table 4. E-glass 55% characteristics</caption>
	<tr>	<th>Tension elastic modulus</th>					<th>Et, GPa</th>	<th>41</th>		</tr>
	<tr>	<th>Compression elastic modulus</th>				<th>Ec, GPa</th>	<th>10.4</th>	</tr>
	<tr>	<th>Transversal elastic modulus</th>				<th>G, GPa</th>		<th>4.3</th>	</tr>
	<tr>	<th>Tension critical stress along fiber</th>		<th>Ft1, MPa</th>	<th>1140</th>	</tr>
	<tr>	<th>Compression critical stress along fiber</th>	<th>Fc1, MPa</th>	<th>620</th>	</tr>
	<tr>	<th>Tension critical stress across fiber</th>		<th>Ft2, MPa</th>	<th>39</th>		</tr>
	<tr>	<th>Compression critical stress across fiber</th>	<th>Fc2, MPa</th>	<th>128</th>	</tr>
	<tr>	<th>Transversal critical stress</th>				<th>F12, MPa</th>	<th>89</th> 	</tr>
	<tr>	<th>Poisson coefficient </th>						<th>nu_xy</th>		<th>0,06</th>	</tr>
	<tr>	<th>Mono-layer thickness</th>						<th>d0, mm</th>		<th>0,42</th>	</tr>
	<tr>	<th>Density</th>									<th>po, kg/mm3</th>	<th>1970</th>	</tr>
	</table>

---

The file with the results will be shown in [Appendix]( https://github.com/Balashov-Artem/Portfolio/blob/master/static/source_code/LA-156_abaqus_python/abaqus.rpt), and here is the image of the last iteration with optimal stacking angle and the thickness of the bearing layers.


<img src="../../img/portfolio/LA-156_Abaqus_python_opt/4.png " width="75%" alt="Here shall be picture of wing again" />