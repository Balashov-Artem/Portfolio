+++
draft = false
image = "img/projects/Abaqus_python/1.png"
date = "2016-11-05T18:25:22+05:30"
title = "Automatization of Abaqus FEA using python"
showonlyimage = false
description = "Design of an LA-156 Wing skin"
+++

In this paper I will describe how to automate Abaqus Finite Element Analyses using python script on example of optimization wing skin panel parameters.

<img src="../../img/projects/Abaqus_python/1.png" width="100%" alt="Scheme" />

## Contents
---

-   [Introduction](#introduction)
-   [Initial data](#initial-data)
-   [Work in GUI](#work-in-gui)
    -   [Model import](#model-import)
    -   [Modeling CM](#modeling-cm)
    -   [Loads and BC](#loads-and-bc)
    -   [Result export](#result-export)
-   [Scripts generation and formatting](#scripts-generation-and-formatting)
-   [Main file adjustment](#main-file-adjustment)  
    -   [Making template](#making-template)
    -   [Parsing result file](#parsing-result-file)
    -   [Iteration optimization](#iteration-optimization)
    -   [Main file optimization](#main-file-optimization)
-   [Conclusion](#conclusion)  



---
### Introduction

The main point of this whole work is to replace action sequence in GUI by formatted scripts. By default, Abaqus write each and every setups by sequence in a file. This file generated automatically in default working directory and have format of *.jnl*. This exact file we need to make a script from it, by simply changing it's format to *.py*. After processing all steps in GUI we could just this file as a script and it will reprocess all the steps we made manually. Actually, it will already be 'scripting'. However, a few nuances shall be mention. But I will describe them little bit later. First, I will tell how to run this scrips. 

Abaqus software allows to run a scrips in two ways: from GUI and from command line. From GUI it could be run from menu 'File' -> 'Run script'
<img src="../../img/projects/Abaqus_python/18.png" width="40%" alt="Here shall be picture of abaqus file menu" />

or from command line above:
<img src="../../img/projects/Abaqus_python/19.png" width="40%" alt="Here shall be picture of abaqus command line" />

From command line there is to commands to run a script - in GUI and without GUI:

```
abaqus cae  = sctipt_name
abaqus cae noGUI = sctipt_name
```

The first one will open GUI and then run script there, the second one will run a script without GUI. Which is pretty obvious, whats is not that obvious, is how Abaqus will produce any result from running a script without GUI. And this is first thing about this scripting model. This *.jnl* file contains sequence of all actions in each steps **BEFORE** visualization step. So basically, this sequence just setup job for submit and run it. On this step Abaqus will create results and hold it in format of *.ODB* - Object Database. And to see these results we need to open GUI, import Database and only then results will appears in visualization menu. Or, we need to create one more script for writing results in file format, that could be opened by hands and parsed by python.

One more thing about this *.jnl* file. It contains sequence of EACH action, that was made in GUI. What does it mean? Let's take an example. You setup one of geometrical sizes as 54 mm, then you realized it was a mistake and changed in to 45 mm. In *.jnl* file Abaqus will write not just this size as 45 mm, it will write both actions, and setting this size as 54 mm, and then changing it to 45 mm. 


---
### Initial data

I will describe this method at example of optimization Wing skin panel parameters. This skin panel was taken from [one of my previous projects](https://balashov-artem.github.io/Portfolio/projects/la-156_wing/), so I will import model from there. Here is some initial values, such as geometrical sizes, inner sizes parameters and materials' characteristics.


<table border="1" width="50%">
   <caption>Table 1. Overall dimensions</caption>
   <tr>   <th>Root chord, mm</th>	<th>1925</th>
   <tr>   <td>Edge chord, mm</td>   <th>1025</th>
   <tr>   <td>Console length</td>   <th>270</th>
   </table>



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

<table border="1" width="100%">
	<caption></caption>
	<tr>	<th></th>	<th></th>	<th></th>	<th></th>	</tr>
	<tr>	<th></th>	<th></th>	<th></th>	<th></th>	</tr>
	</table>


<table border="1" width="100%">
	<caption>CM characteristics</caption>
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

### Work in GUI

#### Model import
#### Modeling CM
#### Loads and BC
#### Result export

---
### Scripts generation and formatting

---
### Main file adjustment

#### Making template

#### Parsing result file

#### Iteration optimization

#### Main file optimization

---
### Conclusion


<table border="1" width="100%">
	<caption></caption>
	<tr>	<th></th>	<th></th>	<th></th>	<th></th>	</tr>
	<tr>	<th></th>	<th></th>	<th></th>	<th></th>	</tr>
	</table>