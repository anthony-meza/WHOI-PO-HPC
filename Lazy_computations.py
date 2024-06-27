# Lazy Computations with Dask and xarray

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

# Understanding Lazy Computations
# Dask arrays and xarray objects support lazy computation, meaning that operations on these objects are not executed immediately. Instead, they build up a task graph that can be computed later.
# Extract the air temperature (Tair) data variable
tair = ds.Tair
print(tair)

# Performing Lazy Computations
# Let's perform a lazy computation by calculating the mean air temperature over time. Note that this computation is lazy and will not be executed until we explicitly ask for the result.
# Calculate the mean air temperature over time (lazy computation)
mean_tair = tair.mean(dim='time')
print(mean_tair)

# Executing Lazy Computations
# To execute the lazy computation and get the actual result, we need to call the `compute()` method.
# Execute the lazy computation to get the result
mean_tair_computed = mean_tair.compute()
print(mean_tair_computed)
