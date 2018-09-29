from Code import myApp as myApp
from time import perf_counter

inputDict = dict()

recordMarkerStartText = 'Software Version'
recordMarkerEndText = 'XXX Laboratories'
tableMarkerStartText = 'Water Report'
tableMarkerEndText = 'Timed Event Table'
headerMarkerStartText = 'Software Version'
headerMarkerEndText = 'Water Report'
headerFieldsSelection = ['Sample Name','Sample Number','Instrument','Sample Amount']
tableFieldsSelection = ['Time','Component','Adj Amt','Area']
delimiter = ','

inputDict['recordMarkerStartText'] = recordMarkerStartText
inputDict['recordMarkerEndText'] = recordMarkerEndText
inputDict['tableMarkerStartText'] = tableMarkerStartText
inputDict['tableMarkerEndText'] = tableMarkerEndText
inputDict['headerMarkerStartText'] = headerMarkerStartText
inputDict['headerMarkerEndText'] = headerMarkerEndText
inputDict['headerFieldsSelection'] = headerFieldsSelection
inputDict['tableFieldsSelection'] = tableFieldsSelection
inputDict['delimiter'] = delimiter

#-----------------------xml parameters----------------------
tableHeader = []
fields = []
header = []

parentTag = 'TestOrder'
headerFields = ['TestOrder:Id','TestOrder:LastModificationActorId','TestOrder:Specimen','Detail:Value']
tableFields = ['TestOrder:TestOrderDate','TestOrder:Status','TestData:Id', 'TestResult:Id', 'ProcessOrder:Id']

inputDict['tableHeader'] = tableHeader
inputDict['fields'] = fields
inputDict['header'] = header
inputDict['parentTag'] = parentTag
inputDict['headerFields'] = headerFields
inputDict['tableFields'] = tableFields

#---------------csv----------------------
attr_list = [1,2,3,4,5,6]
inputDict['attr_list'] = attr_list
retval= True

fileName=r'C:\Users\user\Downloads\GC2.DAT'

retval = myApp.myApp.main(myApp.myApp(), funcName="TXT", fileName=fileName, funcInput=inputDict)

startTime = perf_counter()
fileName=r'C:\Users\Public\Documents\Python Scripts\MPX RUN 1 PL1 PH_2013_01_23_09_44_27.xml'
retval = myApp.myApp.main(myApp.myApp(),funcName="XML",fileName=fileName,funcInput=inputDict)
print("Retval is : {0}".format(retval))
endTime = perf_counter()
print('StartTime : ',startTime)
print('endTime : ',endTime)
print('TimeTaken : ',endTime - startTime)
print("Retval is : {0}".format(retval))

fileName=r'C:\Users\Public\Documents\Python ScriptsICP1.csv'
#retval = myApp.myApp.main(myApp.myApp(),funcName="CSV",fileName=fileName,funcInput=inputDict)
print("Retval is : {0}".format(retval))