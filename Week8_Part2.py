import pandas as pd
from arcgis.features import GeoAccessor, GeoSeriesAccessor
from arcgis.gis import GIS
import matplotlib.pyplot as plt

# Setup a GIS object
gis = GIS('home')

# Load the CSV data into a pandas DataFrame
csv_path = r"C:\Users\kyler\OneDrive\Desktop\GIS6980\Project Data\Vector\Border_Crossing_Entry_Data.csv"
data = pd.read_csv(csv_path)

# Custom function to parse dates
def custom_date_parser(date_str):
    try:
        if '-' in date_str:
            parts = date_str.split('-')
            if parts[1].isdigit():  # Format "Month-Year" e.g., "Dec-23"
                year = int('19' + parts[1]) if int(parts[1]) < 96 else int('20' + parts[1])
                month = parts[0]
                return pd.to_datetime(f'{month} {year}', format='%b %Y')
            else:  # Format "Day-Month" e.g., "23-Dec", assuming these are for the year 2024
                day = parts[0]
                month = parts[1]
                return pd.to_datetime(f'{day} {month} 2024', format='%d %b %Y')
    except ValueError:
        return pd.NaT  # Return Not a Time (NaT) if any parsing error

# Apply the custom date parser
data['Date'] = data['Date'].apply(custom_date_parser)

# CSV 'Latitude' and 'Longitude' for the coordinates
data['SHAPE'] = data.apply(lambda row: {'x': row['Longitude'], 'y': row['Latitude'], 'spatialReference': {'wkid': 4326}}, axis=1)

# Convert the pandas DataFrame to a Spatially Enabled DataFrame (SED)
sdf = pd.DataFrame.spatial.from_xy(data, 'Longitude', 'Latitude')

# Create a map centered around the data
m = gis.map('United States', zoomlevel=4)

# Assuming 'Measure' column exists and you want to differentiate points based on it
# Use a simple renderer with a color map for visualization
sdf.spatial.plot(map_widget=m,
                 renderer_type='u',  # Unique renderer based on 'Measure' values
                 col='Measure',  # This is the column based on which to apply unique colors
                 cmap='viridis',  # Use a Matplotlib colormap
                 alpha=0.7)  # Transparency of points

# Filter data for a specific port of entry, e.g., "Roma, Texas"
roma_sdf = sdf[sdf['Port Name'] == "Roma"]

# Group by Date and Measure, then sum the Values
roma_grouped = roma_sdf.groupby(['Date', 'Measure'])['Value'].sum().unstack(fill_value=0)

# Plotting the data using Matplotlib
fig, ax = plt.subplots(figsize=(12, 8))
roma_grouped.plot(kind='line', marker='o', ax=ax)
ax.set_title('Number of Entries by Transportation Measure at Roma, Texas')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Entries')
ax.grid(True)

plt.show()








