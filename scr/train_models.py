import boto3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
import joblib

sagemaker_client = boto3.client('sagemaker')

def train_model(model, X_train, y_train, model_name):
    model.fit(X_train, y_train)
    joblib.dump(model, f'{model_name}.joblib')
    return model

def upload_to_s3(file_name, bucket='your-bucket', key='models/'):
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_name, bucket, key + file_name)
    print(f'Uploaded {file_name} to s3://{bucket}/{key}{file_name}')

if __name__ == '__main__':
    # Load processed data
    df = pd.read_csv('s3://your-bucket/processed_data/ticker=AAPL/year=2025/month=06/data.csv')
    X = df[['moving_avg_7', 'moving_avg_30', 'price_change']].dropna()
    y = df['close'].shift(-1).dropna()
    X, y = X.align(y, join='inner', axis=0)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train models
    models = {
        'knn': KNeighborsRegressor(),
        'svm': SVR(),
        'decision_tree': DecisionTreeRegressor()
    }
    
    for name, model in models.items():
        trained_model = train_model(model, X_train, y_train, name)
        upload_to_s3(f'{name}.joblib')
    
    # SageMaker training (example)
    # Replace with actual SageMaker training job configuration
    print("SageMaker training job initiated")