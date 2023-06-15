from flask_initialize import app
import requests

def test_get_transactions():     
	# Send a GET request to /transactions/1 endpoint     
	response = requests.get("http://127.0.0.1:5000/transactions/73053")     
	# Check if the response status code is 200     
	assert response.status_code == 200     
	# Check if the response JSON object matches the expected value     
	assert response.json() == [
								  {
								    "user_id": 73053,
								    "amount_in_dollars": 709,
								    "datetime": "2023-05-16 07:14:29.832756",
								    "merchant_type_code": 5300
								  },
								  {
								    "user_id": 73053,
								    "amount_in_dollars": 956,
								    "datetime": "2023-05-31 07:13:35.739863",
								    "merchant_type_code": 5732
								  },
								  {
								    "user_id": 73053,
								    "amount_in_dollars": 1276,
								    "datetime": "2023-05-31 07:14:56.676358",
								    "merchant_type_code": 5732
								  }
							   ]