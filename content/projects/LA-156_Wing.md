+++
draft = false
image = "img/projects/LA-156_Wing.jpg"
date = "2016-11-05T18:25:22+05:30"
title = "NEED TR    LA-156 Wing skin"
showonlyimage = false
description = "Design of an LA-156 Wing skin"
+++

Design of an LA-156 Wing skin.

<img src="../../img/projects/LA-156_Wing/1.png" width="100%" alt="Scheme" />

## Contents
---

-   [Introduction](#introduction)
-   [Work scheme](#work-scheme)
-   [Input data](#input-data)
-   [Parametrize Master-Geometry](#parametrize-master-geometry)
-   [Calculating](#calculating)
    -   [Pressure type allocation](#pressure-type-allocation)
    -   [Adhesive connection](#adhesive-connection)
    -   [Skin types comprasion](#skin-types-comprasion)
    -   [Figurativly parts](figurativly-parts)
-   [Modeling](#modeling)
-   [FEM calculation](#fem-calculation)
-   [Technology and manufacturing](#technology-and-manufacturing)
    -   [Segments lining](#segments-lining)
    -   [Modling frame](#modling-frame)
    -   [Materials and equipment list](#materials-and-equipment-list)
-   [Conclusion](#conclusion)
-   [Tech-documentation](#tech-documentation)

---

### Introduction  
The aim of this work was a design of covering for the wing LA-156, as a part of acomplex teamwork. The operation loads of the skin panels were calculated based on the rationing loads of the wing. The structure of covering was designed in various type, qualitative analysis and selected final version of sandwich panel were calculated. A shear stresses of compounds were calculated and verification of a calculation by finite element method was conducted. The second section is devoted to the manufacturing of top panel, considered as the most typical. Finally, the price of the panel and cost manufacturing process were calculated. In addition, a complete set of design documentation was developed.


---

### Work scheme

Project's and construction's tasks were separated by the next scheme:

* Stress and loads definition that acting on a wing
* Design of longitudinal frame 
* Design of transversal frame
* Wing skin design
* Wing elements motorization design

This work is about wing design from composite materials (CM). Was made assembly scheme and parametrized master-geometry. Was design skin parameters, selected and explained constructive-manufacture solutions, developed assemblage schemes for skin-longitudinal frame and skin-transversal frame. For the upper skin panel was designed a manufacturing process, were determined weight, structural, manufacture and economical advantages of making wing from CM.
<img src="../../img/projects/LA-156_Wing/2.png" width="110%" alt="Working scheme" />

---

### Input data

Input data for constructional design are geometrical wing parameters and internal force factors (next FF), that was defined on a first step. Stress distribution characteristics along wing panels is next - from ambient medium on wing panels act only aerodynamic forces: ascentional force and air resistance force. Distributed external forces transformed into system of normal and tangential stresses. It follows that we can rewrite internal stresses as stresses that only act in a plane surface of panel and distributed pressure.

<img src="../../img/projects/LA-156_Wing/3.png" width="90%" alt="Stress" />

### Parametrize Master-Geometry
For the reason of variation geometrical parameters was design a parametrized master-geometry in program complex CATIA V5. All input sizes as well as amount of longerons and ribs and even airfoil type controls from excel-file and than transform as parameters in CATIA. Also, was made a simple program to define geometrical parameters of 4-digit NACA airfoil. It could be found [here](https://github.com/Balashov-Artem/Portfolio/blob/master/static/source_code/LA-156_Wing/Naca_airfoil.xlsx). 
<img src="../../img/projects/LA-156_Wing/4.png" width="100%" alt="Parametrize Master-Geometry" />

---

### Calculating

For a pin-ended plates with a symmetrical structure stress Nx, Ny and qxy will not cause a deflection and transversal pressure - membranous stress. As orthotropy, as well as symmetry almost valid, because with load and temperature application will not arise undesirable internal stresses and deformations inside the panel, that are connected with, for example, interference coefficients. And if this shear deformation are bounded by frame - they cause additional tangential stresses. 
Also, nonuniform structure by thickness (unsymmetrical order of plies) while temperature changes will cause a temperature 'moment of force' - the pair of force that will bend and twist the panel, which is in turn will cause a buckling of panel. 

<img src="../../img/projects/LA-156_Wing/5.png" width="80%" alt="Geom-size" />

---

#### Pressure type allocation

Have to note, that distributed normal and tangential stresses, that acts inside the panel was defined for a 2 calculation cases (next - CC), while pressure - for 3. Yhe last one is connected with transform calculation scheme - pressure represent distributed uniform. Scheme [4] of pressure distributed shows on a picture below.

<img src="../../img/projects/LA-156_Wing/6.png" width="50%" alt="Profile wing pressure" />

#### Figuratively parts
Before designing parts and properties of wing skin, it (wing skin) should first be separated on a theoretical (figuratively) parts, within which properties will stable and unaltered. Calculation and definition of constructive parameters will make by calculative scheme of layer plate (wafer). For defined sizes of this parts it is needed to orient on manufacturing of making this skin, and ribs position - supports, within which panel parts should be stable. 

<img src="../../img/projects/LA-156_Wing/7.png" width="60%" alt="Figurativly parts" />

---

#### Adhesive connection

<img src="../../img/projects/LA-156_Wing/8.png" width="100%" alt="Adhesive connection" />

In this work was selected surface type of connected. There are several reasons for this. First of all, skin thick enough, so installing connected element (of 'fast', but next is CE) could intervene on aerodynamic contour or we should increase thickness near connection area to make a chance to install CE with countersunk head. Secondly, field of tangential stresses are not high enough. For third, because of material of skin is similar (structure and properties) with the wing frame (longeron and ribs) materials (carbon fiber HEXPLY IM6) means adhesive characteristics of glue connected will maximal. And the last one, mechanical connecting will makes itself as stress concentrator, and must us to increase thickness of the longeron's shelfs. In this case weight advantage of composite wing instead of metal one will grade by the necessaries of reinforcement of it. 

---

#### Skin types comparison

Here shall be noted, that defined wing skin type based only on weight efficient is carefree, because it has to be contemplated it’s manufacturing process, operation conditions, equipment that in use and connection method (between panels and panel with load-carrying spar and ribs).
While it is easy to connect plain panel with the rest elements with almost any connection type, it is quite a wasteful process with stringer panel.
<img src="../../img/projects/LA-156_Wing/9.png" width="80%" alt="Types of skin" />

With this arrangement of longitudinal power elements wing leading edge have to be plain. From technological reasons (quite hidebound across section) back panel above plain flap also have to be plain.
From calculations results could be seen, that most efficient are sandwich panels (panels with fillers). However, properties of each section are different from each other, which leads to complexity of manufacturing process of that kind of panels. And while amount of composite layers quite simple to control, then filler have to be ordered according to calculations.
  

---

### Modeling

Modelling of whole wing and panels specifically were made using software CATIA V5. To make quick access to wing lift devices was made provision inspection manhole.
<img src="../../img/projects/LA-156_Wing/10.png" width="100%" alt="Wing with manway" />
<img src="../../img/projects/LA-156_Wing/11.png" width="60%" alt="Lock" />
<img src="../../img/projects/LA-156_Wing/12.png" width="60%" alt="Segment" />

---

### FEM calculation

After defined geometrical sizes and overall dimensions of a skin panels, were carried out flow of tangential stresses, using methodology of thin-walled bar. Also, by way of another checking calculation were provided calculations using FEA (Finite Element Analyses). These calculations were carried out for leading edge of the wing and back panel above plain flap by uninform pressure distribution. Boundary conditions were rigid attachment in a places of connections. 

<img src="../../img/projects/LA-156_Wing/13.png" width="100%" alt="FEM" />

---

### Technology and manufacturing

So far the wing skin is collectable it contains from several parts. The most loaded from them are upper panel, lower, aerodynamic fillet, leading edge and back panel above plain flap. The back part which is directly above plain flap, but placed in a middle of the wing console was not calculated with stress – it is used only for covering and locking airfoil contour. From there very considerations parts, which are close on airfoil shape in a places with ailerons also weren’t calculated. From technological reasons their thickness will be 2 monolayers, or 0.84 mm, and used manufacturing technic, as well as for other plain panels – leading edge, aerodynamic fillet and upper back panels – is laying out method of fiber textile prepreg on negative molding form with continuous vacuum molding in autoclave.

Construction fabricability is next:

* Upper panel presented as sandwich panel;
* Filler is foam plastic brand ROHACELL® 71 XT;
* Composite layers made from prepreg brand HEXEL, which contains from fiber textile W3T282 and epoxy resin F155;
* Panel has high quality of outside aerodynamic surface;
* For manufacture needs 18 running meters of prepreg and 2 slab boards of foam plastic 2500x1250 mm2 with 2 mm thickness;
* Manufacture method does not allow producing several details at the same time, however, with high scale of production there is a possibility of forming two same panels simultaneously by conditions they are made in a different moulding forms;
* In so far as transversal stress flow (TSF) shall transform directly from skin panels to load-carrying spar and load ribs, in a places of connection there are shall not be filler, so upper and lower panels will have segment structure;
* Connection places has increased requirements to a surface quality;
* For connection was used membranous hot cured glue Redix 312;
* After producing panels and before assembling could pass some time period and connection surfaces could be damaged, so as a preventive measure these surfaces shall be covered with lining (primer) by Redux 100;
* The panel has an inspection window which is also serve for exploitation needs.


---

#### Segments lining


Because of quite curved shape sawing was made with using laser projector LAP Laser COMPOSITE PRO on a coordinate desk Eastman M9000 with vibrocut tool EC-Cutter. To execute sawing scheme was used CAD software CATIA V5. Lower layers of prepreg, which are compiling aerodynamic contour – laying out with one single piece of textile. Upper layers compiling from 10 lying along pieces of prepreg textile (for each ply). Membranous glue shall be disclosed according to foam plastic sawing scheme with tolerance for a side edges of filler. 
Scheme of carbon textile segments sawing shown on a figure below.

<img src="../../img/projects/LA-156_Wing/14.png" width="90%" alt="Segments of layers" />

Due to high deformation angle of prepreg we have a chance to laying out segments with inspection window almost without deformation. Sawing also was made using CATIA V5 software, module “Composite design”. Colored with yellow zones with textile deformation angle more than 30°.

<img src="../../img/projects/LA-156_Wing/15.png" width="80%" alt="Segment of layer" />


---

#### Modling frame

As far as external surface has aerodynamic quality, laying out shall be produced on a negative molding form.

<img src="../../img/projects/LA-156_Wing/16.png" width="90%" alt="Modeling form scheme" />  

Because the panel is quite curved – difference between lowest and uppermost points in a normal to panel plain is 78 mm – molding form have to be produce on a roll-bending machine from leaf metal with a thickness of 8,5 mm. Because producing press matrix and hob for a 4-th meter stamp is quite expensive one-time job, leaf sample for molding form previously bended on a roll-bending machine with a clearance of 3 mm, and then produced final shape of continuous milling machine. Molding cannot be combined from pieces by welding, because welding joint will become ununiform heat transfer concentrator while molding, also while welding could happen buckling, which deform aerodynamic shape of the airfoil. Due to more than 100 kg weight of this leaf, it placed on a frame with rails.

<img src="../../img/projects/LA-156_Wing/19.png" width="100%" alt="Modeling form" />  

While preparative molding form have be fixed, cleaned by plastic mechanical tool and water from previous usage, dried and deoiling. After this measures form will be ready for following usage.

<img src="../../img/projects/LA-156_Wing/17.png" width="100%" alt="Shaping" />

Laying out shall be proceed on a molding form with previously delivered separation layer. While laying out have to preserve edge conjunction along whole surface to prevent pap sans cavities after forming. Laying out process is next: on a molding form lay down 2 lengthwise plies of prepreg textile. Tightness shall be preserved by using forming roll. After that goes laser projector to position membraned glue and foam plastic segments. After second layer of membraned glue on segments laying out with next laser program shall lay out inner plies of composite. Envelopes for machining shall be leaved according to drawings.

<img src="../../img/projects/LA-156_Wing/18.png" width="60%" alt="Cure sycle" />

Due to high requirements to a surface quality molding this panel will be in autoclave press under high pressure.
According to manufacturer recommendation, maximum molding temperature shall be less than 127° for prepreg, and the molding pressure from 310 to 103 kPa. Molding time variated according to heating and cooling rates. The heating rate shall be from 1 to 4 °C/min, and cooling rate – maximum 3°C/min. Cured cycle provided by the manufacturer is shown on a diagram below. Final autoclave pressure – 3 atm.

---

#### Materials and equipment list

In a table below with two columns are shown list of used material and equipment.

<table border="1" width="100%">
   <caption>Materials and equipment</caption>
   <tr>   <th>Equipment</th>               <th>Model</th>                     <th>Material</th>          <th>Model</th>   </tr>
   <tr>   <td>Autoclave</td>               <th>Econoclave EC6x20</th>         <td>Prepreg</td>           <td>HEXCEL HEXPLY W3T282 / F155</td>         </tr>
   <tr>   <td>Vacum pump</td>              <th>Value v-I 260SV</th>           <td>Rigid foam</td>        <th>ROHACELL 71 XT</th>                      </tr>
   <tr>   <td>Coordinate table</td>        <th>Eastman M9000</th>             <td>Adhesive fil m</td>    <th>HEXCEL Redux 312</th>                    </tr>
   <tr>   <td>Workbanch  foam cutting</td> <th>CPД "СКАТ"</th>                <td>Separation layer</td>  <th>Lusin Alro LL 301</th>                   </tr>
   <tr>   <td>Lazer projecting</td>        <th>LAP Laser Copmosite PRO</th>   <td>Vacuum film</td>       <th>Fiber Glast 1782-A</th>                  </tr>
   <tr>   <td>Vibrocut</td>                <th>EC-Cutter</th>                 <td>Vacuum pupe</td>       <th>Spiral pupe 10/12</th>                   </tr>
   <tr>   <td>Angle grinder</td>           <th>Proxxon WP/E</th>              <td>Germetic strip</td>    <th>ГерЛен УТ/3-13</th>                      </tr>
   <tr>   <td>Graver</td>                  <th>Proxxon LWB 220/E</th>         <td>Perforated fabric</td> <th>Fiber Glast 1540-А</th>                  </tr>
   <tr>   <td>Acustic crack detector</td>  <th>ИД-91М</th>                    <td>Sacrificial layer</td> <th>Лавсан</th>                              </tr>
   <tr>   <td>Acustic leak detector</td>   <th>ТИАМ-3</th>                    <td>Priming layer</td>     <th>Resux 100 series</th>                    </tr>
   <tr>   <td>thermal imager</td>          <th>Testo 882</th>                 <td>Consumables</td>       <th>De-icing agent, napkins, sandpaper</th>  </tr>

  </table>



---

### Conclusion

Summary I would say, that in this work was made a proof-of-concept design of wing skin for airplane LA-156. Was calculated active on a panel external loads and pressure by several calculation method and for several settlement cases. Was design a construction and composition of power frame and panel characteristics. After that it was developed manufacturing process for upper, as the most complicated panel, and calculated it self-cost. After transversal stress field calculation was completed checking calculation and FE Analyses. Final characteristic on upper panel is next:

Was design composition of power units and connection method between them and panels. 
 

* 4 plies, or 1,68 mm of composite material for upper and lower panels in total
* 6 plies, or 2,52 mm of CM for back panel
* 8 plies, or 3,36 mm of CM for lead edge
* 15 mm of foam plastic for filler
* Glue connection method


At third chapter was observed and described manufacturing process for upper panel for LA-156 wing skin. During producing were involved a lot of equipment and at least 2 workers, though the cheapest manufacturing process was one the development criterion, the criterion of appropriate quality was more important. However, with the condition of full-scale production and producing several parts of the wing simultaneously – self cost become proportional for each part.
Also, manufacturing process was developed considering multi-functional equipment for producing other wing parts, such as longeron, ribs, side-members, ailerons and wing flaps. While producing upper panel coefficient of used material theoretically shall be 58%, needful area of CM prepreg – 18 running meters, foam plastic – 2 plates, 17 running meters of membrane glue. Producing tume is 1005 min and full self-cost is 314 thous. HRN, or 11,200 USD


<img src="../../img/projects/LA-156_Wing/20.png" width="100%" alt="Panel plate" />

### Tech-documentation

A full package of paperwork and engineering documentation could be found by [this link](https://github.com/Balashov-Artem/Portfolio/blob/master/static/source_code/LA-156_Wing).

<img src="../../img/projects/LA-156_Wing/21.png" width="100%" alt="Tech documentation" />
<img src="../../img/projects/LA-156_Wing/22.png" width="100%" alt="Tech documentation2" />