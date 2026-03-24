# Sales by day of the week
sales = {
    "Monday": 1200,
    "Tuesday": 850,
    "Wednesday": 2100,
    "Thursday": 975,
    "Friday": 1800,
    "Saturday": 3200,
    "Sunday": 1450
}

# Find best and worst day
best_day = max(sales, key=sales.get)
worst_day = min(sales, key=sales.get)
total = sum(sales.values())

print(f"Total revenue: ${total}")
print(f"Best day: {best_day} with ${sales[best_day]}")
print(f"Worst day: {worst_day} with ${sales[worst_day]}")