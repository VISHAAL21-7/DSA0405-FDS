import numpy as np
from sklearn.linear_model import LinearRegression

# Original dataset from the scenario (unchanged)
X = np.array([
    [2, 25000, 1200],
    [5, 60000, 1500],
    [3, 40000, 1300],
    [7, 90000, 1800],
    [1, 15000, 1000]
])
y = np.array([650000, 420000, 520000, 300000, 720000])  # Resale_Price

model = LinearRegression()
model.fit(X, y)

# Brand price multiplier (applied on top of the regression prediction)
brand_multiplier = {"Maruti": 1.0, "Honda": 1.1, "BMW": 4.0, "Mercedes": 4.5}

# Accept user input for a new car
age = float(input("Enter car age (years): "))
kms = float(input("Enter kilometers driven: "))
engine_cc = float(input("Enter engine capacity (cc): "))
brand = input("Enter car brand (Maruti/Honda/BMW/Mercedes): ")

base_price = model.predict([[age, kms, engine_cc]])[0]
base_price = max(base_price, 50000)  # floor, avoids negative/nonsense base

multiplier = brand_multiplier.get(brand, 1.0)
final_price = base_price * multiplier

print(f"Estimated Resale Price: ₹{final_price:,.2f}")
