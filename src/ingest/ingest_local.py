from pathlib import Path
for f in ["customers.csv","products.csv","transactions.csv"]:
    p = Path("data/raw")/f
    assert p.exists(), f"Missing data/raw/{f}"
    print("[ingest] found", p, "size=", p.stat().st_size, "bytes")
