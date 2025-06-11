import pandas as pd
import requests
import boto3
from datetime import datetime

s3_client = boto3.client('s3')

# Google Finance API (assumed endpoint, replace with actual API)
def fetch_stock_data(ticker='AAPL', days=30):
    url = f"https://finance.google.com/finance/api/{ticker}"  # Placeholder
    response = requests.get(url)  # Use actual Google Finance API
    data = response.json()  # Assumed JSON response
    df = pd.DataFrame(data['prices'], columns=['date', 'close', 'volume'])
    return df

# Save to S3
def save_to_s3(df, bucket='your-bucket', ticker='AAPL'):
    year, month = datetime.now().strftime('%Y'), datetime.now().strftime('%m')
    s3_key = f'stock_data/ticker={ticker}/year={year}/month={month}/data.csv'
    df.to_csv(f's3://{bucket}/{s3_key}', index=False)
    print(f'Saved data to s3://{bucket}/{s3_key}')

if __name__ == '__main__':
    df = fetch_stock_data()
    save_to_s3(df)