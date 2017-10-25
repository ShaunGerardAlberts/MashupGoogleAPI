import petl as etl

def createTableFromCSV(csvFile):
    return etl.fromcsv(csvFile)

def createTableFromXML(xmlFile):
    return etl.fromxml(xmlFile, "store",{"Name":"Name", "Suburb":"Suburb", "Lat":"Lat", "Lon":"Lon"})

def joinTables(tableOne, tableTwo, key):
    return etl.join(tableOne, tableTwo, key=key)
    #mergeTable = etl.join(tableOne, tableTwo, key=key)
    #return etl.cut(mergeTable, )

if __name__ == "__main__":
    #file locations
    xmlFile = './resources/locations.xml'
    csvFile = "./resources/stores.csv"

    #create the tables using the supplied files
    locTable = createTableFromXML(xmlFile)
    # print(locTable)
    storesTable = createTableFromCSV(csvFile)
    # print(storesTable)

    #join two tables
    locationStores = joinTables(locTable, storesTable, "Name")
    # print(locationStores)

    #order table
    orderdColumns = etl.cut(locationStores, "Name", "Suburb", "Lat", "Lon", "ID", "State", "Postcode")

    #write joind and ordered table to file
    etl.tocsv(orderdColumns, "./resources/store_locations.csv")
