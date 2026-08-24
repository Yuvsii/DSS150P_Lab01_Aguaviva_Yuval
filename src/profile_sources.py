from pathlib import Path
import pandas as pd
import os

RAW = Path("data/raw")

def profile_dataframe(name, df, file_path):
    print(f"\n=== {name} ===")
    print(f"File size: {os.path.getsize(file_path) / 1024:.2f} KB")
    print("shape:", df.shape)
    print("columns:", list(df.columns))
    print("dtypes:\n", df.dtypes)
    print("nulls:\n", df.isna().sum())
    
    # Safe duplicate check for nested JSON/dicts
    try:
        print("duplicate rows:", df.duplicated().sum())
    except TypeError:
        print("duplicate rows:", df.astype(str).duplicated().sum())
    
    print("distinct values:")
    for col in df.columns:
        try:
            print(f"  {col}: {df[col].nunique()}")
        except TypeError:
            print(f"  {col}: {df[col].astype(str).nunique()}")
        
    print("head:\n", df.head())
    
    # Numeric Min/Max
    numeric_cols = df.select_dtypes(include='number').columns
    if not numeric_cols.empty:
        print("numeric ranges:")
        for col in numeric_cols:
            print(f"  {col}: Min = {df[col].min()}, Max = {df[col].max()}")
            
    # Date ranges
    print("date ranges:")
    for col in df.columns:
        if 'date' in col.lower() or 'time' in col.lower():
            try:
                parsed_dates = pd.to_datetime(df[col])
                print(f"  {col}: Earliest = {parsed_dates.min()}, Latest = {parsed_dates.max()}")
            except Exception:
                pass

# Load the files
customers = pd.read_csv(RAW / "customers.csv")
orders = pd.read_json(RAW / "orders.json")
products = pd.read_parquet(RAW / "products.parquet")

for name, df in {
    "customers.csv": customers,
    "orders.json": orders,
    "products.parquet": products,
}.items():
    file_path = RAW / name
    profile_dataframe(name, df, file_path)