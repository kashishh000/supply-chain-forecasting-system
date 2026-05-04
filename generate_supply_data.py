import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_supply_data():
    np.random.seed(42)
    dates = [datetime(2023, 1, 1) + timedelta(days=i) for i in range(365)]
    
    data = []
    for d in dates:
        # Base demand + weekend spike + random noise
        base = 500
        weekend_mult = 1.5 if d.weekday() >= 5 else 1.0
        noise = np.random.normal(0, 50)
        demand = max(0, int(base * weekend_mult + noise))
        
        data.append({
            'date': d.strftime('%Y-%m-%d'),
            'day_of_week': d.weekday(),
            'is_weekend': 1 if d.weekday() >= 5 else 0,
            'marketing_spend': np.random.randint(100, 1000),
            'demand': demand
        })
        
    df = pd.DataFrame(data)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/supply_history.csv', index=False)
    print("✅ Supply chain data generated at data/supply_history.csv")

if __name__ == "__main__":
    generate_supply_data()
