import json
from . import app, client, cache, create_token_customer, create_token_seller
import random 

class TestProductCrud():

    product_id = 0

######### get list (public)
    def test_product_list(self, client):
        res = client.get('/product/list')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_product_list_customer(self, client):
        token = create_token_customer()
        res = client.get('/product/list',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

######### get list (seller)
    def test_product_list_seller(self, client):
        token = create_token_seller()
        res = client.get('/product/list',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_product_invalid_list_seller(self, client):
        token = create_token_customer()
        res = client.get('/product/list',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

# ######### get by id (public)
    def test_product_get(self, client):
        res = client.get('/product/4')
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_product_invalid_get(self, client):
        res = client.get('/product/1000')
        
        res_json=json.loads(res.data)
        assert res.status_code == 404

# ######### post

    def test_product_input(self, client):
        token = create_token_seller()
        data = {
            "name": "baju tes 2",
            "category_id": 1,
            "description": "ini adalah deskripsi tes untuk barang 2",
            "unit_price": 20000,
            "url_foto": "tes image src 2",
            "stock": 32
        }
        res=client.post('/product', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        TestProductCrud.product_id = res_json['id']
        assert res.status_code == 200

    def test_product_invalid_input(self, client):
        token = create_token_customer()
        data = {
            "name": "baju tes 2",
            "category_id": 1,
            "description": "ini adalah deskripsi tes untuk barang 2",
            "unit_price": 20000,
            "image": "tes image src 2",
            "stock": 32
        }
        res=client.post('/product', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 403

######### put

    def test_product_update(self, client):
        random_number = random.random() * 1000
        token = create_token_seller()
        data = {
            "name": "baju tes " + str(random_number),
            "category_id": 1,
            "description": "ini adalah deskripsi tes untuk barang 2",
            "unit_price": 20000,
            "url_foto": "tes image src 2",
            "stock": 32
        }
        res=client.put(f'/product/{TestProductCrud.product_id}', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_client_invalid_update(self, client):
        token = create_token_seller()
        data = {
            "category_id": 1,
            "description": "ini adalah deskripsi tes untuk barang 2",
            "unit_price": 20000,
            "url_foto": "tes image src 2",
        }
        res=client.put(f'/product/{TestProductCrud.product_id}', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 400

#########  soft delete
    def test_product_soft_delete(self, client):
        token = create_token_seller()
        res=client.delete(f'/product/{TestProductCrud.product_id}', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_product_invalid_soft_delete(self, client):
        token = create_token_seller()
        res=client.delete('/product/1000', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 404

# #########  hard delete
#     def test_product_hard_delete(self, client):
#         token = create_token_seller()
#         res=client.delete(f'/product/{TestProductCrud.product_id}', 
#                         headers={'Authorization': 'Bearer ' + token})

#         assert res.status_code == 200

#     def test_product_category_invalid_hard_delete(self, client):
#         token = create_token_seller()
#         res=client.delete('/product/1000', 
#                         headers={'Authorization': 'Bearer ' + token})

#         assert res.status_code == 404