"""
aws_storage_analysis.py
Starter script to analyze storage usage sample data.
"""
import pandas as pd

def load_data(path="storage_data_sample.csv"):
    df = pd.read_csv(path, parse_dates=["snapshot_date"])
    return df

def summarize_usage(df):
    print("Overall usage (GB):")
    print(df["usage_gb"].describe())
    monthly = df.set_index("snapshot_date").resample("M").usage_gb.sum().reset_index()
    print("\nMonthly usage totals:")
    print(monthly.head())
    return monthly

def high_usage_accounts(df, threshold=1000):
    high = df[df["usage_gb"] > threshold].sort_values("usage_gb", ascending=False)
    return high[["account_id","service","usage_gb","cost_usd"]]

if __name__ == "__main__":
    df = load_data("storage_data_sample.csv")
    monthly = summarize_usage(df)
    high = high_usage_accounts(df)
    print("\nHigh usage accounts (sample):")
    print(high.head())
    df.to_csv("storage_cleaned.csv", index=False)
    # TODO: Integrate GenAI API to generate natural-language summaries of 'monthly'
