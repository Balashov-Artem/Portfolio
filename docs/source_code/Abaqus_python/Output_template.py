#Output_template.py


def Generate_viewport_and_setting():
    session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=209.625, 
        height=132.017364501953)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].maximize()

    executeOnCaeStartup()
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    execfile('Script.py', __main__.__dict__)

    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)

    o3 = session.openOdb(name='Job-Main.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)

def Generate_plot():
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='TSAIH', outputPosition=INTEGRATION_POINT)

def Generate_png():

    #file_path = 'C:/Users/Balashov Artem/Desktop/Abaqus_Python/'
    file_path = ''
    file_name = 'Print' + str(n)
    name = file_path + file_name

    session.printToFile(
        fileName=name, 
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))

def Generate_report():
    odb = session.odbs['Job-Main.odb']
    nf = NumberFormat(numDigits=3, precision=0, format=ENGINEERING)
    session.fieldReportOptions.setValues(printXYData=OFF, printTotal=OFF, 
        numberFormat=nf)
    session.writeFieldReport(
        fileName='abaqus.rpt', 
        append=ON, sortItem='Element Label', odb=odb, step=0, frame=1, 
        outputPosition=INTEGRATION_POINT, variable=(('TSAIH', INTEGRATION_POINT), 
        ))

def Generate_Output():
    Generate_viewport_and_setting()
    Generate_plot()
    Generate_png()
    Generate_report()

if __name__ == '__main__':
    from abaqus import *
    from abaqusConstants import *
    from caeModules import *
    from driverUtils import executeOnCaeStartup
    Generate_Output()