from bottle import route, request, response, run
import petl as etl
import sys

storeLocationsTable = etl.fromcsv("./resources/store_locations.csv")
#print(storeLocationsTable)

@route('/hello')
def hello():
    return "Hello"

#http://localhost:8080/getlocation?postcode=5000
@route('/getlocation')
def get_location():
    setHeaders()
    postCode = request.query.postcode
    selectedRow = etl.select(storeLocationsTable, "{Postcode} == '" + postCode + "'") 

    #if 2 records are not returned it didn't find a result
    if (selectedRow.len() != 2):
        defaultPostCode = "2000"
        selectedRow = etl.select(storeLocationsTable, "{Postcode} == '" + defaultPostCode + "'") 

    name = selectedRow[1][0]
    lat = selectedRow[1][2]
    lon = selectedRow[1][3]
    storeData = {
        "name": name,
        "lat": lat,
        "lon": lon
    }
    return storeData

def setHeaders():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Content-type'] = '*'

run(host='localhost', port=8080, debug=True)