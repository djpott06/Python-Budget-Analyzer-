import pandas as pd 
import matplotlib.pyplot as plt

def load_data():
    data = pd.read_csv("sample_transactions.csv")
    return data

def calculate_totals(data):
    income = 9000
    needs = ["Rent", "Groceries", "Utilities", "Transportation"]
    wants = ["Entertainment", "Dining", "Shopping", "Subscriptions"]
    
    total_spent = data["Amount"].sum()
    needs_total = data[data["Category"].isin(needs)]["Amount"].sum()
    wants_total = data[data["Category"].isin(wants)]["Amount"].sum()
    savings = income - total_spent

    needs_percentage = float((needs_total / income * 100).round(2))
    wants_percentage = float((wants_total / income * 100).round(2))
    savings_percentage = float((savings / income * 100).round(2))

    return needs_percentage, wants_percentage, savings_percentage

def print_summary(needs_pct, wants_pct, savings_pct):
    print(f"Needs: {needs_pct:.1f}% (Recommended: 50%)")
    print(f"Wants: {wants_pct:.1f}% (Recommended: 30%)")
    print(f"Savings: {savings_pct:.1f}% (Recommended: 20%)")

def plot_chart(needs_pct, wants_pct, savings_pct):
    plt.figure(figsize=(6, 6))
    plt.pie(
        [needs_pct, wants_pct, savings_pct],
        labels=['Needs', 'Wants', 'Savings'],
        colors=['b', 'r', 'g'],
        startangle=90,
        explode=(0, 0, 0.05),
        autopct='%1.1f%%'
    )
    plt.axis("equal")
    plt.title("Needs/Wants/Savings")
    plt.legend(loc="lower left")
    plt.show()
    plt.close()

def plot_bar(data):
    category_totals = data.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 5))
    category_totals.plot(kind="bar", color="steelblue", edgecolor="white")
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
    plt.close()
    

def main():
    data = load_data()
    needs_pct, wants_pct, savings_pct = calculate_totals(data)
    print_summary(needs_pct, wants_pct, savings_pct)
    plot_chart(needs_pct, wants_pct, savings_pct) 
    plot_bar(data)
    

main()