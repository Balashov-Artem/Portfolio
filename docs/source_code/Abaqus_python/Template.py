#Template.py

def Generate_part():
    #Plate gen
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(Dim['x0'], Dim['y0']), 
        point2=(Dim['x1'], Dim['y1']))
    mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Plate', type=
        DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['Plate'].BaseShell(sketch=
        mdb.models['Model-1'].sketches['__profile__'])
    del mdb.models['Model-1'].sketches['__profile__']

    #Datum System
    mdb.models['Model-1'].parts['Plate'].DatumCsysByThreePoints(coordSysType=
        CARTESIAN, name='Datum csys-1', origin=
        mdb.models['Model-1'].parts['Plate'].vertices[0], point1=
        mdb.models['Model-1'].parts['Plate'].InterestingPoint(
        mdb.models['Model-1'].parts['Plate'].edges[0], MIDDLE), point2=
        mdb.models['Model-1'].parts['Plate'].InterestingPoint(
        mdb.models['Model-1'].parts['Plate'].edges[3], MIDDLE))

def Generate_material():
    #Material gen
    mdb.models['Model-1'].Material(name='Carbon')
    mdb.models['Model-1'].materials['Carbon'].Elastic(table=((Mat['E1'], Mat['E2'], 
        Mat['mu'], Mat['G12'], Mat['G12'], Mat['G12']), ), type=LAMINA)
    mdb.models['Model-1'].materials['Carbon'].elastic.FailStress(table=((Mat['F1t'], 
        Mat['F1c'], Mat['F2t'], Mat['F2c'], Mat['F12'], 0.0, 0.0), ))

def Generate_Composite_Layup():
    #CM Layout
    mdb.models['Model-1'].parts['Plate'].CompositeLayup(description='', 
        elementType=SHELL, name='CompositeLayup-1', offsetType=MIDDLE_SURFACE, 
        symmetric=False, thicknessAssignment=FROM_SECTION)
    #Surface for CM
    mdb.models['Model-1'].parts['Plate'].compositeLayups['CompositeLayup-1'].Section(
        integrationRule=SIMPSON, poissonDefinition=DEFAULT, preIntegrate=OFF, 
        temperature=GRADIENT, thicknessType=UNIFORM, useDensity=OFF)
    #CM direction axis
    mdb.models['Model-1'].parts['Plate'].compositeLayups['CompositeLayup-1'].ReferenceOrientation(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, fieldName='', localCsys=
        mdb.models['Model-1'].parts['Plate'].datums[2], orientationType=SYSTEM)


    #Plys paremeters
    mdb.models['Model-1'].parts['Plate'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=Pl_or['Ply1'], plyName='Ply1', region=Region(
        faces=mdb.models['Model-1'].parts['Plate'].faces.getSequenceFromMask(mask=(
        '[#1 ]', ), )), suppressed=False, thickness=Pl_th['Ply1'], thicknessType=
        SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Plate'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=Pl_or['Ply2'], plyName='Ply2', region=Region(
        faces=mdb.models['Model-1'].parts['Plate'].faces.getSequenceFromMask(mask=(
        '[#1 ]', ), )), suppressed=False, thickness=Pl_th['Ply2'], thicknessType=
        SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Plate'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=Pl_or['Ply3'], plyName='Ply3', region=Region(
        faces=mdb.models['Model-1'].parts['Plate'].faces.getSequenceFromMask(mask=(
        '[#1 ]', ), )), suppressed=False, thickness=Pl_th['Ply3'], thicknessType=
        SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Plate'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=Pl_or['Ply4'], plyName='Ply4', region=Region(
        faces=mdb.models['Model-1'].parts['Plate'].faces.getSequenceFromMask(mask=(
        '[#1 ]', ), )), suppressed=False, thickness=Pl_th['Ply4'], thicknessType=
        SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Plate'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=Pl_or['Ply5'], plyName='Ply5', region=Region(
        faces=mdb.models['Model-1'].parts['Plate'].faces.getSequenceFromMask(mask=(
        '[#1 ]', ), )), suppressed=False, thickness=Pl_th['Ply5'], thicknessType=
        SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Plate'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=Pl_or['Ply6'], plyName='Ply6', region=Region(
        faces=mdb.models['Model-1'].parts['Plate'].faces.getSequenceFromMask(mask=(
        '[#1 ]', ), )), suppressed=False, thickness=Pl_th['Ply6'], thicknessType=
        SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Plate'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=Pl_or['Ply7'], plyName='Ply7', region=Region(
        faces=mdb.models['Model-1'].parts['Plate'].faces.getSequenceFromMask(mask=(
        '[#1 ]', ), )), suppressed=False, thickness=Pl_th['Ply7'], thicknessType=
        SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Plate'].compositeLayups['CompositeLayup-1'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=Pl_or['Ply8'], plyName='Ply8', region=Region(
        faces=mdb.models['Model-1'].parts['Plate'].faces.getSequenceFromMask(mask=(
        '[#1 ]', ), )), suppressed=False, thickness=Pl_th['Ply8'], thicknessType=
        SPECIFY_THICKNESS)

def Generate_Assembly():
    #Assembly gen
    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='Plate-1', 
        part=mdb.models['Model-1'].parts['Plate'])

def Generate_Step():
    #Step gen
    mdb.models['Model-1'].StaticStep(description='Pressure applying', name=
        'Step-General', previous='Initial')
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(
        layupLocationMethod=SPECIFIED, layupNames=('Plate-1.CompositeLayup-1', ), 
        outputAtPlyBottom=False, outputAtPlyMid=True, outputAtPlyTop=False, rebar=
        EXCLUDE, variables=('S', 'MISES', 'MISESMAX', 'CFAILURE'))

def Generate_Load_and_BC():

    #Set ans Surface gen, for BC and load
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['Plate-1'].edges.getSequenceFromMask(
        ('[#a ]', ), ), name='Set-BC')
    mdb.models['Model-1'].rootAssembly.Surface(name='Surf-Plate', side1Faces=
        mdb.models['Model-1'].rootAssembly.instances['Plate-1'].faces.getSequenceFromMask(
        ('[#1 ]', ), ))

    #BC def
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
        'Step-General', distributionType=UNIFORM, fieldName='', fixed=OFF, 
        localCsys=mdb.models['Model-1'].rootAssembly.instances['Plate-1'].datums[2]
        , name='BC-1', region=mdb.models['Model-1'].rootAssembly.sets['Set-BC'], 
        u1=BC['u1'], u2=BC['u2'], u3=BC['u3'], ur1=BC['r1'], ur2=BC['r2'], ur3=BC['r3'])

    #Load def
    mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='Step-General', 
        distributionType=UNIFORM, field='', magnitude=Pressure['Magnitude'], name='Load-1', region=
        mdb.models['Model-1'].rootAssembly.surfaces['Surf-Plate'])

def Generate_Mesh():
    #Mesh gen
    mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
        minSizeFactor=0.1, regions=(
        mdb.models['Model-1'].rootAssembly.instances['Plate-1'], ), size=Mesh['Size'])
    mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
        mdb.models['Model-1'].rootAssembly.instances['Plate-1'], ))

def Generate_Job():
    #Job definition
    mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
        explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
        multiprocessingMode=DEFAULT, name='Job-Main', nodalOutputPrecision=SINGLE, 
        numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
        ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
    mdb.jobs['Job-Main'].submit(consistencyChecking=OFF)


def Submit_proc():
    Generate_part()
    Generate_material()
    Generate_Composite_Layup()
    Generate_Assembly()
    Generate_Step()
    Generate_Load_and_BC()
    Generate_Mesh()
    Generate_Job()


if __name__ == '__main__':
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
    Submit_proc()