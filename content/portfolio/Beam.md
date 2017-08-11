+++
draft = false
image = "img/portfolio/Beam.jpg"
date = "2016-11-05T18:25:22+05:30"
title = "The beam with strut"
showonlyimage = false
+++

Design composite carbon beam with fiber-glass strut and articulator connectors.
<!--more-->

<img src="../../img/portfolio/beam_with_strut/1.jpg" width="100%" alt="Beam with strut isometry" />

-   [Исходные данные](#исходные-данные)
-   [Выбор профиля балки](#выбор-профиля-балки)
-   [Определение проектных нагрузок](#определение-проектных-нагрузок)
-   [Эпюры внутренних силовых факторов](#эпюры-внутренних-силовых-факторов)
-   [Конструкторская документация](#конструкторская-документация)
-   [МКЭ](#мкэ)
-   [Заключение](#заключение)

#### Исходные данные
Beam has been designed to bearable irregularly distributed load from 75 kN at the assembly unit to -60 kN at the end.  
<img src="../../img/portfolio/beam_with_strut/2.jpg" width="100%" alt="Beam with strut" />


<table border="1" width="100%">
   <caption>Materials</caption>
   <tr>   <th>Part</th>   <th>Type</th>         <th>Material</th>   </tr>
   <tr>   <td>Shelfs</td> <th>Carbon fiber</th> <td>IM6, 65%</td>   </tr>
   <tr>   <td>Side</td>   <th>Carbon cloth</th> <td>6GfH, 58%</td>   </tr>
   <tr>   <td>Srtut</td>  <th>Fibrf-glass</th>  <td>E-glass, 60%</td>   </tr>
  </table>   
.


#### Выбор профиля балки
В данной работе балка изготавливается в виде двутавра. Такой профиль обеспечивает достаточно свободный доступ к узлам крепления, крепежным элементам, а также прост в изготовлении. Кроме того, в симметричном относительно плоскости действия нагрузки профиле отсутствует необходимость в нахождении центра изгиба.  
<img src="../../img/portfolio/beam_with_strut/3.png" width="60%" alt="" />


#### Определение проектных нагрузок 
Согласно расчетной схеме бруса в каждом сечении балки действуют обобщенные силовые факторы – перерезывающая (поперечная) сила, изгибающий момент и осевая сила.  
<img src="../../img/portfolio/beam_with_strut/4.png" width="100%" alt="" />



#### Эпюры внутренних силовых факторов  
После расчета (ВСФ) необходимо построить эпюры распределения их по длине балки. Это необходимо для того, чтобы наблюдать характер их распределения. Ниже приведены эпюры – распределения ВСФ вдоль длинны балки.  
<img src="../../img/portfolio/beam_with_strut/5.jpg" width="60%" alt="" />
<img src="../../img/portfolio/beam_with_strut/6.jpg" width="60%" alt="" />

#### Конструкторская документация
There how is looking only beam with assembly units:
<img src="../../img/portfolio/beam_with_strut/7.jpg" width="100%" alt="Beam with assembly units" />

Composite laying scheme of beam looks like:
<img src="../../img/portfolio/beam_with_strut/8.jpg" width="100%" alt="Laying scheme" />

<img src="../../img/portfolio/beam_with_strut/9.jpg" width="100%" alt="Fitting_MFE" />

Strut was made by spooling fiber-glass and gluing assembly units.
<img src="../../img/portfolio/beam_with_strut/11.jpg" width="100%" alt="Strut" />


#### МКЭ
Attachment fitting wich connect beam with strut made from 30ChGSA Steel and with using [`Topology optimization`](https://en.wikipedia.org/wiki/Topology_optimization).
<img src="../../img/portfolio/beam_with_strut/10.jpg" width="100%" alt="Fitting" />

#### Технология изготовления балки


Изготавливается полуформа двутавра методом выкладки. На негативную оснастку укладывается слои стенки, обеспечивающие ее устойчивость, осле чего укладывается часть слоев стенки, обеспечивающих ее прочность, потом чередуя выкладываются слои полки, композитного усиления и оставшееся слои стенки. Необходимо обеспечить, чтобы слои стенки закрывали слои полки и усиления со всех сторон. Технологические накладки изготавливаются из 3 групп слоев. Внутренняя - группа слоев из того же материала, что и материал стенки, после чего часть слоев полки. Третья группа - слои, которые защищают однонаправленное волокно стенки от механических повреждений и расшелушевания. Изготовленные и отформованные части полуформы склеиваются в сборочном приспособлении с сотовым заполнителем, в это же время позиционируется стойка-балка и узел навески, после чего к ним клеятся технологические накладки. После отверждения просверливаются отверстия под КЭ, устанавливаются металлические вкладыши-усилители и устанавливаются КЭ.
 

#### Заключение

* Вес полок -5 805 г
* Толщина стенки – 3.6 мм
* Вес стенки – 2 438 г
* Вес технологических накладок – 3 375 г
* Вес - металлических деталей – 11.242
* Вес вкладышей – 3.54
* Вес всей балки с учетов веса КЭ – 39 070 г

Параметры подкоса:

* Длинна стержня – 1570 мм
* Средний радиус стержня – 49 мм
* Толщина стенки стержня – 6 мм
* Вес композитной части стержня – 6 863 г
* Вес переходников – 3 882 г
* Вес всего подкоса – 10 745 г