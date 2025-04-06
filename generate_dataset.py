import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Define categories as needs and wants with adjusted realistic expenditure ranges
categories = {
    'Groceries': {'type': 'need', 'min': 50, 'max': 500},
    'Rent': {'type': 'need', 'min': 500, 'max': 2000},
    'Utilities': {'type': 'need', 'min': 50, 'max': 300},
    'Transport': {'type': 'need', 'min': 50, 'max': 500},
    'Healthcare': {'type': 'need', 'min': 20, 'max': 300},
    'Dining Out': {'type': 'want', 'min': 10, 'max': 200},
    'Shopping': {'type': 'want', 'min': 20, 'max': 500},
    'Entertainment': {'type': 'want', 'min': 20, 'max': 300},
    'Travel': {'type': 'want', 'min': 50, 'max': 1000},
    'Food Delivery': {'type': 'want', 'min': 5, 'max': 100},
    'Subscriptions': {'type': 'want', 'min': 5, 'max': 50}
}

# Function to generate a single transaction with more realistic amounts
def generate_transaction(start_date, end_date):
    date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    category = random.choice(list(categories.keys()))
    category_info = categories[category]
    amount = round(random.uniform(category_info['min'], category_info['max']), 2)
    description = f"{category} expense"
    type_of_expense = category_info['type']
    return {
        'datetime': date,
        'date': date.strftime('%Y-%m-%d'),
        'time': date.strftime('%H:%M:%S'),
        'month': date.strftime('%B %Y'),
        'week': f"Week {date.isocalendar()[1]}",
        'category': category,
        'amount': amount,
        'description': description,
        'type': type_of_expense
    }

# Generate 1000 transactions between Jan 2024 and April 2025
start = datetime(2024, 1, 1)
end = datetime(2025, 4, 5)
transactions = [generate_transaction(start, end) for _ in range(1000)]

# Create a DataFrame
df = pd.DataFrame(transactions)
df.sort_values(by="datetime", inplace=True)

# Save the data
df.to_csv("mock_transactions_realistic.csv", index=False)
print("✅ Dataset generated: mock_transactions_realistic.csv")