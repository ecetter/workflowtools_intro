#!/usr/bin/env python3
"""Transform cleaned CSV: add normalized value (0-1) and rank. Reads input path, writes output path."""
import sys
import pandas as pd

def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    df = pd.read_csv(input_path)
    df["value_norm"] = (df["value"] - df["value"].min()) / (
        df["value"].max() - df["value"].min() + 1e-9
    )
    df["rank"] = df["value"].rank(ascending=False).astype(int)
    df.to_csv(output_path, index=False)
    print("transformed", len(df), "rows", file=sys.stderr)

if __name__ == "__main__":
    main()
