#!/usr/bin/env python3
"""Plot bar chart of category vs value. Reads input path, writes output path(s).
   Creates: (1) plot sorted by value, (2) plot in original row order."""
import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def make_bar_plot(ax, df, title_suffix=""):
    """Draw horizontal bar chart of category vs value on ax."""
    ax.barh(df["category"], df["value"], color="steelblue", edgecolor="black")
    ax.set_xlabel("Value")
    ax.set_ylabel("Category")
    ax.set_title("Simple demo: category vs value" + title_suffix)
    plt.tight_layout()


def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    # Optional: second output path for unsorted plot (default: same dir, _by_order suffix)
    if len(sys.argv) >= 4:
        output_path_unsorted = sys.argv[3]
    else:
        base = output_path.rsplit(".", 1)
        output_path_unsorted = (base[0] + "_by_order." + base[1]) if len(base) == 2 else (output_path + "_by_order")

    df = pd.read_csv(input_path)

    # Plot 1: sorted by value (original behavior)
    df_sorted = df.sort_values("value")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    make_bar_plot(ax1, df_sorted, " (sorted by value)")
    plt.savefig(output_path, dpi=100)
    plt.close()
    print("saved plot (sorted)", output_path, file=sys.stderr)

    # Plot 2: original order (no sort)
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    make_bar_plot(ax2, df, " (original order)")
    plt.savefig(output_path_unsorted, dpi=100)
    plt.close()
    print("saved plot (original order)", output_path_unsorted, file=sys.stderr)


if __name__ == "__main__":
    main()
