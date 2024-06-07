import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
file_path = r'C:\Users\kyler\OneDrive\Desktop\GIS6345\Week5\Nationwide_Drugs_2020_2024.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
data_head = data.head()
print(data_head)

# Choose a field to plot: "Drug Type" and "Sum Qty (lbs)"
# Convert "Sum Qty (lbs)" to numeric
data['Sum Qty (lbs)'] = pd.to_numeric(data['Sum Qty (lbs)'], errors='coerce')

# Group by "Drug Type" and sum the quantities
grouped_data = data.groupby('Drug Type')['Sum Qty (lbs)'].sum().reset_index()

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['Drug Type'], grouped_data['Sum Qty (lbs)'])
plt.xlabel('Drug Type')
plt.ylabel('Total Quantity (lbs)')
plt.title('Total Quantity of Drugs Seized by Type (2020-2024)')
plt.xticks(rotation=45)
plt.show()
