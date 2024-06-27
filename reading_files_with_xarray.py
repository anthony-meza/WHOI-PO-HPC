# Basic Tutorial: Using Dask and xarray on Poseidon

# Prerequisites
# Ensure you have activated the Conda environment:
# conda activate poseidon-cluster-env

# Importing Libraries
import dask.array as da
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# Loading a NetCDF File with xarray
# Let's load a sample NetCDF file using xarray. For this example, we'll use a sample dataset from xarray.
ds = xr.tutorial.open_dataset('rasm')

# Exploring the Dataset
# We can explore the contents of the dataset to understand its structure and variables.
print(ds)

# Visualizing the Data
# Let's plot the air temperature (Tair) for the first time step.
# Select the first time step
tair = ds.Tair.isel(time=0)

# Plot the data
tair.plot(cmap='viridis')
plt.title('Air Temperature at First Time Step')
plt.show()
