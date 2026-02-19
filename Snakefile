# Simple Snakemake demo: CSV -> multiple processing stages -> plot.


rule all:
    input:
        "results/plot.png",
        "results/summary.txt"


# 
# Stage 1: validate and clean input CSV (drop empty rows, ensure numeric value)
#

rule clean:
    input:
        "data/input.csv"
    output:
        "data/cleaned.csv"
    log:
        "logs/clean.log"
    shell:
        "python scripts/clean.py {input[0]} {output[0]} 2> {log}"


# 
# Stage 2: transform (add normalized value 0-1 and rank)
#          NOTE: This stage, perhaps, has the most doing to do, so we can overwrite the default runtime value to give it more time to do its thing.
# 

rule transform:
    input:
        "data/cleaned.csv"
    output:
        "results/transformed.csv"
    resources:
        runtime=15
    benchmark:
        "benchmarks/transform.txt"
    log:
        "logs/transform.log"
    shell:
        "python scripts/transform.py {input[0]} {output[0]} 2> {log}"


# 
# Stage 3: summarize (optional summary stats)
#

rule summarize:
    input:
        "results/transformed.csv"
    output:
        "results/summary.txt"
    log:
        "logs/summary.log"
    shell:
        "python scripts/summarize.py {input[0]} {output[0]} 2> {log}"

# 
# Stage 4: plot (bar chart of category vs value)
# 

rule plot:
    input:
        "results/transformed.csv"
    output:
        "results/plot.png",
        "results/plot_unsorted.png"
    log:
        "logs/plot.log"
    shell:
        "python scripts/plot.py {input[0]} {output[0]} {output[1]} 2> {log}"

