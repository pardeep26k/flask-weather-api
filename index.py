from flask import Flask
from shipment import Shipment
from weather import Weather

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


# Api Call to return shipment data by shipment ID
@app.route('/order/<order_id>')
def order_data(order_id):
    shipment_obj = Shipment()
    weather_obj = Weather()
    result = shipment_obj.search_by_shipment(order_id);
    response = weather_obj.get_weather(result)
    return response


# Api Call to return shipment data by Career
@app.route('/shipment/<career>')
def shipment_data(career):
    shipment_obj = Shipment()
    weather_obj = Weather()
    result = shipment_obj.search_by_career(career.lower());
    response = weather_obj.get_weather(result)
    return response
