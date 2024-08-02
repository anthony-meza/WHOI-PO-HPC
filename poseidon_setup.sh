#!/bin/bash

module load mambaforge 

mamba create --name "test_enviornment" python=3.9
mamba install -y --name "test_enviornment" -c conda-forge numpy pandas ipykernel pip-tools fastapi jupyterlab copernicusmarine


