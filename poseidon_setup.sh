#!/bin/bash

curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh

mamba install -y --name "test_enviornment" -c conda-forge numpy pandas ipykernel pip-tools fastapi jupyterlab copernicusmarine
