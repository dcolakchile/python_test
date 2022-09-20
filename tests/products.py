import requests
import pytest
import json

def test_product_list_unauthorized():

     response = requests.get("http://127.0.0.1:8000/v1/products/list")

     assert response.status_code == 401	 


def test_product_list_authorized():

	headers = {"Authorization": "Bearer can_readwrite"}

	response = requests.get("http://127.0.0.1:8000/v1/products/list", headers=headers)

	assert response.status_code == 200

def test_product_create():
	
	headers = {"Authorization": "Bearer can_readwrite"}

	data = """
		{
	"id": 0,
	"name": "string",
	"uom": "string",
	"category_name": "string",
	"is_producible": true,
	"is_purchasable": true,
	"type": "string",
	"purchase_uom": "string",
	"purchase_uom_conversion_rate": 0,
	"batch_tracked": true,
	"variants": [
		{
		"id": 0,
		"product_id": 0,
		"sku": "string",
		"type": "string",
		"sales_price": 0,
		"purchase_price": 0,
		"config_attributes": [
			{
			"config_name": "string",
			"config_value": "string"
			}
		],
		"created_at": "2022-09-20T17:30:59.193Z",
		"updated_at": "2022-09-20T17:30:59.193Z"
		}
	],
	"additional_info": "string",
	"created_at": "2022-09-20T17:30:59.193Z",
	"updated_at": "2022-09-20T17:30:59.193Z"
	}"""

	response = requests.post("http://127.0.0.1:8000/v1/products/create", data=data, headers=headers)	

	assert response.status_code == 200