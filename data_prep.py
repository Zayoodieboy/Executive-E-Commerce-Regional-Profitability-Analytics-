# Project 4: Executive E-Commerce & Regional Profitability Analytics
# Author: Data Analyst Portfolio
# Description: Programmatically generates synthetic retail transactions, handles 
# data sanitization, engineers financial margins and lead times, and exports a 
# clean master CSV for Tableau ingestion.

import pandas as pd
import numpy as np

# 1. Set seed and parameters for synthetic generation
np.random.seed(42)
n_rows = 1000

categories = {
    'Technology': ['Laptops', 'Accessories', 'Phones', 'Copiers'],
    'Furniture': ['Chairs', 'Tables', 'Bookcases', 'Furnishings'],
    'Office Supplies': ['Paper', 'Binders', 'Storage', 'Art']
}

regions = ['East', 'West', 'Central', 'South']
states = ['New York', 'California', 'Texas', 'Florida', 'Illinois', 'Washington']

data = []
for i in range(1, n_rows + 1):
    category = np.random.choice(list(categories.keys()))
    sub_category = np.random.choice(categories[category])
    region = np.random.choice(regions)
    state = np.random.choice(states)
    
    sales = round(np.random.uniform(20, 1500), 2)
    discount = round(np.random.choice([0.0, 0.1, 0.2, 0.3, 0.5]), 2)
    
    base_margin = np.random.uniform(0.15, 0.35) if category != 'Furniture' else np.random.uniform(0.05, 0.20)
    profit = round(sales * (base_margin - (discount * 1.2)), 2)
    
    order_date = pd.to_datetime('2026-01-01') + pd.to_timedelta(np.random.randint(0, 270), unit='D')
    ship_days = np.random.randint(1, 7)
    ship_date = order_date + pd.to_timedelta(ship_days, unit='D')

    data.append({
        'Order ID': f'ORD-{2026}-{1000 + i}',
        'Order Date': order_date,
        'Ship Date': ship_date,
        'Ship Mode': np.random.choice(['Standard Class', 'Second Class', 'First Class', 'Same Day']),
        'Region': region,
        'State': state,
        'Category': category,
        'Sub-Category': sub_category,
        'Sales': sales,
        'Quantity': np.random.randint(1, 10),
        'Discount': discount,
        'Profit': profit
    })

df = pd.DataFrame(data)

# 2. Data Cleaning & Feature Engineering
# Calculate Profit Margin Ratio to normalize profitability across varying sale sizes
df['Profit Margin Ratio'] = round(df['Profit'] / df['Sales'], 4)

# Calculate Shipping Days to evaluate logistics turnaround times
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# 3. Export Clean Master Dataset for Tableau Ingestion
df.to_csv('ecommerce_master_clean.csv', index=False)
print("Successfully generated, cleaned, and exported 'ecommerce_master_clean.csv'!")
