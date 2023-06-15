import sqlite3
from sqlite3 import Error
import pandas as pd

# read csv data
df = pd.read_csv('combined_transactions.csv')
# data processing
df['amount_in_dollars'] = (df['amount_cents'] / 100).astype(int)
df['datetime'] = pd.to_datetime(df['datetime'], format='ISO8601')
purchases = df[df['transaction_type'] == 'PurchaseActivity']
purchases = purchases[["user_id","amount_in_dollars","datetime","merchant_type_code"]]
returns = df[df['transaction_type'] == 'ReturnActivity']
returns = returns[["user_id","amount_in_dollars","datetime","merchant_type_code"]]

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 

def create_table(conn, table_name):
    cur = conn.cursor()
    cur.execute( (
        "CREATE TABLE IF NOT EXISTS {}"
        "( user_id INTEGER NOT NULL,"
        " amount_in_dollar INTEGER,"
        " datetime NUMERIC,"
        " merchant_type_code INTEGER,"
        " PRIMARY KEY(user_id,datetime))"
    ).format(table_name)
    )
    
def insert_records(conn, df, table_name):
    
    cur = conn.cursor()
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()


def query_table(conn, table_name):

    cur = conn.cursor()
    cur.execute("SELECT * FROM {} LIMIT 10".format(table_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)


# main driver function
if __name__ == '__main__':

    database = 'transactions.sqlite'
    table_names = ['purchases', 'returns']
    tables = [purchases, returns]

    # create a database connection
    conn = create_connection(database)
    with conn:
        for i in range(len(tables)):
            create_table(conn, table_names[i])
            insert_records(conn, tables[i], table_names[i])
            print('{} insertion finished! Following are the record snippets.'.format(table_names[i]))
            query_table(conn, table_names[i])

    conn.close()
