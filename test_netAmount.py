from flask_initialize import app
import requests

def test_get_net_amount():     
	# Send a GET request to /transactions/1 endpoint     
	response = requests.get("http://127.0.0.1:5000/merchant/6540")     
	# Check if the response status code is 200     
	assert response.status_code == 200     
	# Check if the response JSON object matches the expected value     
	assert response.json() == [
								  {
								    "merchant_type_code": 6540,
								    "net_amount_in_dollars": 250,
								    "date": "2023-03-15"
								  },
								  {
								    "merchant_type_code": 6540,
								    "net_amount_in_dollars": 50,
								    "date": "2023-04-30"
								  },
								  {
								    "merchant_type_code": 6540,
								    "net_amount_in_dollars": 400,
								    "date": "2023-05-04"
								  },
								  {
								    "merchant_type_code": 6540,
								    "net_amount_in_dollars": 255,
								    "date": "2023-05-06"
								  }
							   ]