+++
draft = false
image = "img/projects/residual_stress/11.gif"
title = "Research of residual stress in CM after AWJ machining using Abaqus FEA"
showonlyimage = false
description = "A short overview on study of machining composite materials using Abrasive WaterJet. Dependence initial parameters of AWJ on residual stress appearing in CM"
+++



### Contents

-	[Introduction](#introduction)
-	[Simulations](#simulations)
	-	[Quasi-dynamic model](#quasi-dynamic-model)
	-	[Simulation model](#simulation-model)
	-	[Scripting](#scripting)
	-	[ABAQUS FEA results](#abaqus-fea-results)
	-	[Summary](#summary)
-	[Experiments](#experiments)
	-	[Measurement methodology](#measurement-methodology)
	-	[Experiments result](#experiments-result)
-	[Conclusion](#conclusion)

---

### Introduction

In this research will be provided one method to numerical calculation dependences from initial parameters of AWJ equipment and CM characteristics on final quality of cut and residual stress. This method presents numerical modeling using Abaqus software to simulate AWJ behavior in composite structure and examine distribution of residual stress. Also, to update traditional way of using Finite Element Analysis as checking calculation to observation calculation I will use scripting language python to write a script to automate simulation. Hence, using this script were made almost thousand of simulations, and the results of them will be bring in next chapter.

---

###	Simulations
####	Quasi-dynamic model
Since during the waterjet peening process, the velocity of the droplets impact on the work piece can be extremely high, the static model can have wrong estimated of pressure from the reality. The article written by Brunton and Rochester shows the dynamic liquid impact can cause the material damage linked to impact pressure. Therefore, it is worth to be mentioned that the impact pressure should be considered into the modeling part.


#####	Dynamic Assumptions
For the transient dynamic modeling, several key factors are assumed to simplify the model:
1. The work piece is considered to be a half-pace body. That means the dimensions of the work piece, including length and width, are infinite at one side of work surface. In practice we set the work piece much larger than the waterjet peening area.
2. Other effects on the work surface like vibration, erosion, etc are ignored.
3. The waterjet is perpendicular to the work surface.
4. Temperature change of work piece is ignored.
5. Water-droplets are uniformly distributed over the striking region. The distance between each droplet should be equal to the contact water-drop radius.
6. Friction between droplets and air should be ignored.

---

####	Simulation model

#####	Part
According to the pre-supposition the model size must be much larger than the waterjet peening area. Since this is an axisymmetric model, to simulate the work piece we will use a cylinder part. The size of the cylinder was set as:
Radius: R=50mm
In 3-D model, the part model is set to be deformable axisymmetric based on shell. Although mesh and analysis are based on 3-D shell but the original object is still solid, so that the section should also choose solid while doing the simulation.

#####	Materials
For this simulation was considered 14 the most common composite materials. Their characteristic are set below in a table belov:

<table border="2" width="100%">
   <caption>Table 1. Composite material characteristics</caption>
   <tr>   <th>Name</th>		<th>Density, kg/m3</th>	<th>E1, GPa</th>	<th>E2, GPa</th>	<th>G12, Gpa</th>	<th>nu12</th>	<th>d, mm</th>		</tr>
   <tr>   <th>AS463</th>		<th>1580</th>		<th>147</th>		<th>10.3</th>		<th>7</th>			<th>0.27</th>	<th>0.12</th>		</tr>
   <tr>   <th>IM6</th>			<th>1600</th>		<th>177</th>		<th>10.8</th>		<th>7.6</th>		<th>0.27</th>	<th>0.15</th>		</tr>
   <tr>   <th>Mod</th>			<th>1540</th>		<th>216</th>		<th>5.0</th>		<th>4.5</th>		<th>0.25</th>	<th>0.16</th>		</tr>
   <tr>   <th>GY70</th>			<th>1590</th>		<th>294</th>		<th>6.4</th>		<th>4.9</th>		<th>0.23</th>	<th>0.1</th>		</tr>
   <tr>   <th>AS458</th>		<th>1570</th>		<th>131</th>		<th>8.7</th>		<th>5.0</th>		<th>0.28</th>	<th>0.15</th>		</tr>
   <tr>   <th>AGP3705H</th>		<th>1600</th>		<th>77</th>			<th>75.0</th>		<th>6.5</th>		<th>0.06</th>	<th>0.42</th>		</tr>
   <tr>   <th>CF0604</th>		<th>1560</th>		<th>62</th>			<th>60.0</th>		<th>3.9</th>		<th>0.04</th>	<th>0.3</th>		</tr>
   <tr>   <th>E_glass 55%</th>	<th>1970</th>		<th>41</th>			<th>10.4</th>		<th>4.3</th>		<th>0.28</th>	<th>0.08</th>		</tr>
   <tr>   <th>E_glass 45%</th>	<th>2100</th>		<th>39</th>			<th>8.6</th>		<th>3.8</th>		<th>0.28</th>	<th>0.15</th>		</tr>
   <tr>   <th>S_glass 55%</th>	<th>2000</th>		<th>43</th>			<th>8.9</th>		<th>4.5</th>		<th>0.27</th>	<th>0.15</th>		</tr>
   <tr>   <th>Style</th>		<th>2200</th>		<th>29.7</th>		<th>29.7</th>		<th>5.3</th>		<th>0.17</th>	<th>0.25</th>		</tr>
   <tr>   <th>M10E</th>			<th>1900</th>		<th>24.5</th>		<th>23.8</th>		<th>4.7</th>		<th>0.11</th>	<th>0.22</th>		</tr>
   <tr>   <th>Kevlar49</th>		<th>1380</th>		<th>80</th>			<th>5.5</th>		<th>2.2</th>		<th>0.34</th>	<th>0.15</th>		</tr>
   <tr>   <th>K120</th>			<th>1380</th>		<th>29</th>			<th>23.0</th>		<th>1.8</th>		<th>0.05</th>	<th>0.22</th>		</tr>
   <tr></tr>
   </table>


#####	Mesh

For appropriate speed/quality simulation balance, mesh should have nonlinear distribution and reduce element size close to center.
<img src="../../img/projects/residual_stress/1.png" width="60%" alt="Mesh with reducing element size" />
*Figure 1.1 - Mesh with reducing element size*


There was made by apply element size on boundary as 1/100 mm of length of the boundary ring. If radius is set up as 50mm, so than ring len is 2·π·R = 2·50·π = 314.15mm. So the length of each element on the boundary ring will be 3.14mm. To reducing element size closer to center I apply element size on guidelines:
<img src="../../img/projects/residual_stress/2.png" width="60%" alt="Seed distribution" />
*Figure 1.2 - Seed distribution (a – boundary ring; b – guidelines)*


By changing them from R/10 mm for bigger size to impact region as smaller size.

#####	Boundary conditions and loading

For boundary condition (BC) and loading was made a cylindrical coordinate system. Boundary ring are fixed by all 3 displacements, but absolve in rotating.

The interface pressure distribution for the round nozzle is parabolic, and the pressure on work piece can be assumed as:
<img src="../../img/projects/residual_stress/f1.png" width="25%" alt="" />

Where, A, B, C, D are constant coefficients.
Several constrains should be satisfied within the pressure distribution, they are: on the axis of the jet, the pressure should be the maximum; at the edge of the contact area, the pressure should be zero. The boundaries are:

<img src="../../img/projects/residual_stress/f2.png" width="35%" alt="" />

Where Psta is the pressure at the stagnation point.
Combined with equations above, it is obtained that:
<img src="../../img/projects/residual_stress/f3.png" width="27.5%" alt="" />

The transient stagnation pressure produced by each droplet depends on the velocity is:
<img src="../../img/projects/residual_stress/f4.png" width="25%" alt="" />

In this transient dynamic model, loading and unloading process are also needed in ABAQUS to simulate the impact process of water droplets. This can be made in the way of build up ABAQUS analysis steps.
In ABAQUS, dynamic analysis includes two kinds of methods: modal superposition procedure and direct-solution dynamic analysis procedure. Usually, modal superposition procedure is used to solve linear dynamic problem, but direct-solution dynamic analysis procedure is used to solve non-linear dynamic problem. So ‘dynamic, explicit’ should be chosen while loading. The jet moving towards the work surface is defined to be the loading process. The droplets impact on each position in each step to build up the pressure. The step time length for each impact during loading and unloading been calculated based on J.E Field’s research as following:
<img src="../../img/projects/residual_stress/f5.png" width="25%" alt="" />

To get the residual stress generated by the pressure a loading and unloading process is required in ABAQUS to simulate the loading and unloading of waterjet. This can be realized by ABAQUS analysis steps. In each load step the procedure type is set to ‘Static, General’ according to the static model analyzing. Several intermediate steps are added during the loading process and unloading process to make a stress-strain curve in different curves.
<img src="../../img/projects/residual_stress/3.png" width="75%" alt="Distribution load per each steps of calculation" />
*Figure 1.3 - Distribution load per each steps of calculation* 

Seven loads are set in this process due to the size of droplets; one load is applied on its position in each step. The loading time and unloading time are calculated according to velocity. Since the loading process will have the strain variation caused by vibration within the model, there should be a short “ageing treatment” time after the final unloading without any load added. Here 1e-6 is set to be the lasting time of this step, which is about 100 times of the shock time..
Pressure distribution applying in ABAQUS using mapped field on cylindrical coordinate system:
<img src="../../img/projects/residual_stress/4.png" width="80%" alt="Mapped field" />
*Figure 1.4 - Mapped field* 

And the summary pressure looks like:
<img src="../../img/projects/residual_stress/5.png" width="50%" alt="Pressure distribution" />
<img src="../../img/projects/residual_stress/5_1.png" width="50%" alt="Pressure distribution" />
*Figure 1.5 - Pressure distribution* 


####	Scripting
To have a chance to make lots of simulation I have wrote a script on python (which is actually a language ABAQUS was written) to automatize simulations. Script contains of 3 parts:

* Main script
* Job assignment template
* Output assignment template

Job template is actually all of actions taking place to set up a job calculation in abaqus, writing in not evident form. It means that I set up variable instead of direct values each time I want to set up changeable variable (radius, pressure distribution, etc). Output template is actually all of actions taking place in “visualization” section of ABAQUS. To be correct they are setting up the viewport, loading object database and generation text file with results and picture. 
Main script contains a formulas and loop assignments for the templates. It adds variable values to the temple, check the result file and changing variable values. And make it again and again according to the loop inside.
<img src="../../img/projects/residual_stress/6.png" width="90%" alt="Fragment of code from mail script" />
*Figure 1.6 - Fragment of code from mail script* 

Main script contains tree work inside: 

* pressure increasing in 20 iterations for every material in table 
* pressure increasing in 20 iterations for orientation range from 0° to 90° for one unidirectional material
* pressure increasing in 20 iterations for 10 iterations of working distance increasing from 1 to 91 mm and for 5 iterations of nozzle orifice diameters


####	ABAQUS FEA results

There was made 970 simulations at this moment. There will be diagrams how some initial parameters are affect on principal stress distribution. They are dependences principal stress from:

*	Pressure in one quasi-orthotropic material
*	Pressure in unidirectional material
*	Orientation in unidirectional
*	Different materials
*	Working distance
*	Different nozzle diameters

#####	Pressure distribution in quasi-orthotropic material

By quasi-orthotropic material means material, which have almost equal properties in more than one direction (unlike anisotropy) but not in every direction (unlike isotropy). In field of composite material by quasi-orthotropic material assume fabric reinforcement materials which has equal (or almost equal) amount of fiber in cross-directions. In this simulations used fibre fabric AGP-370H – carbon fabric with 0°/90° structure. Characteristic of this material shows in table . Principal stress dependence shown on a figure below:
<img src="../../img/projects/residual_stress/7.png" width="85%" alt="Principal stress dependence from pressure distribution" />
<img src="../../img/projects/residual_stress/7.gif" width="50%" alt="Principal stress dependence from pressure distribution" />
*Figure 1.7 - Principal stress dependence from pressure distribution* 

From the diagram above could be seen, that principal stress in direct ratio to applying pressure. FEA Mesh diagrams shows prospective distribution of principal stress – in directions of fiber reinforcement. Dependence line is linear –which means that principal stress will rise linear proportionally with increasing of AWJ pressure.

#####	Pressure in unidirectional material
By unidirectional material means strong isotropy one-directional fiber. For this simulation was used material – Mod – carbon one-directional fiber, characteristics of which could be found in the table. Orientation of fiber was taken in range from 0° to 90° with a step of 5°. On a figure 3.14 shows PS distribution for 0° and ±45°. More simulation results could be found in [appendixes](https://github.com/Balashov-Artem/Portfolio/blob/master/static/source_code/residual_stress/).
FEA mesh diagrams shows PS distribution on direction of 0° for pressure of 200Mpa.
<img src="../../img/projects/residual_stress/8.png" width="85%" alt="Principal stress dependence from pressure in unidirectional material" />
<img src="../../img/projects/residual_stress/8.gif" width="50%" alt="Principal stress dependence from pressure in unidirectional material" />
*Figure 1.8 - Principal stress dependence from pressure in unidirectional material* 



#####	Orientation in unidirectional material
Composite structure for this simulation, was modeled symmetrically. Actually, double-symmetrically. Because unsymmetrical structure cause addition interlaminar stress. General structure was **[+φ; - φ: - φ: + φ]s**. Material for this simulation was taken unidirectional carbon fiber Mod – the same one with previous simulation.
<img src="../../img/projects/residual_stress/9.png" width="85%" alt="Principal stress dependence from orientation in unidirectional material 1" />
<img src="../../img/projects/residual_stress/9_1.gif" width="50%" alt="Principal stress dependence from orientation in unidirectional material 3" />
*Figure 1.8 - Principal stress dependence from orientation in unidirectional material (left – 0°, middle – 45°, right – 90°)* 

First scheme shows the minimum principal stress in ±45°, which is pretty obvious. Nevertheless, shall be mentioned this islands on 10°-20° and 70°-80. FEA mesh scheme shows prospective PS distribution. 


#####	Different materials
Materials for this simulation was chosen as the most common composite materials in use in industry (table 1). Their properties were shown in a table. Applied pressure on these diagrams was 200 MPa, more simulations are in appendixes.
<img src="../../img/projects/residual_stress/10.png" width="85%" alt="Different materials 1" />
<img src="../../img/projects/residual_stress/10.gif" width="50%" alt="Different materials 2" />
*Figure 1.9 - Different materials (left blue are – carbon-fiber CM, middle orange – glass-fiber CM, right green – organic fiber (like Kevlar) CM)* 




#####	Working distance
By working distance means distance between nozzle and sample. With increasing working distance increasing area of pressure distribution. So the principal stress in CM structure as well. Applied pressure on these diagrams was 200 MPa, more simulations are in appendixes.
<img src="../../img/projects/residual_stress/11.png" width="85%" alt="Principal stress distribution from working distance" />
<img src="../../img/projects/residual_stress/11.gif" width="50%" alt="Principal stress distribution from working distance" />
*Figure 1.10 - Principal stress distribution from working distance* 

From distribution diagram could be seen that PS dependence curve close to quadratic line. This is because quadratic distribution pressure in working area.


#####	Different nozzle diameters
<img src="../../img/projects/residual_stress/12.png" width="85%" alt="Principal stress dependence from different nozzle diameters" />
<img src="../../img/projects/residual_stress/12.gif" width="50%" alt="Principal stress dependence from different nozzle diameters" />
*Figure 1.11 - Principal stress dependence from different nozzle diameters* 


Here is small mistake on this diagram – applied pressure was 300 MPa, material – AGP-370H – carbon fabric with 0°/90° structure. As per this diagram, the smaller diameter of orifice diameter always produces less yield stress, hence, it is always preferred to use smaller orifice nozzle diameter, unless it is not multi-pass cutting. Also, the smallest orifice diameter requires less pressure to achieve cutting velocity. Orifice nozzle diameter in one-pass cutting should be chosen according to average abrasive granule size.


#### Summary
To summarize this chapter, I could say that there are several ways to describe and observe how initial parameters of composite characteristics and AWJ machine affect on final property of cutting quality. 
Knowing the dependence between initial properties of composite and final quality could be applying any of the techniques from paragraph one. Knowing the dependence between initial properties of AWJ machining could be modified equipment how described in paragraph two.
First of all, it is mathematical algorithm, which has described on paragraph one, to determine adhesive parameters of interfacial layer of composite structure. It is quite important to observe this adhesive characteristic because it can solve the layering problem of AWJ machining. Adapting composite structure in a way of increasing interfacial layer’s thickness and increasing its elastic modulus could completely preserve composite sample from layering, because kinetic energy of jet won’t be enough to apply stress, which will destroy interfacial adhesive.
Second determination method – numerical simulation – preserve different goals, specific is determination of residual stress appearing from different initial parameters of composite and AWJ machine. These initial parameters affect each on specific different way, so it is quite important to observe all of them and then formulated a recommendation for adapting initial parameters. After 970 simulations I could certainly say, that increasing AWJ pressure will increase residual stress, as well increasing working distance or orifice diameter of the nozzle. Orientation affects on quality in a way of increasing residual stress for this type of material, which orientation aspire to isotropy.


###	Experiments

One of the reasons, why this work calls “high precision machining” is type of waterjet equipment. There are two significant principal scheme of AWJ machine. The classical one uses dry abrasive granules, such as sand or garnet, and it mixes with water inside nozzle right before cutting:
<img src="../../img/projects/residual_stress/13.png" width="60%" alt="Classic scheme of AWJ nozzle" />
*Figure 2.1 - Classic scheme of AWJ nozzle* 
		

This scheme also exists in three different variations: 

*	Forcing – when abrasive from abrasive tank delivered by addition air forcing;
*	Gravitation – when abrasive tank installed higher than nozzle and abrasive drop down to mixing module by gravitation force. This method ineffective due to possibility of sticking abrasive in tank.
*	Injections – the most common method, when abrasive sucked by vacuum force, which appears from water moving in pipe. 
Also, these exists one addition method to increase quality of cutting. It’s updating injection method by installing vacuum pump for abrasive on nozzle. This method uses OMAX corporation (patent belongs to them), and it calls “vacuum assist”
<img src="../../img/projects/residual_stress/14.png" width="60%" alt="Vacuum assist" />
*Figure 2.2 - Vacuum assist* 

The main point of this addition, is to equate kinetic energy of abrasive to kinetic energy of water. Speaking of which, whole principal scheme of this method assuming using nozzle diameter bigger than abrasive granule. Which is why the lowest diameter of nozzle for this scheme which could be found is 0.25 mm. Which is not enough to call precision. 
The another principal scheme of AWJ machining, which is appears to be nonclassical – developed for precision machining, and also could be using for polishing and lapping. The main difference of this scheme is another type of abrasive – wet abrasive lower average size of granule. It gives a chance to reduce nozzle diameter and increase precision of machining. Also, this abrasive mixes with pure water long before nozzle in special mixing tank, which is better, because kinetic energy of abrasive now is equal to kinetic energy of water, which reducing total energy wastage, and absent necessary of mixing this abrasive inside nozzle (fig 4.7).
With smaller orifice diameter there is needed less pressure, to obtain cutting speed velocity. For example, when classic scheme with orifice diameter of 0.5 mm uses 250-350 MPa water pressure to cut 2 mm steel plate, my equipment with orifice diameter of 0.12 mm and different type of abrasive needs only 20-25 MPa of water pressure to cut similar steel plate. 
For experiment I will use water jet machine, which consist from 2 parts – 6 degree of freedom robotic manipulator, main role of which is guide vanes, and high pressure water pump. Robotic manipulator is quite classic, nothing special or important, the only one quality of this robot what should be mentions is itsvery small critical measurement clearance. The model of it is ABB 2004. But the high pressure water pump appears to be very interesting part of equipment. There was built from the order spatially for AWJ machining. The main difference this pump is the way, how abrasive fracture mixing with water. Usually, general AWJ machine mix them at the very end of cycle, right before going through nozzle. This one makes it previously in a tank, for the reason to makes abrasive grain gain higher potential energy. Also, it is work not by power of electricity, but pneumatically, but this is not the point.
<img src="../../img/projects/residual_stress/15.png" width="90%" alt="Principal scheme of high pressure pump" />
*Figure 2.3 - Principal scheme of high pressure pump* 


Where, 1- air compressor 2-water inlet 3-air filter 4-inlet filter 5-airflow regulator 6- safety valve 7- manometer 8-air gate valve 9- damper 10- 12- nonreturnable valve 13-accumulator14-manometer 15- high pressure safety valve 16-high pressure three-way valve,17- high pressure safety valve 18- throttle flap 19- one-way valve 20- throttle valve 21,22- nonreturnable valve, 23- three-way valve, 24- abrasive container, 25- three-way valve 26- emission valve 27-manometer 28-high pressure shut off valve 29- nozzle 30- workpiece 31-table 32-jet collection box.
To be more precise there is another one structural diagram, which I made for a purpose of better understanding. It is shown on a fig (4.10) below. All indexes are the same.
<img src="../../img/projects/residual_stress/16.png" width="100%" alt="Structural diagram" />
*Figure 2.4 - Structural diagram* 



####	Measurement methodology

With the exception of x-ray, all experimental methods for detecting and measuring residual stresses in products relate to stresses of the first kind, which mainly determine the operational properties of the product.
All experimental methods can be divided (to some extent conditionally) into:

*	chemical;
*	radiographic;
*	harnesses;
*	polarization-optical;
*	thermal;
*	acoustic.

*Chemical methods*, most often aimed at detection and the definition of the sign of surface stresses are based on the phenomenon of the influence of residual (and not only) stresses on the corrosion resistance of the metal. It is not necessary to refer to the chemical methods where chemical treatment is used to remove the surface layers of products that are inherently mechanical.

All *mechanical methods* are destructive and consist in the measurement of deformations (most often elastic) after the removal of part of the material of the product, due to which there is a redistribution in the volume of internal stresses.
Mechanical methods are in limited use, since the product is subjected to partial or complete destruction and, in addition, it is not always suitable for the study of objects of the simplest form, such as spherical, or bodies of rotation with axial symmetry. This method is based on the fact that the residual stresses are mutually balanced inside the body. Therefore, when cutting the body in the study part, elastic deformations occur, which should turn to zero the resultant and the moment of residual stresses, thereby creating a new equilibrium of stresses in the body. By measuring the resulting deformation, it is possible in each case to determine the magnitude of the residual stresses acting in the remote part of the body.

*Radiographic methods* have the following advantages over mechanical and chemical: firstly, the object of study is preserved, if limited to the measurement of stresses in the surface layers; secondly, it is possible to measure the stress at each point of the surface at any, even asymmetric, stress distribution.

The *method of hardness* is to use the effect of internal stresses on the hardness of the stressed bodies.

The *polarization-optical method* is based on the study of deformations on the metal surface using optically active films.

The *thermal method* is to determine the residual stresses, using the ability of products to change size during annealing.

#####	Acoustic method

The basis of acoustic methods for determining stresses are nonlinear acoustic effects that occur in a deformed body during the propagation and interaction of sound waves in it.

One of the main causes of such effects is the nonlinear properties of a deformed solid. In particular, the speed of polarized sound waves propagating in a solid body depends on the level of stresses acting in it, the direction of oscillations of particles (polarization) and the direction of wave propagation. This phenomenon, called acousto-elasticity, is the basis of the considered method of stress analysis in machine parts.

To excite elastic waves, usually used ultrasonic emitters, since ultrasonic waves have a high penetrating power, which is practically independent of the aggregate state of the studied materials. There are many methods for measuring the speed of ultrasonic waves. When measuring the propagation time of the ultrasonic wave in the test medium is compared with the time of its propagation in a reference medium. In solving practical problems with the help of acoustic strain measurement relative error does not exceed 3·10-4.

In the study of nonuniform stress fields by ultrasonic method, averaged stresses are obtained on the base, which is determined by the size of the measuring sensors. If the stresses vary in the thickness of the samples, their averaged values are obtained. The considered method is non-destructive, allows to measure residual stresses both on the surface and inside the body, provides efficiency of control, high resolution and accuracy. However, this method has disadvantages: the complexity of the experiment, the use of complex equipment, limited implementation of the method in production and operation.

French developers from CANTOR COLBURN patented a method of measuring residual stresses using ultrasound in the United States. In this case, the time of the wave passing between the two ends of the workpiece in the loaded and unloaded state is measured. The stress calculation is based on the comparison of the angles of inclination of the load diagrams.

Acoustic methods of residual stress analysis were successfully applied to determine the stress state in deformed metal composite materials by the authors . This technique is based on the features of the macrostructure of fibrous composite materials and allows to determine the axial residual stresses in the fibers and matrix, which are predominant and occur in heterogeneous materials in the manufacturing process and subsequent processing.

If the ends of the composite sample are rigidly fixed in a special device and the matrix layers are dissolved, the remaining system of rigidly clamped fibers will qualitatively reflect the distribution of residual stresses in them.

To measure the frequency of natural oscillations of fibers etched from the samples of composites and having the initial voltage, a special installation was used (Fig. 4.11). Measurements were carried out at the main resonance frequency using frequency meter 2. The moment of resonance was determined by the oscilloscope 6 using a shielded piezoelectric sensor 4. Amplitude control of the oscillations of the fiber for obtaining a value of the resonant frequency with the minimum error was carried out by adjusting the energy output of a sound generator 1 or by passing through a sample of 7 low-voltage power 0,01...0,03 And the measurements of stresses in the fibers of a nonmagnetic material.
<img src="../../img/projects/residual_stress/17.png" width="75%" alt="Scheme of installation for determining the residual stresses in the fibers of composite materials" />
*Figure 2.5 -  Scheme of installation for determining the residual stresses in the fibers of composite materials: 1 — generator (type 3 G-10); 2 — frequency (type F-599); 3 — excitation electromagnet; 4 — piezoelectric sensor; 5 — low frequency amplifier (type UCH-2); 6 — oscilloscope (type C1–19); 7 — sample* 

The fibers in the real composite have random deviations from the straightness as a result of manufacturing technology, uneven deformation during processing by pressure and other reasons. After etching the matrix, the bent fibers of the pinched sample are further extended by a certain value Dl f (fictitious deformation) depending on the degree of curvature. Processing of statistical characteristics of irregularities in the arrangement of fibers on the basis of radiographs of flat samples of aluminum-tungsten composites, aluminum-steel X18 H9 T, obtained by hot rolling, and comparison of the parameters of curvatures with the calculated ones, showed satisfactory accuracy of the approximation of curvatures by periodic sinusoidal function. Taking into account the curvature of the fibers, the system of equations for determining the axial residual stresses will have the form:
<img src="../../img/projects/residual_stress/f6.png" width="55%" alt="" />

Where n — harmonic number; a — vibrational amplitude; l — string length; σ — stress; ρ — string density, EI – wire stiffness, F — cross-section area of fiber; E — fiber elastic modulus ; I — moment of inertia; r, l — fiber geometrical parameter, σfiΣ — total residual stree in the i-th fiber; σ0i — final residual stress in the i-th fiber, obtained by equation (5.2) or (4); Δσti — stress dropping, Δσt1i — stress dropping, associated with the stress relaxation; Δσt2— stress dropping, associated with the pliability of the device supports (Δσet = εсf ·Ef), Vf — fiber volume ratio; σ’m — average by cross-section area axis residual stress in matrix; σf — average by cross-section area axis residual stress in fiber.

Generally types for QC (quality control) depends on accessible in each and every enterprises and laboratories, but as a one justice thesis for all types is nondestructive inspection better that destructive. For QC in this work were chosen acoustic method as the one with better correlation between preparation time and results’ quality. Also, this method could not only observe surface quality after machining, and also determine residual stress. Which is necessary to understand, because surface quality measure – roughness – is not fully describe cutting area behavior after machining, but residual stress is one of the most important property. 


####	Experiments result

A number of experiments were pursued to determine the residual stress in a polymer composite material (PCM) samples by acoustic emission method. The tested samples in quantity (N=60) were divided into the following groups, depending on the examined cutting parameters: - pressure changing group (N=20), orientation angle changing group (N=24), feed rate changing group (N=16).
Residual stress distribution in a first group will show on a figure:
<img src="../../img/projects/residual_stress/18.png" width="100%" alt="Residual stress distribution according to machining pressure" />
*Figure 2.6 - Residual stress distribution according to machining pressure* 


From this diagram could be understand, that Residual Stress (next, RS) expectable increase with machining pressure increasing, which is perfectly corresponding to a numeral of simulation from chapter 4.4.1. Here is (fig 4.13) intercomparison diagram between simulation and experiments.
<img src="../../img/projects/residual_stress/19.png" width="60%" alt="Experiment data in comparison with simulation for pressure increasing" />
*Figure 2.7 - Experiment data in comparison with simulation for pressure increasing* 
		

Experimental data for orientation angle quite different in values from simulation, but exact the same in distribution format. This stipulated by different composite structure – for simulation I chose unidirectional carbon fiber, while in experiment were used carbon textile – double-directional fiber. On a fig 4.14 may be seen experimental data for a second group of orientation change.
 <img src="../../img/projects/residual_stress/20.png" width="100%" alt="Residual stress distribution according to orientation angle in composite structure" />
*Figure 2.8 - Residual stress distribution according to orientation angle in composite structure* 


Here weren’t made experiment’s analysis for 90° orientation because of symmetric structure of double-directional fiber – it is completely the same as 0°. On a figure 4.15 shown intercomparison between simulation and experiment’s data.
<img src="../../img/projects/residual_stress/21.png" width="60%" alt="Experiment data in comparison with simulation for different orientation composite fiber" />
*Figure 2.9 - Experiment data in comparison with simulation for different orientation composite fiber* 


For the third group of experiment’s data I have not made any simulation, because my simulation model represents residual stress dependence from feed rate with insufficient accuracy. But I assume this dependence to be quite essential so I request experiments. Data are shown on a fig 4.16.
<img src="../../img/projects/residual_stress/22.png" width="100%" alt="Residual stress distribution according to feed rate" />
*Figure 2.10 - Residual stress distribution according to feed rate* 



### Conclusion


As a conclusion, I should write recommendation how to choose AWJ machining parameters for different types of composite, but previous analysis shows that for each and every type of composite, it’s thickness and structure orientation there is preferred distinct initial parameters. Furthermore, all types of initial parameters definition based on some empirical coefficients, so anyhow some foreplay should take place before machining.

In general case, I could say that algorithm of initial AWJ parameters definition shall be next:

*	prepare the test sample;
*	define the minimum pressure required to cut in quiescent state (with no traverse speed);
*	define the separation speed – maximum speed while jet cuts the sample with the pressure 1.25 – 1.5 from minimal;
*	according to the simulations diagrams, choose the preferred pressure, traverse speed and working distance;
*	traverse speed could be update by verifying roughness and kerf taper

Orifice nozzle diameter should always as small as possible. Using bigger orifice diameters could be justified only while several pass cutting. Also, orifice nozzle diameter is not as important property as cone angel of nozzle, or relative between initial and orifice diameters. At first glance, it may seem that working distance is not an initial parameter because it only depends on the focus distance of nozzle cone, but it is not true. According to pressure distribution model in Chapter 4, with the different nozzle cone and working distances steed up as focus distance pressure distribution could be different, and affect on yield stress of CM. So it is always preferred to make some simulations while choosing cutting regime.

Temperature of water-abrasive compound usually neglected, considering energy failure criterion, but this this wrong, because it may have a significant affect on critical deformation energy. However, most abrasive compound have they own working temperature 20° – 25° (polishing and cutting wet abrasive chilling at 10°-15°). 

For the most specified cases composite structure could be updated by inserting additional layers in different directions to preserve structure which aspire to isotropy. In general cases it could mean adding layers of ±45° orientation, but specific cases require specific solutions – the orientation of inserted layers could also be opposite from orientation of the most frequent layers.

Water for in cutting environment should be reducing by installing water and cooling pump in area of cutting. Best solution – is to combine vacuum pump with air ventilator opposite to each other. Also, cooling the water droplet will decrease their potential energy, hence, decreasing Brownian movement. Installing this vacuum system also require to satisfy safety measures, because lateral discharge of abrasive waterjet machining is abrasive, which could be extremely dangerous for workers.