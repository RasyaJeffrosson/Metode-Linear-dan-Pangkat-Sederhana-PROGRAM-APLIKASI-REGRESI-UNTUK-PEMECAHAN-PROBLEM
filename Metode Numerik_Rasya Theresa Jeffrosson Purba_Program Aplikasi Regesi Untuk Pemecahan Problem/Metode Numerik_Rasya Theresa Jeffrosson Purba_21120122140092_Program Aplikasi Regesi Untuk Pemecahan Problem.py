import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

# Function for the simple power law model
def power_law(x, a, b):
    return a * np.power(x, b)

# Function to fit the simple power law model
def fit_power_law_model(X, y):
    # Avoid zero values in X
    X_nonzero = X[X > 0]
    y_nonzero = y[X > 0]
    params, _ = curve_fit(power_law, X_nonzero, y_nonzero, p0=[1, 2])
    return params

# Function to predict using the simple power law model
def predict_power_law_model(X, params):
    a, b = params
    return a * np.power(X, b)

# Function to calculate the RMS error
def calculate_rms_error(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

# Reading data from CSV
data_path = r'D:\Metode Numerik_Rasya Theresa Jeffrosson Purba_Program Aplikasi Regesi Untuk Pemecahan Problem\Metode_Numerik_Student_Performance.csv'
data = pd.read_csv(data_path)
X = data['Sample Question Papers Practiced'].values.reshape(-1, 1)
y = data['Performance Index'].values

# Creating a linear regression model
linear_model = LinearRegression()
linear_model.fit(X, y)

# Predicting using the linear regression model
y_pred_linear = linear_model.predict(X)

# Calculating RMS error for the linear regression model
rms_error_linear = calculate_rms_error(y, y_pred_linear)

# Fitting the simple power law model
params = fit_power_law_model(X.flatten(), y)

# Creating dense x values for a smoother curve
dense_X = np.linspace(X.min(), X.max(), 300)

# Predicting using the simple power law model
y_pred_power = predict_power_law_model(dense_X, params)

# Calculating RMS error for the simple power law model
rms_error_power = calculate_rms_error(y, predict_power_law_model(X.flatten(), params))

# Plotting the results of linear regression and simple power law side by side
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Plot linear regression
axs[0].scatter(X, y, color='blue', label='Actual Data', s=2, alpha=1)
axs[0].plot(X, y_pred_linear, color='cyan', label=f'Linear Regression (RMS Error: {rms_error_linear:.2f})')
axs[0].set_xlim(0, 10)
axs[0].set_xlabel('Sample Question Papers Practiced')
axs[0].set_ylabel('Performance Index')
axs[0].set_title('Linear Regression')
axs[0].legend()
axs[0].grid(True, linestyle='-', alpha=0.5)

# Plot simple power law regression
axs[1].scatter(X, y, color='blue', label='Actual Data', s=2, alpha=1)
axs[1].plot(dense_X, y_pred_power, color='red', label=f'Power Law Regression (RMS Error: {rms_error_power:.3f})')
axs[1].set_xlim(0, 10)
axs[1].set_xlabel('Sample Question Papers Practiced')
axs[1].set_ylabel('Performance Index')
axs[1].set_title('Power Law Regression')
axs[1].legend()
axs[1].grid(True, linestyle='-', alpha=0.5)

plt.tight_layout()
plt.show()

print(f'RMS Error Linear: {rms_error_linear:.2f}')
print(f'RMS Error Power Law: {rms_error_power:.3f}')
