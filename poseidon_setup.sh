#!/bin/bash

module load mambaforge 

mamba install -y --name "test_enviornment" -c conda-forge numpy pandas ipykernel pip-tools fastapi jupyterlab copernicusmarine


