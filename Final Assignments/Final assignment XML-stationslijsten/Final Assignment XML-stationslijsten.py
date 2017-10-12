import xmltodict
#help
def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

stationendict = processXML('stationslijst.xml')
stationen = stationendict['Stations']['Station']
OrderedDict = {}

print('dit zijn de codes en types van de {} stations:'.format(len(stationen)))
for station in stationen:
    print('{0:5}- {1:}'.format(station['Code'],station['Type']))

print('\nDit zijn alle staions met één of meer synoniemen:')
for station in stationen:
    if station['Synoniemen'] is not None:
        OrderedDict.update(station['Synoniemen'])
        print('{0:5}- {1:}'.format(station['Code'], OrderedDict))

print('\nDit is de lange naam van elk station:')
for station in stationen:
    print('{0:5}- {1:}'.format(station['Code'],station['Namen']['Lang']))
