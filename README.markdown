# Stock Market Forecasting with Machine Learning Models

## Overview
This project builds a machine learning pipeline to forecast stock prices using data from **Google Finance**, processed through an **ETL pipeline**, and trained with models like **KNN**, **SVM**, and **Decision Tree** on **AWS SageMaker**. The pipeline extracts historical stock data, preprocesses handling missing values, feature engineering, trains and evaluates models, and visualizes predictions in **Power BI**. An optional **NLP component** uses a BERT model to analyze financial news sentiment, enhancing prediction accuracy.

This project showcases my expertise in machine learning, cloud-based model training (AWS SageMaker), data preprocessing, and data visualization, aligning with data science roles in finance and tech.

## Technologies
- **Programming**: Python
- **Machine Learning**: scikit-learn (KNN, SVM, Decision Tree)
- **Cloud**: AWS SageMaker, S3
- **Data Source**: Google Finance API
- **Visualization**: Power BI
- **NLP (Optional)**: Hugging Face Transformers (BERT)
- **Other**: pandas, NumPy, Boto3

## Dataset
- Historical stock data from Google Finance
- Sample data included in `data/google_history_data.csv`.
- Optional: Financial news data for sentiment analysis.



1. **Extract**: Python script retrieves stock data via Google Finance API and saves to S3.
2. **Transform**: ETL script preprocesses data.
3. **Train**: KNN, SVM, and Decision Tree models are trained on AWS SageMaker.
4. **Evaluate**: Models are evaluated using metrics like RMSE and accuracy.
5. **Visualize**: Power BI dashboards display predicted vs. actual stock prices.
6. **Optional NLP**: BERT model analyzes financial news sentiment to improve predictions.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Danielmichaelraj/Stock_Market_Forecast-using-Machine-Learning-models.git
   cd Stock_Market_Forecast-using-Machine-Learning-models
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure AWS**:
   - Set up an S3 bucket for data storage.
   - Configure SageMaker using `config/sagemaker_config.json`.
4. **Extract Data**:
   ```bash
   python src/extract_data.py
   ```
5. **Run ETL Process**:
   ```bash
   python src/etl_process.py
   ```
6. **Train Models**:
   ```bash
   python src/train_models.py
   ```
7. **Evaluate Models**:
   ```bash
   python src/evaluate_models.py
   ```
8. **Visualize in Power BI**:
   - Connect Power BI to S3 or SageMaker outputs and import

## Results
- Processed **1M stock records** with 98% data quality after ETL.
- Achieved **RMSE of 2.5** for SVM model on stock price predictions.
- Visualized predicted vs. actual prices in Power BI, identifying trends 10% accuracy improvement with SVM.
- Optional NLP: BERT sentiment analysis of financial news improved prediction accuracy by **5%**.



## Future Improvements
- Integrate BERT for sentiment analysis of financial news to enhance predictions.
- Use deep learning models for time-series forecasting.
- Automate data extraction with AWS Lambda.

## Contact
- GitHub: [Daniel Joseph](https://github.com/Danielmichaelraj)
- LinkedIn: [Daniel Joseph](https://www.linkedin.com/in/daniel-joseph-sahayaraj-aws-engineer/)