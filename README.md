# Kasheesh

This is a data engineering take home assignment that shows how to load data from a CSV file into a SQLite database and expose it via a webserver with RESTful API using Python.

## Getting Started

To get started with this project, you need to clone this repository to your local machine, install the dependencies, and run the scripts. Here are the steps:



### Clone the repository

Use git to clone this repository to your local machine:

```bash
git clone https://github.com/timothyyang96/Kasheesh.git
```

Then, change your current directory to the project directory:

```bash
cd Kasheesh
```

### Install the dependencies

The project requires Python 3.x and the following libraries:

- pandas
- sqlite3
- flask
- pytest

You can install these libraries using pip:

```bash
pip install -r requirements.txt
```


This command will install all the dependencies listed in the `requirements.txt` file in your project.

Optionally, you can also create and activate a virtual environment to isolate your project and its dependencies from other Python projects. You can use the `venv` module that comes with Python 3. Here’s how to create and activate a virtual environment:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Load the data

Make sure that you have the `combined_transactions.csv` file under the folder of Kasheesh. This file contains data on users’ transactions with different merchants types.

Run the `sqlite_connection.py` script to load the data from the CSV file into a SQLite database:

```bash
python sqlite_connection.py
```

This will create a file called `transactions.db` in the project directory that contains two tables: `purchases` and `returns`.

### Start the webserver

Run the `webserver.py` script to start the webserver:

```bash
python webserver.py
```

This will start the webserver on your local machine and print the URL of the webserver on the console. By default, the webserver will run on port 5000.

## Using the API

The webserver provides two API endpoints that return JSON objects:

- `/transactions/<user_id>`: Returns all transactions given a user_id
- `/merchant/<merchant_type_code>`: Returns daily total purchases net of returns given a merchant_type_code

You can use any tool such as curl or postman to send requests to these endpoints and receive responses.

### Example request and response for `/transactions/<user_id>`

Request:

```bash
curl http://localhost:5000/transactions/1
```

Response:

```json
[
  {
    "user_id": 1,
    "amount_in_dollars": 100,
    "datetime": "2022-06-05T22:22:00+00:00",
    "merchant_type_code": 1
  },
  {
    "user_id": 1,
    "amount_in_dollars": -50,
    "datetime": "2022-06-06T10:10:00+00:00",
    "merchant_type_code": 2
  }
]
```

### Example request and response for `/merchant/<merchant_type_code>`

Request:

```bash
curl http://localhost:5000/merchant/1
```


Response:

```json
[
  {
    "merchant_type_code": 1,
    "net_amount_in_dollars": 50,
    "date": "2022-06-05"
  },
  {
    "merchant_type_code": 1,
    "net_amount_in_dollars": 0,
    "date": "2022-06-06"
  }
]
```


## Running the tests

To run the tests for this project, you need to run the `test_webserver.py` script using pytest. Here are the steps:

### Run flask_initialize.py

Before running pytest, you need to run `flask_initialize.py` as well. This will start your webserver on your local machine and make it available for your test script to send requests to. You can run `flask_initialize.py` using this command:

```bash
python flask_initialize.py
```


This will print the URL of your webserver on the console, which should be something like:

```bash
http://localhost:5000/
```


You can use this URL to access your webserver endpoints in your browser or in your test script. Make sure that your webserver is running before running pytest.

### Run test_webserver.py

Run the `test_webserver.py` script using pytest:

```bash
pytest test_webserver.py
```


This will run the tests for each function and print the results on the console. You should see something like this:

```bash
============================= test session starts ==============================
platform darwin -- Python 3.10.9, pytest-7.3.2, pluggy-1.0.0
rootdir: /Users/yyy/Downloads/Kasheesh
collected 1 item

test_netAmount.py .                                                      [100%]

============================== 1 passed in 0.85s ===============================
```
