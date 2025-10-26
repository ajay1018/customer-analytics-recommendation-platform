from pathlib import Path
import pandas as pd

RAW = Path("data/raw")
PROC = Path("data/processed"); PROC.mkdir(parents=True, exist_ok=True)

customers = pd.read_csv(RAW/"customers.csv", parse_dates=["signup_date"])
products  = pd.read_csv(RAW/"products.csv")
txns      = pd.read_csv(RAW/"transactions.csv", parse_dates=["ts"])

df = txns.merge(products, on="product_id", how="left").merge(customers, on="customer_id", how="left")
df["revenue"] = df["qty"] * df["price"]

# KPIs
kpi_overall = pd.DataFrame({
    "customers":[df["customer_id"].nunique()],
    "transactions":[len(df)],
    "revenue":[df["revenue"].sum()]
})
kpi_by_segment = df.groupby("segment", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
kpi_by_category = df.groupby("category", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
top_products = df.groupby(["product_id","category"], as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)

# Write outputs
df.to_csv(PROC/"events_enriched.csv", index=False)
kpi_overall.to_csv(PROC/"kpi_overall.csv", index=False)
kpi_by_segment.to_csv(PROC/"kpi_by_segment.csv", index=False)
kpi_by_category.to_csv(PROC/"kpi_by_category.csv", index=False)
top_products.to_csv(PROC/"top_products.csv", index=False)
print("[transform] wrote:", PROC/"events_enriched.csv")
