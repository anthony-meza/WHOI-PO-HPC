## Download

Miniforge installers are available here: https://github.com/conda-forge/miniforge/releases

#### Miniforge3

Latest installers with Python 3.10 `(*)` in the base environment:

| OS      | Architecture          | Download  |
| --------|-----------------------|-----------|
| Linux   | x86_64 (amd64)        | [Miniforge3-Linux-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh) |
| Linux   | aarch64 (arm64) `(**)` | [Miniforge3-Linux-aarch64](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh) |
| Linux   | ppc64le (POWER8/9)    | [Miniforge3-Linux-ppc64le](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-ppc64le.sh) |
| OS X    | x86_64                | [Miniforge3-MacOSX-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh) |
| OS X    | arm64 (Apple Silicon) `(***)` | [Miniforge3-MacOSX-arm64](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh) |
| Windows | x86_64                | [Miniforge3-Windows-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) |

`(*)` The Python version is specific only to the base environment. Conda can create new environments with different Python versions and implementations.

`(**)` For Raspberry PI that include a 64 bit processor, you must also use
a 64-bit operating system such as
[Raspberry Pi OS 64-bit](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-64-bit)
or
[Ubuntu for Raspberry PI](https://ubuntu.com/raspberry-pi).
The versions listed as "System: 32-bit" are not compatible with the installers on this website.

`(***)` Apple silicon builds are experimental and haven't had testing like the other platforms.

#### Miniforge-pypy3

Latest installers with PyPy 3.9 in the base environment:

| OS      | Architecture          | Download  |
| --------|-----------------------|-----------|
| Linux   | x86_64 (amd64)        | [Miniforge-pypy3-Linux-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge-pypy3-Linux-x86_64.sh) |
| Linux   | aarch64 (arm64)       | [Miniforge-pypy3-Linux-aarch64](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge-pypy3-Linux-aarch64.sh) |
| Linux   | ppc64le (POWER8/9)    | [Miniforge-pypy3-Linux-ppc64le](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge-pypy3-Linux-ppc64le.sh) |
| OS X    | x86_64                | [Miniforge-pypy3-MacOSX-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge-pypy3-MacOSX-x86_64.sh) |
| Windows | x86_64                | [Miniforge-pypy3-Windows-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge-pypy3-Windows-x86_64.exe) |

<details><summary>Mambaforge (Discouraged as of September 2023)</summary>

With the [release](https://github.com/conda-forge/miniforge/releases/tag/23.3.1-0) of
`Miniforge3-23.3.1-0`, that incorporated the changes in
[#277](https://github.com/conda-forge/miniforge/pull/277), the packages and
configuration of `Mambaforge` and `Miniforge3` are now **identical**. The
only difference between the two is the name of the installer and, subsequently,
the default installation directory.

Given its wide usage, there are no plans to deprecate Mambaforge. If at some
point we decide to deprecate Mambaforge, it will be appropriately announced and
communicated with sufficient time in advance.

As of September 2023, the new usage of Mambaforge is thus discouraged. Bug
reports specific to Mambaforge will be closed as won't fix.

#### Mambaforge

Latest installers with Mamba in the base environment:


| OS      | Architecture          | Download  |
| --------|-----------------------|-----------|
| Linux   | x86_64 (amd64)        | [Mambaforge-Linux-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh) |
| Linux   | aarch64 (arm64)       | [Mambaforge-Linux-aarch64](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-aarch64.sh) |
| Linux   | ppc64le (POWER8/9)    | [Mambaforge-Linux-ppc64le](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-ppc64le.sh) |
| OS X    | x86_64                | [Mambaforge-MacOSX-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-MacOSX-x86_64.sh) |
| OS X    | arm64 (Apple Silicon) | [Mambaforge-MacOSX-arm64](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-MacOSX-arm64.sh) |
| Windows | x86_64                | [Mambaforge-Windows-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Windows-x86_64.exe) |

#### Mambaforge-pypy3

Latest installers with Mamba and PyPy in the base environment:

| OS      | Architecture          | Download  |
| --------|-----------------------|-----------|
| Linux   | x86_64 (amd64)        | [Mambaforge-pypy3-Linux-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-pypy3-Linux-x86_64.sh) |
| Linux   | aarch64 (arm64)       | [Mambaforge-pypy3-Linux-aarch64](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-pypy3-Linux-aarch64.sh) |
| Linux   | ppc64le (POWER8/9)    | [Mambaforge-pypy3-Linux-ppc64le](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-pypy3-Linux-ppc64le.sh) |
| OS X    | x86_64                | [Mambaforge-pypy3-MacOSX-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-pypy3-MacOSX-x86_64.sh) |
| Windows | x86_64                | [Mambaforge-pypy3-Windows-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-pypy3-Windows-x86_64.exe) |

</details>

## Install

### Unix-like platforms (Mac OS & Linux)

Download the installer using curl or wget or your favorite program and run the script.
For eg:

    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash Miniforge3-$(uname)-$(uname -m).sh

or

    wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash Miniforge3-$(uname)-$(uname -m).sh
