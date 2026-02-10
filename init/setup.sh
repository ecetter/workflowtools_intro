#!/bin/bash

# load anaconda from software stack
module load anaconda/2023
module list

# create environment that contains snakemake and its dependencies
conda create -y -n workflow_env
conda activate workflow_env
conda install -y snakemake snakemake-executor-plugin-slurm
