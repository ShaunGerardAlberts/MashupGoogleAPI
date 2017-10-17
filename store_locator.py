from bottle import route, request, response, run
import petl as etl
import sys

_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = '*'

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
    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Content-type'] = _allow_headers

run(host='localhost', port=8080, debug=True)