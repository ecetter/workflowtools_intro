# Simple Snakemake demo

A minimal pipeline: one input CSV, several processing steps, and a plot.

## Pipeline

1. **clean** — Read `data/input.csv`, drop nulls, ensure numeric `value` → `data/cleaned.csv` (`scripts/clean.py`)
2. **transform** — Add normalized value and rank → `results/transformed.csv` (`scripts/transform.py`)
3. **summarize** — Write summary stats → `results/summary.txt` (`scripts/summarize.py`)
4. **plot** — Bar chart of category vs value → `results/plot.png` (`scripts/plot.py`)

Each step is implemented in a Python script under `scripts/`; the Snakefile invokes them with input and output paths.

## Input

`data/input.csv` is a small table with columns `category` and `value` (included in this directory).

## Run

From **this directory** (`demo_snakemake/`):

**Local:**
```bash
mkdir -p logs
snakemake -j1
```

**SLURM:** Edit `config/slurm.yaml` and set `slurm_account` and `slurm_partition` under `default_resources`. Then run:

```bash
mkdir -p logs
snakemake --executor slurm -j 4
```

No `--default-resources` is needed; the Snakefile loads `config/slurm.yaml` and uses its `default_resources` for the SLURM executor.

## Outputs

- `data/cleaned.csv`
- `results/transformed.csv`
- `results/summary.txt`
- `results/plot.png`
