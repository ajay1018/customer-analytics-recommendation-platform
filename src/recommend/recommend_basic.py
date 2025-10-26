from pathlib import Path
import pandas as pd, json

PROC = Path("data/processed")
enriched = pd.read_csv(PROC/"events_enriched.csv")

# Popularity-based recommenders
pop_by_product = (enriched.groupby("product_id", as_index=False)["revenue"].sum()
                  .sort_values("revenue", ascending=False))
pop_by_category = (enriched.groupby("category", as_index=False)["revenue"].sum()
                   .sort_values("revenue", ascending=False))

# Segment-affinity: top category per segment
seg_cat = (enriched.groupby(["segment","category"], as_index=False)["revenue"].sum())
top_cat_per_segment = (seg_cat.sort_values(["segment","revenue"], ascending=[True,False])
                            .groupby("segment").head(1).reset_index(drop=True))

# Export JSONs for quick consumption
(PROC/"recommendations").mkdir(parents=True, exist_ok=True)
pop_by_product.head(5).to_json(PROC/"recommendations/top_products.json", orient="records", indent=2)
pop_by_category.head(5).to_json(PROC/"recommendations/top_categories.json", orient="records", indent=2)
top_cat_per_segment.to_json(PROC/"recommendations/top_category_per_segment.json", orient="records", indent=2)

print("[recommend] wrote top_products/top_categories/top_category_per_segment")
