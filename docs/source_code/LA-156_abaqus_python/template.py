#This is template to insert here a variables dicts


def Generate_part(dict_variables_for_part_bar, dict_variables_for_part_rib):
    '''
    *******************************
                PART
    *******************************
    dict_variables_for_part_bar = {'back_side', 'r_bar', 'l_bar', 'front_side'}
    dict_variables_for_part_rib = {'rib_1s', 'rib_1f', 'rib_2s', 'rib_2f', 'rib_3s', 'rib_3f', 'rib_4s', 'rib_4f', 'rib_5s', 'rib_5f'}
    '''
    dvpb = dict_variables_for_part_bar
    dvpr = dict_variables_for_part_rib

    #   Import catV5 model
    mdb.openCatia(fileName=
        'E:/WorkSpace/#Ongoing_projects/abaqus_wing_python_optymmization/Wing_surf/Master_Geom_surf.CATPart'
        , topology=SOLID, useServer=True)
    #Creating model
    mdb.models['Model-1'].PartFromGeometryFile(combine=False, dimensionality=
        THREE_D, geometryFile=mdb.acis, name='Master_Geom_surf', scale=1.0, type=
        DEFORMABLE_BODY)


    # Model processing. Prepearing to creating a set for BC

    ## Creating YZ Plane
    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPlaneByPrincipalPlane(
        offset=0.0, principalPlane=YZPLANE)

    ## Points sides
    ### Bar and sides points 
    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[1], parameter=dvpb['back_side'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Base 5%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[1], parameter=dvpb['r_bar'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Base 65%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[1], parameter=dvpb['l_bar'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Base 75%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[1], parameter=dvpb['front_side'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Base 95%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[3], parameter=dvpb['back_side'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='End 5%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[3], parameter=dvpb['r_bar'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='End 65%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[3], parameter=dvpb['l_bar'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='End 75%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[3], parameter=dvpb['front_side'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='End 95%')

    # Points ribs
    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[0], parameter=dvpr['rib_1s'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Rib 6,5%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[0], parameter=dvpr['rib_1f'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Rib 8%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[0], parameter=dvpr['rib_2s'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Rib 26,5%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[0], parameter=dvpr['rib_2f'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Rib 28%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[0], parameter=dvpr['rib_3s'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Rib 47%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[0], parameter=dvpr['rib_3f'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Rib 48,5%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[0], parameter=dvpr['rib_4s'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Rib 63,5%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[0], parameter=dvpr['rib_4f'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Rib 65%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[0], parameter=dvpr['rib_5s'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Rib 90%')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPointByEdgeParam(edge=
        mdb.models['Model-1'].parts['Master_Geom_surf'].edges[0], parameter=dvpr['rib_5f'])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum pt-1', toName='Rib 91,5%')


    ## Creating planes for ribs
    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPlaneByOffset(plane=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[2], point=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[11])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum plane-2', toName='Plane rib 1s')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPlaneByOffset(plane=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[2], point=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[12])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum plane-2', toName='Plane rib 1f')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPlaneByOffset(plane=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[2], point=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[13])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum plane-2', toName='Plane rib 2s')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPlaneByOffset(plane=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[2], point=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[14])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum plane-2', toName='Plane rib 2f')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPlaneByOffset(plane=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[2], point=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[15])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum plane-2', toName='Plane rib 3s')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPlaneByOffset(plane=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[2], point=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[16])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum plane-2', toName='Plane rib 3f')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPlaneByOffset(plane=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[2], point=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[17])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum plane-2', toName='Plane rib 4s')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPlaneByOffset(plane=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[2], point=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[18])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum plane-2', toName='Plane rib 4f')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPlaneByOffset(plane=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[2], point=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[19])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum plane-2', toName='Plane rib 5s')

    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumPlaneByOffset(plane=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[2], point=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[20])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Datum plane-2', toName='Plane rib 5f')



    ## Partition for sides
    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByShortestPath(
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#1 ]', ), ), point1=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[3], point2=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[7])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Back side')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByShortestPath(
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#3 ]', ), ), point1=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[4], point2=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[8])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Long_right')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByShortestPath(
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#7 ]', ), ), point1=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[5], point2=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[9])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Long_left')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByShortestPath(
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#f ]', ), ), point1=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[6], point2=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[10])
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Front side')

    #Partition for sides
    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByDatumPlane(
        datumPlane=mdb.models['Model-1'].parts['Master_Geom_surf'].datums[21], 
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#1f ]', ), ))
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Rib 1s')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByDatumPlane(
        datumPlane=mdb.models['Model-1'].parts['Master_Geom_surf'].datums[22], 
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#3ff ]', ), ))
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Rib 1f')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByDatumPlane(
        datumPlane=mdb.models['Model-1'].parts['Master_Geom_surf'].datums[23], 
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#7fff ]', ), ))
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Rib 2s')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByDatumPlane(
        datumPlane=mdb.models['Model-1'].parts['Master_Geom_surf'].datums[24], 
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#fffff ]', ), ))
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Rib 2f')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByDatumPlane(
        datumPlane=mdb.models['Model-1'].parts['Master_Geom_surf'].datums[25], 
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#1ffffff ]', ), ))
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Rib 3s')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByDatumPlane(
        datumPlane=mdb.models['Model-1'].parts['Master_Geom_surf'].datums[26], 
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#3fffffff ]', ), ))
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Rib 3f')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByDatumPlane(
        datumPlane=mdb.models['Model-1'].parts['Master_Geom_surf'].datums[27], 
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#ffffffff #7 ]', ), ))
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Rib 4s')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByDatumPlane(
        datumPlane=mdb.models['Model-1'].parts['Master_Geom_surf'].datums[28], 
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#ffffffff #ff ]', ), ))
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Rib 4f')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByDatumPlane(
        datumPlane=mdb.models['Model-1'].parts['Master_Geom_surf'].datums[29], 
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#ffffffff #1fff ]', ), ))
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Rib 5s')

    mdb.models['Model-1'].parts['Master_Geom_surf'].PartitionFaceByDatumPlane(
        datumPlane=mdb.models['Model-1'].parts['Master_Geom_surf'].datums[30], 
        faces=
        mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask((
        '[#ffffffff #3ffff ]', ), ))
    mdb.models['Model-1'].parts['Master_Geom_surf'].features.changeKey(fromName=
        'Partition face-1', toName='Rib 5f')


def Generate_material (dict_variables_for_layout_thickness, dict_variables_for_layout_orientation):
    '''
    *******************************
    Generation a material property
    *******************************

    dict_variables_for_material = {'E1', 'E2', 'mu', 'G1', 'G2', 'G3', 'F1t', 'F1c', 'F2t', 'F2c', 'F12'}
    dict_variables_for_layout_thickness = {'Ply1', 'Ply2', 'Ply3', 'Ply4', 'Ply5', 'Ply6', 'Ply7', 'Ply8'}
    dict_variables_for_layout_orientation = {'Ply1', 'Ply2', 'Ply3', 'Ply4', 'Ply5', 'Ply6', 'Ply7', 'Ply8'}

    '''
    mat = dict_variables_for_material
    fil = dict_variables_for_material_filler
    thic = dict_variables_for_layout_thickness
    orient = dict_variables_for_layout_orientation

    # Creating a CSys
    mdb.models['Model-1'].parts['Master_Geom_surf'].DatumCsysByThreePoints(
        coordSysType=CARTESIAN, name='Ply CSys', origin=
        mdb.models['Model-1'].parts['Master_Geom_surf'].vertices[58], point1=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[4], point2=
        mdb.models['Model-1'].parts['Master_Geom_surf'].vertices[57])

    # Material
    mdb.models['Model-1'].Material(name='Carbon_fiber')
    mdb.models['Model-1'].materials['Carbon_fiber'].Elastic(table=((mat['E1'], 
        mat['E2'], mat['mu'], mat['G12'], mat['G12'], mat['G12']), ), type=LAMINA)
    mdb.models['Model-1'].materials['Carbon_fiber'].elastic.FailStress(table=((
        mat['F1t'], mat['F1c'], mat['F2t'], mat['F2c'], mat['F12'], 0.0, 0.0), ))
    ## material filler
    mdb.models['Model-1'].Material(name='ROCHACELL')
    mdb.models['Model-1'].materials['ROCHACELL'].Elastic(table=((fil['E1'], 
        fil['E2'], fil['mu'], fil['G12'], fil['G12'], fil['G12']), ), type=LAMINA)
    mdb.models['Model-1'].materials['ROCHACELL'].elastic.FailStress(table=((
        fil['F1t'], fil['F1c'], fil['F2t'], fil['F2c'], fil['F12'], 0.0, 0.0), ))

    # Generation Layup
    mdb.models['Model-1'].parts['Master_Geom_surf'].CompositeLayup(description=
        '8 Layers allow to set up a [0, 90 +-fi] structure', elementType=SHELL, 
        name='CompositeLayup', offsetType=BOTTOM_SURFACE, symmetric=False, 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['Master_Geom_surf'].compositeLayups['CompositeLayup'].Section(
        integrationRule=SIMPSON, poissonDefinition=DEFAULT, preIntegrate=OFF, 
        temperature=GRADIENT, thicknessType=UNIFORM, useDensity=OFF)
    mdb.models['Model-1'].parts['Master_Geom_surf'].compositeLayups['CompositeLayup'].ReferenceOrientation(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, fieldName='', localCsys=
        mdb.models['Model-1'].parts['Master_Geom_surf'].datums[45], 
        orientationType=SYSTEM)


    # Ply property
    mdb.models['Model-1'].parts['Master_Geom_surf'].compositeLayups['CompositeLayup'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon_fiber', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=orient['Ply1'], plyName='Ply-1', region=Region(
        faces=mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask(
        mask=('[#ffffffff #7fffff ]', ), )), suppressed=False, thickness=thic['Ply1'], 
        thicknessType=SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Master_Geom_surf'].compositeLayups['CompositeLayup'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon_fiber', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=orient['Ply2'], plyName='Ply-2', region=Region(
        faces=mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask(
        mask=('[#ffffffff #7fffff ]', ), )), suppressed=False, thickness=thic['Ply2'], 
        thicknessType=SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Master_Geom_surf'].compositeLayups['CompositeLayup'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon_fiber', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=orient['Ply3'], plyName='Ply-3', region=Region(
        faces=mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask(
        mask=('[#ffffffff #7fffff ]', ), )), suppressed=False, thickness=thic['Ply3'], 
        thicknessType=SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Master_Geom_surf'].compositeLayups['CompositeLayup'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon_fiber', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=orient['Ply4'], plyName='Ply-4', region=Region(
        faces=mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask(
        mask=('[#ffffffff #7fffff ]', ), )), suppressed=False, thickness=thic['Ply4'], 
        thicknessType=SPECIFY_THICKNESS)

    mdb.models['Model-1'].parts['Master_Geom_surf'].compositeLayups['CompositeLayup'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon_fiber', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=orient['Filler'], plyName='Filler', region=Region(
        faces=mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask(
        mask=('[#ffffffff #7fffff ]', ), )), suppressed=False, thickness=thic['Filler'], 
        thicknessType=SPECIFY_THICKNESS)

    mdb.models['Model-1'].parts['Master_Geom_surf'].compositeLayups['CompositeLayup'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon_fiber', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=orient['Ply5'], plyName='Ply-5', region=Region(
        faces=mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask(
        mask=('[#ffffffff #7fffff ]', ), )), suppressed=False, thickness=thic['Ply5'], 
        thicknessType=SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Master_Geom_surf'].compositeLayups['CompositeLayup'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon_fiber', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=orient['Ply6'], plyName='Ply-6', region=Region(
        faces=mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask(
        mask=('[#ffffffff #7fffff ]', ), )), suppressed=False, thickness=thic['Ply6'], 
        thicknessType=SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Master_Geom_surf'].compositeLayups['CompositeLayup'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon_fiber', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=orient['Ply7'], plyName='Ply-7', region=Region(
        faces=mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask(
        mask=('[#ffffffff #7fffff ]', ), )), suppressed=False, thickness=thic['Ply7'], 
        thicknessType=SPECIFY_THICKNESS)
    mdb.models['Model-1'].parts['Master_Geom_surf'].compositeLayups['CompositeLayup'].CompositePly(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, material='Carbon_fiber', numIntPoints=3, orientationType=
        SPECIFY_ORIENT, orientationValue=orient['Ply8'], plyName='Ply-8', region=Region(
        faces=mdb.models['Model-1'].parts['Master_Geom_surf'].faces.getSequenceFromMask(
        mask=('[#ffffffff #7fffff ]', ), )), suppressed=False, thickness=thic['Ply8'], 
        thicknessType=SPECIFY_THICKNESS)


def Generate_assembly ():
    '''
    *******************************
            ASSEMBLY
    *******************************
    '''

    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name=
        'Master_Geom_surf-1', part=mdb.models['Model-1'].parts['Master_Geom_surf'])


def Generate_step ():
    '''
    *******************************
            STEP
    *******************************
    '''

    mdb.models['Model-1'].StaticStep(name='Air_pressure_Applying', previous=
        'Initial')

    #Field Output Request
    mdb.models['Model-1'].FieldOutputRequest(createStepName='Air_pressure_Applying'
        , layupLocationMethod=SPECIFIED, layupNames=(
        'Master_Geom_surf-1.CompositeLayup', ), name='Field-Output-2', 
        outputAtPlyBottom=False, outputAtPlyMid=True, outputAtPlyTop=False, rebar=
        EXCLUDE, variables=('S', 'E', 'CFAILURE'))


def Generate_load_and_bc (dict_variables_for_load):
    '''
    *******************************
            LOAD & BC
    *******************************
    dict_variables_for_load = {'pressure', 'u1', 'u2', 'u3', 'r1', 'r2', 'r3'}
    '''

    pressure = dict_variables_for_load['pressure']
    bc = dict_variables_for_load

    #Surface
    mdb.models['Model-1'].rootAssembly.Surface(name='Air_Pressure_surf', 
        side1Faces=
        mdb.models['Model-1'].rootAssembly.instances['Master_Geom_surf-1'].faces.getSequenceFromMask(
        ('[#ffffffff #7fffff ]', ), ))

    # Set
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['Master_Geom_surf-1'].edges.getSequenceFromMask(
        ('[#0:3 #8811000 ]', ), ), faces=
        mdb.models['Model-1'].rootAssembly.instances['Master_Geom_surf-1'].faces.getSequenceFromMask(
        ('[#ebfafebf #56bfaf ]', ), ), name='BC_Set')

    # Load (here is presuure variable)
    mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName=
        'Air_pressure_Applying', distributionType=UNIFORM, field='', magnitude=
        pressure, name='Load-1', region=
        mdb.models['Model-1'].rootAssembly.surfaces['Air_Pressure_surf'])

    # BC (here is all displacement can be variable)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
        'Air_pressure_Applying', distributionType=UNIFORM, fieldName='', fixed=OFF, 
        localCsys=
        mdb.models['Model-1'].rootAssembly.instances['Master_Geom_surf-1'].datums[45]
        , name='BC-1', region=mdb.models['Model-1'].rootAssembly.sets['BC_Set'], 
        u1=bc['u1'], u2=bc['u2'], u3=bc['u3'], ur1=bc['r1'], ur2=bc['r2'], ur3=bc['r3'])


def Generate_mesh (Mesh):
    '''
    *******************************
            MESH
    *******************************
    '''

    # Seed (size variable)
    mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
        minSizeFactor=0.1, regions=(
        mdb.models['Model-1'].rootAssembly.instances['Master_Geom_surf-1'], ), 
        size=Mesh['size'])

    # Mesh genetarion
    mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
        mdb.models['Model-1'].rootAssembly.instances['Master_Geom_surf-1'], ))


def Generate_job ():
    '''
    *******************************
            JOB
    *******************************
    '''

    # Job generation
    mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
        explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
        multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE, 
        numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
        ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)

    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)

    # Massage
    mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
        'clientHost': 'BAL-AE-DESKTOP', 'handle': 0, 'jobName': 'Job-1'})
    mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
        'message': 'NO BIAXIAL STRESS LIMIT GIVEN.  DEFAULT F12 USED.', 
        'jobName': 'Job-1'})
    mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
        'file': 'e:\\WorkSpace\\#Ongoing_projects\\abaqus_wing_python_optymmization\\Wing_surf\\Job-1.odb', 
        'jobName': 'Job-1'})
    mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
        'message': 'Analysis phase complete', 'jobName': 'Job-1'})
    mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE, 
        'clientHost': 'BAL-AE-DESKTOP', 'handle': 9100, 'jobName': 'Job-1'})
    mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
        'jobName': 'Job-1'})
    mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
        'frame': 0, 'jobName': 'Job-1'})
    mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
        'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
        'jobName': 'Job-1', 'severe': 0, 'iterations': 0, 'phase': STANDARD_PHASE, 
        'equilibrium': 0})
    mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
        'jobName': 'Job-1', 'memory': 49.0})
    mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
        'frame': 1, 'jobName': 'Job-1'})
    mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1, 
        'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 'step': 1, 
        'jobName': 'Job-1', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
        'equilibrium': 1})
    mdb.jobs['Job-1']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
        'jobName': 'Job-1'})
    mdb.jobs['Job-1']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
        'message': 'Analysis phase complete', 'jobName': 'Job-1'})
    mdb.jobs['Job-1']._Message(JOB_COMPLETED, {'time': 'Thu May 17 14:33:02 2018', 
        'jobName': 'Job-1'})




def Generate_whole_proc ():
    Generate_part(dict_variables_for_part_bar, dict_variables_for_part_rib)
    Generate_material(dict_variables_for_layout_thickness, dict_variables_for_layout_orientation)
    Generate_assembly()
    Generate_step()
    Generate_load_and_bc(dict_variables_for_load)
    Generate_mesh(Mesh)
    Generate_job()




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

    Generate_whole_proc()