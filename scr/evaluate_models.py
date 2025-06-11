import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
import boto3

def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print(f'{model_name} RMSE: {rmse}')
    return rmse

if __name__ == '__main__':
    # Load test data
    df = pd.read_csv('s3://your-bucket/processed_data/ticker=AAPL/year=2025/month=06/data.csv')
    X = df[['moving_avg_7', 'moving_avg_30', 'price_change']].dropna()
    y = df['close'].shift(-1).dropna()
    X, y = X.align(y, join='inner', axis=0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Load models
    models = ['knn', 'svm', 'decision_tree']
    for name in models:
        model = joblib.load(f'{name}.joblib')
        evaluate_model(model, X_test, y_test, name)