#!/usr/bin/env python3
"""Plot bar chart of category vs value. Reads input path, writes output path."""
import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    df = pd.read_csv(input_path)
    df = df.sort_values("value")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(df["category"], df["value"], color="steelblue", edgecolor="black")
    ax.set_xlabel("Value")
    ax.set_ylabel("Category")
    ax.set_title("Simple demo: category vs value")
    plt.tight_layout()
    plt.savefig(output_path, dpi=100)
    plt.close()
    print("saved plot", file=sys.stderr)

if __name__ == "__main__":
    main()
