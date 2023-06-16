import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# read csv
df = pd.read_csv('combined_transactions.csv')
df['amount_in_dollars'] = (df['amount_cents'] / 100).astype(int)
df['datetime'] = pd.to_datetime(df['datetime'], format='ISO8601')

# select rows satifying the criteria
purchase5732 = df[(df['transaction_type'] == 'PurchaseActivity') & (df['merchant_type_code'] == 5732)]
purchase5732.set_index('datetime', inplace=True)
daily_data = purchase5732['amount_in_dollars'].resample('D').sum()

# fit the model and print prediction
model = ARIMA(daily_data, order=(1, 0, 0))
result = model.fit()
prediction = result.forecast(steps=10)
print(prediction)

# plot the prediction with the original data
# Plot the original data and the prediction
plt.plot(daily_data, label='Original data')
plt.plot(prediction, label='10-day prediction')
plt.legend()
plt.show()