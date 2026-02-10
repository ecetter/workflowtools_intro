# Simple Snakemake demo: CSV -> multiple processing stages -> plot.
# Run from this directory:
#   Local:  snakemake -j1
#   SLURM:  edit config/slurm.yaml (account, partition), then:
#           snakemake --executor slurm -j 4
#           (account and partition are read from config/slurm.yaml below)

configfile: "config/slurm.yaml"

# SLURM executor: default_resources are read from config/slurm.yaml only.
default_resources: config.get("default_resources", {})

rule all:
    input:
        "results/plot.png",
        "results/summary.txt"

# Stage 1: validate and clean input CSV (drop empty rows, ensure numeric value)
rule clean:
    input:
        "data/input.csv"
    output:
        "data/cleaned.csv"
    log:
        "logs/clean.log"
    shell:
        "python scripts/clean.py {input[0]} {output[0]} 2> {log}"

# Stage 2: transform (add normalized value 0-1 and rank)
rule transform:
    input:
        "data/cleaned.csv"
    output:
        "results/transformed.csv"
    log:
        "logs/transform.log"
    shell:
        "python scripts/transform.py {input[0]} {output[0]} 2> {log}"

# Stage 3: summarize (optional summary stats)
rule summarize:
    input:
        "results/transformed.csv"
    output:
        "results/summary.txt"
    log:
        "logs/summary.log"
    shell:
        "python scripts/summarize.py {input[0]} {output[0]} 2> {log}"

# Stage 4: plot (bar chart of category vs value)
rule plot:
    input:
        "results/transformed.csv"
    output:
        "results/plot.png"
    log:
        "logs/plot.log"
    shell:
        "python scripts/plot.py {input[0]} {output[0]} 2> {log}"

