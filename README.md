# WHOI-PO-HPC
This repository will contain all relevant information related to using parallel and distributed computing on the Poseidon cluster at the Woods Hole Oceanographic Institution (WHOI). This repository will specifically go over Dask, xarray and requesting resources on Poseidon and your local machine. Below is a README that I asked ChatGPT to generate for me, we can change it later but I was lazy. 

# Parallel and Distributed Computing on the Poseidon Cluster at WHOI

Welcome to the repository for all relevant information related to using parallel and distributed computing on the Poseidon cluster at the Woods Hole Oceanographic Institution (WHOI). This repository will specifically cover the following topics:

- Using Dask for parallel computing
- Leveraging xarray for handling multi-dimensional arrays
- Requesting resources on the Poseidon cluster
- Setting up your local machine for compatibility with Poseidon

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Using Dask](#using-dask)
- [Working with xarray](#working-with-xarray)
- [Requesting Resources on Poseidon](#requesting-resources-on-poseidon)
- [Setting Up Your Local Machine](#setting-up-your-local-machine)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This repository contains comprehensive information on utilizing parallel and distributed computing resources on the Poseidon cluster at WHOI. The primary focus is on using Dask for parallel computing, leveraging xarray for managing multi-dimensional arrays, and efficiently requesting resources on both the Poseidon cluster and your local machine.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:
- You have a WHOI Poseidon cluster account.
- You have Python installed on your local machine.
- You have basic knowledge of parallel and distributed computing concepts.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/poseidon-cluster-guide.git
    ```
2. Navigate to the project directory:
    ```bash
    cd poseidon-cluster-guide
    ```
3. Install the required Python packages:
   Using ```pip```
    ```bash
    pip install -r requirements.txt
    ```
    or ```conda```
    ```bash
    conda env create -f environment.yml
    ```

## Using Dask

[Dask](https://dask.org/) is a flexible parallel computing library for analytics. It helps scale the Python ecosystem (numpy, pandas, scikit-learn, etc.) and enables execution on multi-core machines and distributed clusters.

- [Dask Documentation](https://docs.dask.org/en/latest/)
- Examples and tutorials: [examples/](examples/)

## Working with xarray

[xarray](http://xarray.pydata.org/en/stable/) is an open-source project and Python package that makes working with labeled multi-dimensional arrays simple, efficient, and fun!

- [xarray Documentation](http://xarray.pydata.org/en/stable/)
- Examples and tutorials: [examples/](examples/)

## Requesting Resources on Poseidon

Learn how to request and manage computing resources on the Poseidon cluster effectively:
- [Poseidon User Guide](https://www.whoi.edu/page.do?pid=23491)
- Examples of job scripts: [scripts/](scripts/)

## Setting Up Your Local Machine

To ensure your local machine can interact with Poseidon:
- Install the necessary SSH tools.
- Set up environment modules for consistency with the cluster environment.

## Contributing

Contributions are welcome! Please read the [contributing guide](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact the repository maintainer at [your-email@whoi.edu](mailto:your-email@whoi.edu).
