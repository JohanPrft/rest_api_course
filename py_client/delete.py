import requests

product_id = input("Which product id would you like do delete?\n")
try:
	product_id = int(product_id)
except:
	print(f'{product_id} isnt valid id')

if (product_id):
	endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

	get_response = requests.delete(endpoint)
	print(get_response.status_code)
