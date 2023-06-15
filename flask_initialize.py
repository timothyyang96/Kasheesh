from flask import Flask, jsonify
from sqlite_connection import create_connection

# Web Server Setup
app = Flask(__name__)
app.json_provider_class.sort_keys    = False

# API Endpoints
@app.route('/transactions/<int:user_id>', methods=['GET'])
def get_transactions(user_id):
    # Implement logic to fetch transactions for the given user_id

    # database connect
	database = 'transactions.sqlite'
	conn = create_connection(database)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM purchases WHERE user_id = ?", (user_id,))
	purchases = cursor.fetchall()
	cursor.execute("SELECT * FROM returns WHERE user_id = ?", (user_id,))
	returns = cursor.fetchall()
	transactions = purchases + returns
	transactions_json = [{'user_id':t[0],'amount_in_dollars':t[1],'datetime':t[2],'merchant_type_code':t[3]} for t in transactions]
	cursor.close()
	conn.close()
	return jsonify(transactions_json)

@app.route('/merchant/<int:merchant_type_code>', methods=['GET'])
def get_merchant_transactions(merchant_type_code):

	database = 'transactions.sqlite'
	conn = create_connection(database)
	cursor = conn.cursor()
	cursor.execute("""
	    SELECT 
	        merchant_type_code,
	        SUM(CASE WHEN transaction_type = 'PurchaseActivity' THEN amount_in_dollars ELSE 0 END) -
	        SUM(CASE WHEN transaction_type = 'ReturnActivity' THEN amount_in_dollars ELSE 0 END) as net_amount_in_dollars,
	        DATE(datetime) as date
	    FROM (
	        SELECT 'PurchaseActivity' as transaction_type, merchant_type_code, amount_in_dollars, datetime FROM purchases
	        UNION ALL
	        SELECT 'ReturnActivity' as transaction_type, merchant_type_code, amount_in_dollars, datetime FROM returns
	    ) AS transactions
	    WHERE merchant_type_code = ?
	    GROUP BY date, merchant_type_code
	""", (merchant_type_code,))
	results = cursor.fetchall()
	results_json = [{'merchant_type_code':r[0],'net_amount_in_dollars':r[1],'date':r[2]} for r in results]
	cursor.close()
	conn.close()
	return jsonify(results_json)


# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='127.0.0.1', debug=True)
