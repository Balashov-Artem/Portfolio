def dir_defination ():
    global cur_dir
    cur_dir = os.getcwd() + os.sep

    print('cur_dir:= ', cur_dir)
    os.chdir(cur_dir)



def viewport_gen ():
    session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=209.625, 
        height=132.017364501953)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].maximize()

    executeOnCaeStartup()
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)


def script_call ():
    script_name = cur_dir + 'plate.py'
    execfile(script_name, __main__.__dict__)


def model_call ():
    a = mdb.models['Model-1'].rootAssembly  
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)


def find_or_delay (path, name):
    list_dir = os.listdir(path)
    #print('waiting for ', name)
    #print('in ', list_dir)
    for i in range(150):
        list_dir = os.listdir(path)
        if name in list_dir:
            #time.sleep(1)
            break
        else:
            time.sleep(1)


def odb_call ():
    odb_name = cur_dir + 'Job-1.odb'
    o3 = session.openOdb(name=odb_name)

    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])


def print_normsize_pic (n, n_name):
    print_name_1 = cur_dir + 'picture_' + str(n_name) + '_' + str(n)
    session.printToFile(fileName=print_name_1, 
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))


def viewport_adjusting ():
    session.viewports['Viewport: 1'].view.setValues(nearPlane=277.827, 
        farPlane=288.214, width=20.2393, height=9.38968, viewOffsetX=0.266434, 
        viewOffsetY=0.177162)

    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
        'Max. Principal'), )


def print_resolt ():
    odb_name = cur_dir + 'Job-1.odb'
    odb = session.odbs[odb_name]
    session.fieldReportOptions.setValues(printXYData=OFF)
    session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
        sortItem='Element Label', odb=odb, step=6, frame=1, 
        outputPosition=INTEGRATION_POINT, variable=(('S', INTEGRATION_POINT, ((
        INVARIANT, 'Max. Principal'), )), ))


def print_zoomsize_pic (n, n_name):
    print_name_2 = cur_dir + 'picture_zoom_' + str(n_name) + '_' + str(n)
    session.printToFile(
        fileName=print_name_2, 
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))


def mdb_save ():
    plate_path_name = cur_dir + 'plate'
    mdb.saveAs(pathName=plate_path_name)




from abaqus import *
from abaqusConstants import *

from caeModules import *
from driverUtils import executeOnCaeStartup

import os
import time


dir_defination()
viewport_gen()
script_call()
model_call()
#find_or_delay(cur_dir, 'Job-1.odb')
odb_call()
print_normsize_pic(n, n_name)
viewport_adjusting()
print_resolt()
print_zoomsize_pic(n, n_name)
mdb_save()