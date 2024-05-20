import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error


flights = pd.read_csv('/Users/aleksandrakusz/Desktop/2nd BI/flight_search/Feature_engineering/final_data.csv')


categorical_cols = flights.select_dtypes(include=['object']).columns
encoder = OneHotEncoder(drop='first')
encoded_cols = pd.DataFrame(encoder.fit_transform(flights[categorical_cols]).toarray())
encoded_cols.columns = encoder.get_feature_names_out(categorical_cols)
flights_encoded = pd.concat([flights.drop(columns=categorical_cols), encoded_cols], axis=1)

# Step 4: Split the data into features (X) and target variable (y)
X = flights_encoded.drop(columns=['Log Grand Total Price'])  # Features
y = flights_encoded['Log Grand Total Price']  # Target variable

# Step 5: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Initialize the decision tree regressor model
dt_model = DecisionTreeRegressor(random_state=42)

# Step 7: Train the model on the training data
dt_model.fit(X_train, y_train)

# Step 8: Make predictions on the test data
y_pred_dt = dt_model.predict(X_test)

# Step 9: Evaluate the model using mean squared error
mse_dt = mean_squared_error(y_test, y_pred_dt)
print("Decision Tree Mean Squared Error:", mse_dt)

dt_model.fit(X_train, y_train)

# Step 8: Visualize the decision tree
plt.figure(figsize=(20, 10))
plot_tree(dt_model, feature_names=X.columns, filled=True)
plt.show()



# Assume X_train and y_train are your training features and target variables
# Train a decision tree model
dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)

# Get feature importances
importances = dt_model.feature_importances_

# Sort feature importances in descending order
sorted_indices = np.argsort(importances)[::-1]
sorted_features = [X.columns[i] for i in sorted_indices]
sorted_importances = importances[sorted_indices]

# Print feature importances
for feature, importance in zip(sorted_features, sorted_importances):
    print(f"{feature}: {importance}")

# Visualize feature importances
plt.figure(figsize=(10, 6))
plt.bar(range(X.shape[1]), sorted_importances, tick_label=sorted_features)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Feature Importance (Decision Tree)')
plt.xticks(rotation=90)
plt.show()

# Visualize top 20 feature importances
top_features = sorted_features[:20]
top_importances = sorted_importances[:20]

plt.figure(figsize=(10, 6))
plt.bar(range(len(top_features)), top_importances, tick_label=top_features)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Top 20 Feature Importance (Decision Tree)')
plt.xticks(rotation=90)
plt.show()


# Calculate R-squared score
r2 = r2_score(y_test, y_pred_dt)
print("R-squared Score:", r2)

# Calculate mean squared error
mse = mean_squared_error(y_test, y_pred_dt)
print("Mean Squared Error:", mse)

# Calculate root mean squared error
rmse = np.sqrt(mse)
print("Root Mean Squared Error:", rmse)
