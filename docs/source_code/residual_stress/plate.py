radius = 100
mat1 = {'name': 'AGP3705H', 'E1': 77000.0, 'E2': 75000.0, 'G12': 6500.0, 'mu12': 0.06, 'd': 0.42, 'dens': 0.0016}
mat2 = {'name': 'AGP3705H', 'E1': 77000.0, 'E2': 75000.0, 'G12': 6500.0, 'mu12': 0.06, 'd': 0.42, 'dens': 0.0016}
str_ang = [0, 45, -45, 90]
str_mat = [{'name': 'AGP3705H', 'E1': 77000.0, 'E2': 75000.0, 'G12': 6500.0, 'mu12': 0.06, 'd': 0.42, 'dens': 0.0016}, {'name': 'AGP3705H', 'E1': 77000.0, 'E2': 75000.0, 'G12': 6500.0, 'mu12': 0.06, 'd': 0.42, 'dens': 0.0016}, {'name': 'AGP3705H', 'E1': 77000.0, 'E2': 75000.0, 'G12': 6500.0, 'mu12': 0.06, 'd': 0.42, 'dens': 0.0016}, {'name': 'AGP3705H', 'E1': 77000.0, 'E2': 75000.0, 'G12': 6500.0, 'mu12': 0.06, 'd': 0.42, 'dens': 0.0016}]
dist_P = [380.0, 340.48, 246.23999999999995, 133.75999999999996, 39.51999999999995, 0.0]
dist = [0.0, 0.3745307099674787, 0.7490614199349575, 1.123592129902436, 1.498122839869915, 1.8726535498373935]
stp_dist = [1, 0.8, 0.9, 0.75, 0.8, 0.9, 1]






def dir_defination ():
    cur_dir = os.getcwd() + os.sep
    os.chdir(cur_dir)


def part_generation (radius):

    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
        0.0, 0.0), point1=(radius, 0.0))

    mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=
        DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['Part-1'].BaseShell(sketch=
        mdb.models['Model-1'].sketches['__profile__'])
    del mdb.models['Model-1'].sketches['__profile__']


def partition_generation(radius):
    mdb.models['Model-1'].ConstrainedSketch(gridSpacing=7.05, name='__profile__', 
        sheetSize=282.06, transform=
        mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
        sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[0], 
        sketchPlaneSide=SIDE1, 
        sketchUpEdge=mdb.models['Model-1'].parts['Part-1'].edges[0], 
        sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
    mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
        COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, radius), point2=(
        0.0, -radius))
    mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
        False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[3])
    mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
        addUndoState=False, entity1=
        mdb.models['Model-1'].sketches['__profile__'].geometry[2], entity2=
        mdb.models['Model-1'].sketches['__profile__'].geometry[3])
    mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
        addUndoState=False, entity1=
        mdb.models['Model-1'].sketches['__profile__'].vertices[2], entity2=
        mdb.models['Model-1'].sketches['__profile__'].geometry[2])
    mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
        addUndoState=False, entity1=
        mdb.models['Model-1'].sketches['__profile__'].vertices[3], entity2=
        mdb.models['Model-1'].sketches['__profile__'].geometry[2])
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-radius, 0.0), point2=
        (radius, 0.0))
    mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
        addUndoState=False, entity=
        mdb.models['Model-1'].sketches['__profile__'].geometry[4])
    mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
        addUndoState=False, entity1=
        mdb.models['Model-1'].sketches['__profile__'].geometry[2], entity2=
        mdb.models['Model-1'].sketches['__profile__'].geometry[4])
    mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
        addUndoState=False, entity1=
        mdb.models['Model-1'].sketches['__profile__'].vertices[4], entity2=
        mdb.models['Model-1'].sketches['__profile__'].geometry[2])
    mdb.models['Model-1'].parts['Part-1'].PartitionFaceBySketch(faces=
        mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
        ), ), sketch=mdb.models['Model-1'].sketches['__profile__'], sketchUpEdge=
        mdb.models['Model-1'].parts['Part-1'].edges[0])
    del mdb.models['Model-1'].sketches['__profile__']


def set_and_surf_generation():

    mdb.models['Model-1'].parts['Part-1'].DatumCsysByThreePoints(coordSysType=
        CYLINDRICAL, name='Cyl_C_Sys', origin=
        mdb.models['Model-1'].parts['Part-1'].vertices[0], point1=
        mdb.models['Model-1'].parts['Part-1'].InterestingPoint(
        mdb.models['Model-1'].parts['Part-1'].edges[3], MIDDLE), point2=
        mdb.models['Model-1'].parts['Part-1'].InterestingPoint(
        mdb.models['Model-1'].parts['Part-1'].edges[0], MIDDLE))
    mdb.models['Model-1'].parts['Part-1'].Surface(name='Surf_pressure', side1Faces=
        mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#f ]', 
        ), ))
    mdb.models['Model-1'].parts['Part-1'].Set(faces=
        mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#f ]', 
        ), ), name='material')
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#d2 ]', 
        ), ), name='Boundary')
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#2d ]', 
        ), ), name='Guide_Lines')


def material_generation(mat):
    mdb.models['Model-1'].Material(name=mat['name'])
    mdb.models['Model-1'].materials[mat['name']].Density(table=((mat['dens'], ), ))
    mdb.models['Model-1'].materials[mat['name']].Elastic(table=((mat['E1'], mat['E2'], 
        mat['mu12'], mat['G12'], mat['G12'], mat['G12']), ), type=LAMINA)


def layout_generation(str_ang, str_mat):
    mdb.models['Model-1'].parts['Part-1'].CompositeLayup(description='', 
        elementType=SHELL, name='CompositeLayup-1', offsetType=MIDDLE_SURFACE, 
        symmetric=False, thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['Part-1'].compositeLayups['CompositeLayup-1'].Section(
        integrationRule=SIMPSON, poissonDefinition=DEFAULT, preIntegrate=OFF, 
        temperature=GRADIENT, thicknessType=UNIFORM, useDensity=OFF)
    mdb.models['Model-1'].parts['Part-1'].compositeLayups['CompositeLayup-1'].ReferenceOrientation(
        additionalRotationType=ROTATION_NONE, angle=0.0, axis=AXIS_3, fieldName='', 
        localCsys=None, orientationType=GLOBAL)


    mdb.models['Model-1'].parts['Part-1'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material=str_mat[0]['name'], numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=str_ang[0], plyName='Ply-1', region=
        mdb.models['Model-1'].parts['Part-1'].sets['material'], suppressed=False, 
        thickness=str_mat[0]['d'], thicknessType=SPECIFY_THICKNESS)

    mdb.models['Model-1'].parts['Part-1'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material=str_mat[1]['name'], numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=str_ang[1], plyName='Ply-2', region=
        mdb.models['Model-1'].parts['Part-1'].sets['material'], suppressed=False, 
        thickness=str_mat[1]['d'], thicknessType=SPECIFY_THICKNESS)

    mdb.models['Model-1'].parts['Part-1'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material=str_mat[2]['name'], numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=str_ang[2], plyName='Ply-3', region=
        mdb.models['Model-1'].parts['Part-1'].sets['material'], suppressed=False, 
        thickness=str_mat[2]['d'], thicknessType=SPECIFY_THICKNESS)

    mdb.models['Model-1'].parts['Part-1'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material=str_mat[3]['name'], numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=str_ang[3], plyName='Ply-4', region=
        mdb.models['Model-1'].parts['Part-1'].sets['material'], suppressed=False, 
        thickness=str_mat[3]['d'], thicknessType=SPECIFY_THICKNESS)

    mdb.models['Model-1'].parts['Part-1'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material=str_mat[3]['name'], numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=str_ang[3], plyName='Ply-5', region=
        mdb.models['Model-1'].parts['Part-1'].sets['material'], suppressed=False, 
        thickness=str_mat[3]['d'], thicknessType=SPECIFY_THICKNESS)

    mdb.models['Model-1'].parts['Part-1'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material=str_mat[2]['name'], numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=str_ang[2], plyName='Ply-6', region=
        mdb.models['Model-1'].parts['Part-1'].sets['material'], suppressed=False, 
        thickness=str_mat[2]['d'], thicknessType=SPECIFY_THICKNESS)

    mdb.models['Model-1'].parts['Part-1'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material=str_mat[1]['name'], numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=str_ang[1], plyName='Ply-7', region=
        mdb.models['Model-1'].parts['Part-1'].sets['material'], suppressed=False, 
        thickness=str_mat[1]['d'], thicknessType=SPECIFY_THICKNESS)

    mdb.models['Model-1'].parts['Part-1'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material=str_mat[0]['name'], numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=str_ang[0], plyName='Ply-8', region=
        mdb.models['Model-1'].parts['Part-1'].sets['material'], suppressed=False, 
        thickness=str_mat[0]['d'], thicknessType=SPECIFY_THICKNESS)


def assembly_generation():
    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='Part-1-1', 
        part=mdb.models['Model-1'].parts['Part-1'])


def step_generation():
    mdb.models['Model-1'].StaticStep(name='Step-1', nlgeom=ON, previous='Initial')
    mdb.models['Model-1'].StaticStep(name='Step-2', previous='Step-1')
    mdb.models['Model-1'].StaticStep(name='Step-3', previous='Step-2')
    mdb.models['Model-1'].StaticStep(name='Step-4', previous='Step-3')
    mdb.models['Model-1'].StaticStep(name='Step-5', previous='Step-4')
    mdb.models['Model-1'].StaticStep(name='Step-6', previous='Step-5')
    mdb.models['Model-1'].StaticStep(name='Step-7', previous='Step-6')


def bc_and_loading_generation(dist, PD, stp_dist):

    mdb.models['Model-1'].PinnedBC(createStepName='Step-1', localCsys=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].datums[3], name=
        'BC-1', region=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].sets['Boundary'])
    mdb.models['Model-1'].MappedField(description='', fieldDataType=SCALAR, 
        gridPointData={'0':(
        (0, 0.0, 45.0, 90.0, 135.0, 180.0, 225.0, 270.0, 315.0), 
        (dist[1], PD[0], PD[0], PD[0], PD[0], PD[0], PD[0], PD[0], PD[0]), 
        (dist[1], PD[1], PD[1], PD[1], PD[1], PD[1], PD[1], PD[1], PD[1]), 
        (dist[2], PD[2], PD[2], PD[2], PD[2], PD[2], PD[2], PD[2], PD[2]), 
        (dist[3], PD[3], PD[3], PD[3], PD[3], PD[3], PD[3], PD[3], PD[3]), 
        (dist[4], PD[4], PD[4], PD[4], PD[4], PD[4], PD[4], PD[4], PD[4]), 
        (dist[5], PD[5], PD[5], PD[5], PD[5], PD[5], PD[5], PD[5], PD[5]), 
        (5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), 
        (15.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), 
        (50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))}, localCsys=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].datums[3], name=
        'Pressure_Field', partLevelData=False, pointDataFormat=GRID, regionType=
        POINT)

    mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='Step-1', 
        distributionType=UNIFORM, field='', magnitude=stp_dist[0], name='Load-1', region=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].surfaces['Surf_pressure'])
    mdb.models['Model-1'].loads['Load-1'].setValues(distributionType=FIELD, field=
        'Pressure_Field')
    mdb.models['Model-1'].loads['Load-1'].setValuesInStep(magnitude=stp_dist[1], stepName=
        'Step-2')
    mdb.models['Model-1'].loads['Load-1'].setValuesInStep(magnitude=stp_dist[2], stepName=
        'Step-3')
    mdb.models['Model-1'].loads['Load-1'].setValuesInStep(magnitude=stp_dist[3], stepName=
        'Step-4')
    mdb.models['Model-1'].loads['Load-1'].setValuesInStep(magnitude=stp_dist[4], stepName=
        'Step-5')
    mdb.models['Model-1'].loads['Load-1'].setValuesInStep(magnitude=stp_dist[5], stepName=
        'Step-6')
    mdb.models['Model-1'].loads['Load-1'].setValuesInStep(magnitude=stp_dist[6], stepName=
        'Step-7')


def mesh_generation(radius, dist):
    
    bd_size = radius*2*3.14/100         #boundary mesh size
    gl_size_max = radius/10
    gl_size_min = dist[-1]



    mdb.models['Model-1'].rootAssembly.seedEdgeBySize(constraint=FINER, edges=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
        ('[#d2 ]', ), ), size=bd_size)
    mdb.models['Model-1'].rootAssembly.seedEdgeByBias(biasMethod=SINGLE, 
        constraint=FINER, end1Edges=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
        ('[#28 ]', ), ), end2Edges=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
        ('[#5 ]', ), ), maxSize=gl_size_max, minSize=gl_size_min)
    mdb.models['Model-1'].rootAssembly.setMeshControls(regions=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
        ('[#f ]', ), ), technique=SWEEP)
    mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], ))


def job_generation():

    mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
        explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
        multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE, 
        numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
        ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)



from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *


import os



dir_defination ()
part_generation (radius)
partition_generation(radius)
set_and_surf_generation()
material_generation(mat1)
material_generation(mat2)
assembly_generation()
layout_generation(str_ang, str_mat)
step_generation()
bc_and_loading_generation(dist, dist_P, stp_dist)
mesh_generation(radius, dist)
job_generation()