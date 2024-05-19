import pandas as pd
import csv

# Read the appended CSV file into a DataFrame
df = pd.read_csv('cleaned_data.csv')

# Looking at the missing variables ------------------------------------------------------------------------------
import missingno as msno
import matplotlib.pyplot as plt

msno.bar(df)
plt.show()

# The missing variables show that there are many missing variables especially for the layovers as there is 
# NA when we don't have a second or third layover. We can treat this setting "No layover" in these. 

# Summary statistics ------------------------------------------------------------------------------------

# For numerical columns
summary_statistics_numerical = df.describe()

# For non-numerical columns
summary_statistics_non_numerical = df.describe(include=['object'])

print("Summary Statistics for Numerical Columns:")
print(summary_statistics_numerical)
print("\nSummary Statistics for Non-Numerical Columns:")
print(summary_statistics_non_numerical)

from tabulate import tabulate

# Print the untransposed summary statistics table using tabulate
print(tabulate(summary_statistics_numerical, headers='keys', tablefmt='grid'))

# Transpose the summary statistics DataFrame for better readability
summary_statistics_transposed = summary_statistics_non_numerical.describe().transpose()

# Export the untransposed summary statistics DataFrame to an Excel file with a specific sheet name
summary_statistics_numerical.to_excel('summary_statistics.xlsx', sheet_name='Summary Statistics', index=True)
summary_statistics_transposed.to_excel('summary_statistics_cat.xlsx', sheet_name='Summary Statistics', index=True)

# Looking at our depending variable price -------------------------------------------------------------
print(df['Grand Total Price'])

df['Grand Total Price'].isna().sum()
# no missing values !!

# Histogram for each numerical column
df['Grand Total Price'].hist(figsize=(10, 5), bins=10)
plt.suptitle('Histogram for Grand Total Price')
plt.show()

# It seems like the price is very skewed. So we will try some transformations
import numpy as np
from scipy.stats import boxcox
from scipy.stats import yeojohnson


# Log transformation
log_transformed_data = np.log(df['Grand Total Price'])

# Box-Cox transformation
boxcox_transformed_data, _ = boxcox(df['Grand Total Price'])

# Yeo-Johnson transformation
yeojohnson_transformed_data, _ = yeojohnson(df['Grand Total Price'])


# Plot original and transformed data
plt.figure(figsize=(18, 8))

plt.subplot(2, 2, 1)
plt.hist(df['Grand Total Price'], bins=30, color='blue', alpha=0.7)
plt.title('Original Skewed Price')

plt.subplot(2, 2, 2)
plt.hist(log_transformed_data, bins=30, color='green', alpha=0.7)
plt.title('Log-Transformed Price')

plt.subplot(2, 2, 3)
plt.hist(boxcox_transformed_data, bins=30, color='purple', alpha=0.7)
plt.title('Box-Cox Transformed Price')

plt.subplot(2, 2, 4)
plt.hist(yeojohnson_transformed_data, bins=30, color='brown', alpha=0.7)
plt.title('Yeo-Johnson Transformed Price')

plt.show()
# Based on this graph, all the transformations seem to do the same, so we go with log transformation. 

# For Numerical Data ------------------------------------------------------------------------------------

#_______________________
# Check distributions 

# Plot histograms for all numerical columns in one figure with grid layout
num_cols = len(df.select_dtypes(include=['number']).columns)
num_rows = (num_cols + 1) // 2  # Calculate number of rows needed
fig, axes = plt.subplots(nrows=num_rows, ncols=2, figsize=(12, 8))

# Flatten axes for easy iteration
axes = axes.flatten()

# Plot histograms for each numerical column
for i, column in enumerate(df.select_dtypes(include=['number'])):
    df[column].hist(ax=axes[i], bins=10, color='skyblue', alpha=0.7)
    axes[i].set_title(f'Histogram of {column}')
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('Frequency')

# Hide unused subplots
for j in range(num_cols, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.show()

# It seems we should definitely need to do something with the data as it is very not normal. 
# Therefore, we should try scaling and centering these variables.

#______________________________
# Check for Near Zero Variance 

from sklearn.feature_selection import VarianceThreshold

# Select only numerical columns
numerical_df = df.select_dtypes(include=['number'])

# Calculate variance for each numerical feature
variances = numerical_df.var()

# Define a threshold for near-zero variance
threshold = 0.01  

# Get the names of features with near-zero variance
near_zero_var_features = variances[variances < threshold].index.tolist()

print("Features with near-zero variance:")
print(near_zero_var_features)
    # there does not seem to be any problems with near zero variance. All numeric variables seem to be ok. 

# Factor Variables ----------------------------------------------------------------------------------------------

#_________________
# Bar charts

# Select non-numeric columns
non_numeric_columns = df.select_dtypes(exclude=['number']).columns

# Plot bar charts for each non-numeric column
for column in non_numeric_columns:
    df[column].value_counts().plot(kind='bar', color='skyblue')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.title(f'Distribution of {column}')
    plt.show()

# There are many things to unpack here, more in the analysis. 







