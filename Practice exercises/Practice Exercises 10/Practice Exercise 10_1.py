import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

artikeldict = processXML('artikelen.xml')
artikelen = artikeldict['artikelen']['artikel']

for artikel in artikelen:
    print(artikel['naam'])