#there is template for output script. here is need it to insert 'n' - number of this iteration


def Generation_viewport_and_setting():
    #Viewport generation
    session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=141.98957824707, 
        height=123.528930664063)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].maximize()



    executeOnCaeStartup()
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    execfile('script.py', __main__.__dict__)

    p = mdb.models['Model-1'].parts['Master_Geom_surf']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].setValues(displayedObject=None)

    o1 = session.openOdb(
        name='e:/WorkSpace/#Ongoing_projects/abaqus_wing_python_optymmization/Wing_surf/Job-1.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)

def Orientation():
    # Rotating model
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5849.32, 
        farPlane=10633.3, width=3869.16, height=1848.39, cameraPosition=(4678.16, 
        -3109.37, -2766.4), cameraUpVector=(-0.579215, 0.274592, -0.767535), 
        cameraTarget=(-2199.24, 17.78, 41.9353))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6033.16, 
        farPlane=10449.5, width=3132.94, height=1496.68)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))

def Generation_plot():
    # Plot setting
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='TSAIH', outputPosition=INTEGRATION_POINT, )
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        deformationScaling=UNIFORM, uniformScaleFactor=1)

def Generation_tiff(n):
    file_path = 'e:/WorkSpace/#Ongoing_projects/abaqus_wing_python_optymmization/Wing_surf/'
    file_name = 'print'+ str(n) 
    name = file_path + file_name
    # Making a .tiff picture (for function replace frilename='..' + n, where n is number of iteration)
    session.printToFile(
        fileName=name, 
        format=TIFF, canvasObjects=(session.viewports['Viewport: 1'], ))

def Generation_rpt():
    odb = session.odbs['e:/WorkSpace/#Ongoing_projects/abaqus_wing_python_optymmization/Wing_surf/Job-1.odb']
    nf = NumberFormat(numDigits=3, precision=0, format=ENGINEERING)
    session.fieldReportOptions.setValues(printXYData=OFF, numberFormat=nf)
    session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
        sortItem='Element Label', odb=odb, step=0, frame=1, 
        outputPosition=INTEGRATION_POINT, variable=(('TSAIH', INTEGRATION_POINT), 
        ))



def Generation_Output():
    Generation_viewport_and_setting()
    Orientation()
    Generation_plot()
    Generation_tiff(n)
    Generation_rpt()

if __name__ == '__main__':
    from abaqus import *
    from abaqusConstants import *
    from caeModules import *
    from driverUtils import executeOnCaeStartup
    Generation_Output()