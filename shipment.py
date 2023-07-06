class Shipment:
    def search_by_career(self, career):
        data_list = []
        with open('data.txt') as f:
            for line in f:
                data = line.split(',')
                if career == data[1].lower():
                    data_list.append(data)

        if data_list:
            return data_list
        else:
            return {"status": 'false', "message": "Sorry no data available for career " + career}

    def search_by_shipment(self, shipment_id):
        data_list = []
        with open('data.txt') as f:
            for line in f:
                data = line.split(',')
                if shipment_id == data[0]:
                    data_list.append(data)

        if data_list:
            return data_list
        else:
            return {"status": 'false', "message": "Sorry your " + shipment_id + ' not exist'}
