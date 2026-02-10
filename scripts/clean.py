#!/usr/bin/env python3
"""Clean input CSV: drop nulls, ensure numeric value. Reads input path, writes output path."""
import sys
import pandas as pd

def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    df = pd.read_csv(input_path)
    df = df.dropna()
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value"])
    df.to_csv(output_path, index=False)
    print(len(df), "rows", file=sys.stderr)

if __name__ == "__main__":
    main()
