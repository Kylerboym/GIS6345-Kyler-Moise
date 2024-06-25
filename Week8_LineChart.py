import pandas as pd
import matplotlib.pyplot as plt

# Load your data
data_path = 'path_to_your_csv_file.csv'
data = pd.read_csv(data_path)

# Convert the quantity column to numeric if necessary
data['Sum Qty (lbs)'] = pd.to_numeric(data['Sum Qty (lbs)'], errors='coerce')

# Filter the data for specific drugs
drugs_of_interest = ['Heroin', 'Fentanyl']  # Modify this list as needed
filtered_data = data[data['Drug Type'].isin(drugs_of_interest)]

# Group by Fiscal Year and Drug Type, then sum the quantities
grouped_data = filtered_data.groupby(['FY', 'Drug Type'])['Sum Qty (lbs)'].sum().unstack().fillna(0)

# Adjust FY labels to end with the specific year (e.g., 2024) instead of 'FY'
grouped_data.index = [str(year) for year in grouped_data.index]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each drug type
for drug in drugs_of_interest:
    ax.plot(grouped_data.index, grouped_data[drug], marker='o', label=drug)

ax.set_ylabel('Quantity Seized (lbs)')
ax.set_title('Trends in Quantities of Heroin and Fentanyl Seized by Year')
ax.set_xticks(grouped_data.index)
ax.set_xticklabels(grouped_data.index, rotation=45)
ax.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
