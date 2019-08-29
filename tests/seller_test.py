import json
from . import app, client, cache, create_token_customer, create_token_seller
import random

class TestSellerDetailsCrud():
    cust_id = 0
######### get profile
    def test_seller_details_profile(self, client):
        token = create_token_seller()
        res = client.get('seller/9',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_seller_details_invalid_profile(self, client):
        token = create_token_customer()
        res = client.get('seller/2', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### post

    def test_seller_sign_up(self, client):
        random_number = int(random.random()*1000)
        data = {
            "email": "seller"+ str(random_number) +"@google.com",
            "name": "Seller "+ str(random_number),
            "password": "Seller Tes " + str(random_number),
            "phone_number": "082"+ str(random_number),
            "address": "Alamat "+ str(random_number),
            "province": "provinsi"+ str(random_number),
            "city": "kota"+ str(random_number),
            "postcode": 13298,
            "status": 99
        }
        res=client.post('seller', 
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        TestSellerDetailsCrud.cust_id = res_json['id']
        assert res.status_code == 200

    def test_seller_invalid_sign_up(self, client):
        random_number = int(random.random()*1000)
        data = {
            "email": "seller"+ str(random_number) +"@google.com",
            "name": "Seller "+ str(random_number),
            "phone_number": "082seller"+ str(random_number),
            "address": "Alamat "+ str(random_number),
            "province": "provinsi"+ str(random_number),
            "city": "kota"+ str(random_number),
            "postcode": 98762,
            "status": 99
        }
        res=client.post('seller', 
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        res_json=json.loads(res.data)
        assert res.status_code == 400

######### put

    def test_seller_update(self, client):
        random_number = int(random.random()*1000)
        token = create_token_seller()
        data = {
            "email": "seller"+ str(random_number) +"@google.com",
            "name": "Seller "+ str(random_number),
            "password": "Seller Tes " + str(random_number),
            "phone_number": "082seller"+ str(random_number),
            "address": "Alamat "+ str(random_number),
            "province": "Lampung",
            "city": "kota"+ str(random_number),
            "postcode": 66762,
            "status": 99
        }
        res=client.put('seller', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_seller_invalid_update(self, client):
        token = create_token_customer()
        data = {
            "name": "Seller 1 tes",
            "phone_number": "082seller1",
            "address": "Kera Ngalam",
            "postcode": 40611
        }
        res=client.put('seller', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 403

    def test_client_list(self, client):
        token = create_token_seller()
        res = client.get('/seller/list',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_client_invalid_list(self, client):
        # token = create_token_customer()
        res = client.get('/seller/list')#, 
                        # headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 500

    def test_product_customer_delete(self, client):
        token = create_token_seller()
        res=client.delete(f'/seller/{TestSellerDetailsCrud.cust_id}', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_product_customer_invalid_delete(self, client):
        token = create_token_customer()
        res=client.delete(f'/seller/100', 
                        headers={'Authorization': 'Bearer ' + token}
                        )

        assert res.status_code == 404