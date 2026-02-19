# A simple Snakemake demo

A minimal pipeline: one input CSV, several processing steps, and a plot.


## Input

`data/input.csv` is a small table with columns `category` and `value`.


## Pipeline

1. **clean** (`scripts/clean.py`) :  Read `data/input.csv`, drop any nulls, and ensure `value` entries are numeric. Produces `data/cleaned.csv` as the clean dataset.
2. **transform** (`scripts/transform.py`) : Add column to insert normalized value and another column to add the rank. Produces `results/transformed.csv` as the result.
3. **summarize** (`scripts/summarize.py`) : Write summary stats to `results/summary.txt` file.
4. **plot** (`scripts/plot.py`) : Create bar chart of category vs value as `results/plot.png` and `results/plot_unsorted.png` image files.

Each step is implemented in a Python script under `scripts/`; the Snakefile invokes them with input and output paths taken as input arguments.


## Setup

`init/setup.sh` contains the steps to set up a conda environment that contains `python`, `snakemake`, and any dependencies for this pipeline. Please note that the setup is specifically configured for the Roar Collab cluster. To run on other clusters, some minor modifications must be made.


## Run

From **this directory** (`workflowtools_intro/`):

**Local:**

```bash
snakemake -j 1
```

**Local with a profile:** The `profiles/local/config.yaml` file sets some defaults to limit the resources used the snakemake jobs.

```bash
snakemake --profile profiles/local
```


**Slurm:** The `profiles/slurm/config.yaml` file sets slurm-specific settings that enable snakemake to submit jobs via `sbatch`.

```bash
snakemake --profile profiles/slurm
```


## Reset

`init/reset.sh` removes all outputs and puts the repo back to a clean state after a snakemake run. Run with the following:

```bash
./init/reset.sh
```


## Outputs

- `data/cleaned.csv`
- `results/transformed.csv`
- `results/summary.txt`
- `results/plot.png`
