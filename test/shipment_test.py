import unittest
import json
from shipment import Shipment


class shipmentTest(unittest.TestCase):

    def setUp(self):
        self.shipment_obj = Shipment()

    def test_search_shipment_by_career(self):
        response = self.shipment_obj.search_by_career('fedex')
        self.assertEquals('fedex'.upper(),response[0][1])
        response = self.shipment_obj.search_by_career('test')
        self.assertEquals('Sorry no data available for career test', response['message'])


    def test_search_shipment_by_id(self):
        response = self.shipment_obj.search_by_shipment('TN12345678')
        self.assertEquals('DHL'.upper(),response[0][1])
        response = self.shipment_obj.search_by_shipment('test')
        self.assertEquals('Sorry your test not exist', response['message'])


