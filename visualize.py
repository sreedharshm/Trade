import pandas as pd
import plotly.express as px

# Load the CSV file
file_path = 'data\ZOMATO.csv'
data = pd.read_csv(file_path)

# Assuming the CSV contains 'Date' and 'Price' columns
# Parse the Date column if not already in datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Create an interactive line plot for trading prices over time
fig = px.line(data, x='Date', y='Close', title='Trading Data', labels={'Price': 'Price (INR)'})

# Show the plot
fig.show()
