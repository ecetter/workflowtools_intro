#!/bin/bash

# remove output files
snakemake --delete-all-output

# remove logs
rm logs/*.log

# remove snakmake hidden directory to start fresh
rm -rf .snakemake
