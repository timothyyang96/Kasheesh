# Kasheesh
DE take home assignment

Data ETL and Webserver with RESTful API
This project demonstrates how to load data from a CSV file into a SQLite database and expose it via a webserver with RESTful API using Python.

Dependencies
The project requires Python 3.x and the following libraries:

pandas
sqlite3
flask
pytest
You can install these libraries using pip:

pip install pandas sqlite3 flask pytest

How to build and start your webserver
To build and start your webserver, follow these steps:

Clone this repository to your local machine using git:
git clone https://github.com/timothyyang96/Kasheesh.git

Navigate to the project directory:
cd Kasheesh

**Create a virtual environment (optional)**: This is a good practice to isolate your project and its dependencies from other Python projects. You can use the `venv` module that comes with Python 3. Here's how to create and activate a virtual environment:

   ```bash
   bashCopy code
   python3 -m venv myenv
   source myenv/bin/activate
   ```
   
**Install dependencies**: If you have a `requirements.txt` file in your project, you can install all the dependencies with one command:

   ```bash
   bashCopy code
   pip install -r requirements.txt
   ```

Run the data_etl.py script to load the data from the combined_transactions.csv file into the SQLite database:
python data_etl.py

This will create a file called transactions.db in the project directory that contains two tables: purchases and returns.

Run the webserver.py script to start the webserver:
python webserver.py

This will start the webserver on your local machine and print the URL of the webserver on the console. By default, the webserver will run on port 5000.

How to use the API endpoints
The webserver provides two API endpoints that return JSON objects:

/transactions/<user_id>: Returns all transactions given a user_id
/net_purchases/<merchant_type_code>: Returns daily total purchases net of returns given a merchant_type_code
You can use any tool such as curl or postman to send requests to these endpoints and receive responses.

Example request and response for /transactions/<user_id>
Request:

curl http://localhost:5000/transactions/1

Response:

[ { “user_id”: 1, “amount_in_dollars”: 100, “datetime”: “2022-06-05T22:22:00+00:00”, “merchant_type_code”: 1 } , { “user_id”: 1, “amount_in_dollars”: -50, “datetime”: “2022-06-06T10:10:00+00:00”, “merchant_type_code”: 2 } ]

Example request and response for /net_purchases/<merchant_type_code>
Request:

curl http://localhost:5000/net_purchases/1

Response:

[ { “merchant_type_code”: 1, “net_amount_in_dollars”: 50, “date”: “2022-06-05” } , { “merchant_type_code”: 1, “net_amount_in_dollars”: 0, “date”: “2022-06-06” } ]

How to run the unit tests
To run the unit tests, follow these steps:

Navigate to the project directory:
cd data-etl-webserver

Run the test_webserver.py script using pytest:
pytest test_webserver.py

This will run the unit tests for each function and print the results on the console. You should see something like this:

============================= test session starts ============================== platform win32 – Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0 rootdir: C:\Users\your_username\data-etl-webserver collected 6 items

test_webserver.py … [100%]

============================== 6 passed in 0.15s ===============================
