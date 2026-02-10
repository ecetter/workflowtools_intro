#!/usr/bin/env python3
"""Summarize transformed CSV: write count, mean, std to output file. Reads input path, writes output path."""
import sys
import pandas as pd

def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    df = pd.read_csv(input_path)
    s = df["value"].describe()
    with open(output_path, "w") as f:
        f.write("count\t" + str(s["count"]) + "\n")
        f.write("mean\t" + str(round(s["mean"], 2)) + "\n")
        f.write("std\t" + str(round(s["std"], 2)) + "\n")

if __name__ == "__main__":
    main()
