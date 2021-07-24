import requests
import json
URL='http://127.0.0.1:8000/inventary/'

data={
    'product_name' : 'Dell',
    'product_detail_name' : 'Dell Vostro-3468',
    'price' : 40000,
    'product_category':'better'
}

json_data=json.dumps(data)

r=requests.post(url=URL,data = json_data)
 
data=r.json()
print(data) 