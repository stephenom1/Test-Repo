import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Load and prepare data
df = pd.read_csv('AAPL_clean.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date').reset_index(drop=True)
df = df[df['Date'] >= '2010-01-01'].reset_index(drop=True)

closing_prices = df['Close_AAPL'].values

# Create sliding windows
window_size = 30
X, y = [], []

for i in range(window_size, len(closing_prices)):
    X.append(closing_prices[i-window_size:i])
    y.append(closing_prices[i])

X = np.array(X)
y = np.array(y)

# Train/test split (80/20, no shuffle for time series)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

print("Linear Regression Baseline (30-day window)")
print("-" * 40)
print(f"R²:   {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
print(f"MAE:  {mean_absolute_error(y_test, y_pred):.4f}")
print(f"MAPE: {np.mean(np.abs((y_test - y_pred) / y_test)) * 100:.2f}%")