# Import necessary libraries
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load the spreadsheet into a DataFrame
file_path = r'C:\Users\VaterRW14\Downloads\RestaurantRevenue.xlsx'
df = pd.read_excel(file_path)

# Extract features (independent variables) and target (dependent variable)
X = df[['Number_of_Customers', 'Menu_Price', 'Marketing_Spend', 'Average_Customer_Spending', 'Promotions', 'Reviews']]
y = df['Monthly_Revenue']

# Add a constant column to the features (required for statsmodels)
X = sm.add_constant(X)

# Fit the multiple linear regression model
model = sm.OLS(y, X).fit()

# Print the regression summary
print(model.summary())

# Predict monthly revenue for a new restaurant based on user input
print("\nInput new data for prediction:")
num_customers = float(input("Number of customers: "))
menu_price = float(input("Menu price: "))
marketing_spend = float(input("Marketing spend: "))
avg_customer_spending = float(input("Average customer spending: "))
promotions = float(input("Promotions: "))
reviews = float(input("Reviews: "))

# Predict monthly revenue for the new restaurant
new_data = [[1, num_customers, menu_price, marketing_spend, avg_customer_spending, promotions, reviews]]
predicted_revenue = model.predict(new_data)[0]
print(f"\nPredicted monthly revenue for the new restaurant: ${predicted_revenue:.2f}")

# Create a multiple regression fit plot
fig, ax = plt.subplots()
ax.plot(y, model.fittedvalues, marker='o', linestyle='', markersize=5)
ax.set_xlabel("Actual Monthly Revenue")
ax.set_ylabel("Predicted Monthly Revenue")
ax.set_title("Multiple Regression Fit Plot")
plt.show()
