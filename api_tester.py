import hashlib
import requests
import random


end_point = "https://gateway.marvel.com:443/v1/public/characters?ts="
request_id = str(random.randint(1000,9999))
public_key = "397874f2d3ac2224968baf9dd584e9e4"
private_key = "97f28c16c2b0e56990ce5ba158b85589b82865b5"

#Generate md5 hash
key_initializer = request_id + private_key + public_key
api_key = hashlib.md5(key_initializer.encode())
key_request = api_key.hexdigest()

def apiCaller( request):
    #calling API
    response = requests.get(request)

    if response.status_code == 200:
        print("Sucess => 200")
        print(response.json()) 
    else:
        print("Failure")
        response.status_code

#Constructor
request = end_point + request_id + '&apikey=' + public_key + '&hash=' + key_request

apiCaller(request)


