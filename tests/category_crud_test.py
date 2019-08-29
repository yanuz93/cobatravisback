import json
from . import app, client, cache, create_token_customer, create_token_seller

class TestProductCategoryCrud():

    product_id = 0

######### get list
    def test_product_list(self, client):
        token = create_token_seller()
        res = client.get('/category/list',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_product_invalid_list(self, client):
        # token = create_token_customer()
        res = client.get('/category/list' #, 
                        # headers={'Authorization': 'Bearer ' + token}
                        )
        res_json=json.loads(res.data)
        assert res.status_code == 500

######### get
    def test_product_get(self, client):
        token = create_token_seller()
        res = client.get('/category/1',
                        headers={'Authorization': 'Bearer ' + token})
        
        res_json=json.loads(res.data)
        assert res.status_code == 200

    def test_product_invalid_get(self, client):
        token = create_token_seller()
        res = client.get('/category/5', 
                        headers={'Authorization': 'Bearer ' + token})
        res_json=json.loads(res.data)
        assert res.status_code == 404

######### post

    def test_product_input(self, client):
        token = create_token_seller()
        data = {
            "category": "peralatan makan"
        }
        res=client.post('/category', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)

        TestProductCategoryCrud.product_id = res_json['id']
        assert res.status_code == 200

    def test_product_invalid_input(self, client):
        token = create_token_seller()
        data = {
            "category": "peralatan makan"
        }
        res=client.post('/category', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 404

######### put

    def test_product_update(self, client):
        token = create_token_seller()
        data = {
            "category": "peralatan jalan-jalan"
        }
        res=client.put(f'/category/{TestProductCategoryCrud.product_id}', 
                        headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 200
    
    def test_product_invalid_update(self, client):
        # token = create_token_seller()
        data = {
            "category": "peralatan jalan-jalan",
            "description": "semua peralatan jalan-jalan anak"
        }
        res=client.put(f'/category/{TestProductCategoryCrud.product_id}', 
                        # headers={'Authorization': 'Bearer ' + token},
                        data=json.dumps(data),
                        content_type='application/json')

        res_json=json.loads(res.data)
        assert res.status_code == 500

######### delete
    def test_product_delete(self, client):
        token = create_token_seller()
        res=client.delete(f'/category/{TestProductCategoryCrud.product_id}', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 200

    def test_product_invalid_delete(self, client):
        token = create_token_seller()
        res=client.delete(f'/category/{TestProductCategoryCrud.product_id}', 
                        headers={'Authorization': 'Bearer ' + token})

        assert res.status_code == 404

        