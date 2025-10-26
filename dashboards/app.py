import streamlit as st, pandas as pd

st.set_page_config(page_title="Customer Analytics & Recs", layout="wide")
st.title("🛍️ Customer Analytics & Recommendation Platform")

seg = pd.read_csv("data/processed/kpi_by_segment.csv")
cat = pd.read_csv("data/processed/kpi_by_category.csv")
top = pd.read_csv("data/processed/top_products.csv")

c1, c2 = st.columns(2)
with c1:
    st.subheader("Revenue by Segment")
    st.bar_chart(seg.set_index("segment")["revenue"])
with c2:
    st.subheader("Revenue by Category")
    st.bar_chart(cat.set_index("category")["revenue"])

st.subheader("Top Products (by revenue)")
st.dataframe(top.head(5), use_container_width=True)
st.caption("Demo data. Extend with model-based recommendations later.")
