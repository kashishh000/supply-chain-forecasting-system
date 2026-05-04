import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import os

def train_model():
    try:
        df = pd.read_csv('data/supply_history.csv')
    except:
        print("Run generate_supply_data.py first!")
        return
        
    features = ['day_of_week', 'is_weekend', 'marketing_spend']
    X = df[features]
    y = df['demand']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    print(f"✅ Model Trained! Mean Absolute Error: {mae:.2f}")
    
    # Save predictions
    results = X_test.copy()
    results['Actual_Demand'] = y_test
    results['Predicted_Demand'] = preds
    results.to_csv('data/forecast_results.csv', index=False)

if __name__ == "__main__":
    train_model()
