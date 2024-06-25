import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your CSV data
data_path = 'path_to_your_csv_file.csv'
data = pd.read_csv(data_path)

# Convert quantity column to numeric if necessary
data['Sum Qty (lbs)'] = pd.to_numeric(data['Sum Qty (lbs)'], errors='coerce')

# Filter the data for the drugs of interest
drugs_of_interest = ['Heroin', 'Fentanyl']  # Modify this list based on your drugs of interest
filtered_data = data[data['Drug Type'].isin(drugs_of_interest)]

# Group by Fiscal Year and Drug Type, then sum the quantities
grouped_data = filtered_data.groupby(['FY', 'Drug Type'])['Sum Qty (lbs)'].sum().unstack().fillna(0)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
years = grouped_data.index
x = np.arange(len(years))  # label locations
width = 0.35  # bar width

# Create bars for each drug
for i, drug in enumerate(drugs_of_interest):
    rects = ax.bar(x + i * width - width/2, grouped_data[drug], width, label=drug)
    ax.bar_label(rects, padding=3)

ax.set_ylabel('Quantity Seized (lbs)')
ax.set_title('Quantities of Selected Drugs Seized by Year')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
