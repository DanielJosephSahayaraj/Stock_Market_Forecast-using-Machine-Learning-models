import pandas as pd
import boto3

s3_client = boto3.client('s3')

def preprocess_data(bucket='your-bucket', key='stock_data/ticker=AAPL/year=2025/month=06/data.csv'):
    # Read from S3
    obj = s3_client.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(obj['Body'])
    
    # Handle missing values
    df = df.fillna(method='ffill')
    
    # Feature engineering
    df['moving_avg_7'] = df['close'].rolling(window=7).mean()
    df['moving_avg_30'] = df['close'].rolling(window=30).mean()
    df['price_change'] = df['close'].pct_change()
    
    # Save processed data to S3
    processed_key = key.replace('stock_data', 'processed_data')
    df.to_csv(f's3://{bucket}/{processed_key}', index=False)
    print(f'Saved processed data to s3://{bucket}/{processed_key}')
    
    return df

if __name__ == '__main__':
    preprocess_data()