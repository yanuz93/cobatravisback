import json
from . import app, client, cache, create_token_customer, create_token_seller
import random 

class TestTransactionDetailsR():
    order_id = 0
######### get transaction details (customer)
    def test_orderdetails_list(self, client):
        token = create_token_customer()
        res=client.get('/order', 
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_orderdetails_invalid_list(self, client):
        token = create_token_seller()
        res = client.get('/order/1',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 500

######### get order details (seller)
    def test_order_details_list(self, client):
        token = create_token_seller()
        res=client.get('/order/list', 
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_order_details_invalid_list(self, client):
        # token = create_token_customer()
        res = client.get('/order/list')
        
        res_json=json.loads(res.data)
        assert res.status_code == 500

##################### post
    def test_orderdetails_valid_post(self, client):
        token = create_token_customer()
        data = {
            'product_id': 2,
            'qty': 12,
            'status': 10
        }
        res=client.post('/order', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        # TestTransactionDetailsR.order_id = res_json['id']
        assert res.status_code == 200

    def test_orderdetails_invalid_list(self, client):
        token = create_token_customer()
        data = {
            'product_id': 2,
            'qty': -1,
            'status': 10
        }
        res=client.post('/order', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        print(res_json)
        assert res.status_code == 303

##################### patch
    def test_orderdetails_valid_patch_bayar(self, client):
        token = create_token_customer()
        data = {
            'action': 'bayar'
        }
        res=client.patch(f'/order/8', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_orderdetails_valid_patch_ubah(self, client):
        token = create_token_customer()
        data = {
            'action': 'ubah_qty',
            'new_qty': 13
        }
        res=client.patch(f'/order/3', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_orderdetails_valid_patch_delete(self, client):
        token = create_token_customer()
        data = {
            'action': 'delete'
        }
        res=client.patch(f'/order/3', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200