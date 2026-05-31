# Sample: Sales Forecasting using Scikit-Learn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Generate sample data (since sales_data.csv is not available)
np.random.seed(42)
n = 200
df = pd.DataFrame({
    'marketing_spend':  np.random.randint(1000, 10000, n),
    'seasonal_factor':  np.random.uniform(0.5, 2.0, n),
    'past_sales':       np.random.randint(5000, 50000, n),
})
df['future_sales'] = (
    df['marketing_spend'] * 2.5
    + df['seasonal_factor'] * 3000
    + df['past_sales'] * 0.8
    + np.random.normal(0, 500, n)
)

X = df[['marketing_spend', 'seasonal_factor', 'past_sales']]
y = df['future_sales']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Using Random Forest (AI Trend) for higher accuracy
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Predict future trends
predictions = model.predict(X_test)
print("Predictions (first 5):", predictions[:5])
print("Model R² score:", model.score(X_test, y_test))