# Python MACCOR example
This is an example script for reading a MACCOR file using the Python programming language using the [battery-data-toolkit](https://github.com/materials-data-facility/battery-data-toolkit).

This script is based on this example: [test_maccor.py](https://github.com/materials-data-facility/battery-data-toolkit/blob/master/scripts/CAMP/test_maccor.py)

The main class used is [`MACCORExtractor`](https://github.com/materials-data-facility/battery-data-toolkit/blob/master/batdata/extractors/maccor.py).

# Installation

Create a Python virtual environment with the following dependencies:

* [battery-data-toolkit](https://pypi.org/project/battery-data-toolkit/)

## Conda

Using the Conda environment manager:

```bash
conda env --name my_maccor_env --file environment.yaml
conda activate my_maccor_env
```

# Usage

To run the script:

```bash
python maccor-example.py
```

