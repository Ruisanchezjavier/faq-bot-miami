import csv

def load_sales(filename):
    sales = {}
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales[row["day"]] = int(row["sales"])
    return sales

def analyze(sales):
    total = sum(sales.values())
    best_day = max(sales, key=sales.get)
    worst_day = min(sales, key=sales.get)
    average = total / len(sales)
    return total, best_day, worst_day, average

sales = load_sales("sales.csv")
total, best_day, worst_day, average = analyze(sales)

print("=" * 35)
print("   WEEKLY SALES REPORT")
print("=" * 35)
print(f"Total revenue:  ${total:,}")
print(f"Best day:       {best_day} (${sales[best_day]:,})")
print(f"Worst day:      {worst_day} (${sales[worst_day]:,})")
print(f"Daily average:  ${average:,.2f}")
print("=" * 35)