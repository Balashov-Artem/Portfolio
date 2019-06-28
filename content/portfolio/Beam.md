+++
title = "The beam with strut"

image = "img/portfolio/beam_with_strut/Beam.jpg"
description = "Design composite carbon beam with fiber-glass strut and articulator connectors."
date = ""

draft = false
showonlyimage = false

weight = 3
+++

Design composite carbon beam with fiber-glass strut and articulator connectors.

<img src="../../img/portfolio/beam_with_strut/Beam.jpg" width="100%" alt="Beam with strut isometry" />

-   [Initial data](#initial-data)
-   [Beam profile definition](#beam-profile-definition)
-   [Design loads definition](#design-loads-definition)
-   [Internal forces diagrams](#internal-forces-diagrams)
-   [Paperwork](#paperwork)
-   [FEA](#FEA)
-	[Beam manufacture](#beam-manufacture)
-   [Conclusion](#conclusion)

---


#### Initial data
Beam has been designed to bearable irregularly distributed load from 75 kN at the assembly unit to -60 kN at the end.  
<img src="../../img/portfolio/beam_with_strut/Beam-with-strut.jpg" width="100%" alt="Beam with strut" />


<table border="1" width="100%">
   <caption>Materials</caption>
   <tr>   <th>Part</th>   <th>Type</th>         <th>Material</th>   </tr>
   <tr>   <td>Shelfs</td> <th>Carbon fiber</th> <td>IM6, 65%</td>   </tr>
   <tr>   <td>Side</td>   <th>Carbon cloth</th> <td>6GfH, 58%</td>   </tr>
   <tr>   <td>Srtut</td>  <th>Fibrf-glass</th>  <td>E-glass, 60%</td>   </tr>
</table>   

---


#### Beam profile definition

In this work beam profile has form of I-section (or turned H-section). This kind of profile provides a good enough access to assembly units, fasts and also simple at manufacture. Moreover, with symmetrical about load plane (plane, in which the loads acting)  absent necessity of founding flexural center.

<img src="../../img/portfolio/beam_with_strut/Front.png" width="60%" alt="Front" />
---


#### Design loads definition 

According to analytical model of beam, in each section of beam there are acting generalize forces - transverse force, bending moment and normal force.

<img src="../../img/portfolio/beam_with_strut/Load-scheme.png" width="100%" alt="Load-scheme" />

---



#### Design loads definition  

This generalize forces - also called internal forces - are depended of the actual, real forcer - also called external - **pressure** in this cases. Because the pressure distribution is linear but **non-constant**, so internal forces also will have non-constant distribution  across the beam. Moreover, because the mathematical definition of IF is integrated, their distribution will nonlinear.

After IF definition, there is needed to build a graphical distribution of them. This is necessary to survey character of their distribution. In which point one force is stretch beam fiber and another is compress, and in which vice versa.


<img src="../../img/portfolio/beam_with_strut/Rotation-moment.jpg" width="60%" alt="Rotation-moment" />
<img src="../../img/portfolio/beam_with_strut/Transverse-force.jpg" width="60%" alt="Transverse-force" />

---

#### Paperwork

For this work were made whole package of technical documentation, or engineering data. Here are some example of drawings.
Drawings, by the way, were maid exactly from 3D models, which also were maid in cad system CATIA V5.

There how is looking only beam with assembly units:
<img src="../../img/portfolio/beam_with_strut/Beam-with-assembly-units.jpg" width="100%" alt="Beam with assembly units" />

Composite laying scheme of beam looks like:
<img src="../../img/portfolio/beam_with_strut/Layout-scheme.jpg" width="100%" alt="Layout-scheme" />

Steel-made fitting - first connection unit:
<img src="../../img/portfolio/beam_with_strut/Fitting.jpg" width="100%" alt="Fitting" />

Strut was made by spooling fiber-glass and gluing assembly units:
<img src="../../img/portfolio/beam_with_strut/Strut.jpg" width="100%" alt="Strut" />
---

#### FEA
Attachment fitting, which connect beam with strut made from 30ChGSA Steel and with the use of the [`Topology optimization`](https://en.wikipedia.org/wiki/Topology_optimization).
<img src="../../img/portfolio/beam_with_strut/Fitting_MFE.jpg" width="100%" alt="Fitting_MFE" />
---

#### Beam manufacture

The manufacture technique for this beam is following:

-	I-section half-part (C-section) is made by laying out composite layers. On a negative molding form manage side layers, which are provide side stiffness, then those layers which provide side resistance, than in interlace there are goes shelf layers, composite gain and then again composite layers. It is necessary to ensure that side layers cover shelfs layers.
-	Technological **_mending plate_** are made from 3 groups. Inner one - group from the same with side material. The middle one - the shelf layers. And the outer one - layers that protect monodirectional side fiber from mechanical damage and layering (lay or fiber stratification).
-	Moulded half-parts glue in assembly fixture with filler (honeycomb). At this very time there are connection units sets-in. After that glue to them technological mending plate.
-	After glue condensation in the CU places drilling bolt holes, inserts metal pillow and fasts (connection elements).

---


#### Conclusion

* **Shelfs** weight - 5.8 kg
* Side **thickness** - 3.6 mm
* **Side** weight - 2.44 kg
* Technical ***mending plate*** weight - 3.375 kg
* **Metal parts** weight - 11.25 kg
* **Inserts** weight - 3.54 kg
* Whole **_beam_** weight, considering fasts - 39 kg 


##### Strut properties:

* Rod **length** - 1570 mm
* Rod **middle radius** - 49 mm
* Rod side **thickness** - 6 mm
* Composite parts of rods weight - 6.86 kg
* **Adapters** weight - 3.88 kg
* Whole **strut** weight - 10.75 kg