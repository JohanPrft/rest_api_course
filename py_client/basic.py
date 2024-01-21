import requests

# endpoint = "https://httpbin.org/"
#
# get_response = requests.get(endpoint) # HTTP Request
# # get_response = requests.Response object
# print(get_response.text) # print content of response

# endpoint = "http://localhost:8000/api/home/"
# get_response = requests.get(endpoint)
# print(get_response.status_code) # print status of response
# print(get_response.json()) # print json of response

# # params = query params ../api/?abc=123
# endpoint = "http://localhost:8000/api/echo/"
# get_response = requests.get(endpoint, params={"abc": 123}, json={"query": "JSON query"})
# print(get_response.status_code)
# print(get_response.json())

# params = query params ../api/?abc=123
# endpoint = "http://localhost:8000/api/random_object_rest/"
# get_response = requests.get(endpoint)
# print(get_response.status_code)
# print(get_response.json())

endpoint = "http://localhost:8000/api/post_req/"
get_response = requests.post(endpoint, json={"title": "heyyyy"})
print(get_response.status_code)
print(get_response.json())
