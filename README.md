# Python MACCOR example
This is an example script for reading a [MACCOR](http://www.maccor.com/Products/Software.aspx) file using the Python programming language using the [battery-data-toolkit](https://github.com/materials-data-facility/battery-data-toolkit).

This script is based on this example: [test_maccor.py](https://github.com/materials-data-facility/battery-data-toolkit/blob/master/scripts/CAMP/test_maccor.py)

The main class used is [`MACCORExtractor`](https://github.com/materials-data-facility/battery-data-toolkit/blob/master/batdata/extractors/maccor.py).

# Installation

Create a Python virtual environment with the following dependencies:

* [battery-data-toolkit](https://pypi.org/project/battery-data-toolkit/)

This may done using the environment manager of your choice. Please see guidance below.

## Conda

Using the [Conda](https://docs.conda.io/en/latest/) environment manager:

```bash
conda env --name my_maccor_env --file environment.yaml
conda activate my_maccor_env
```

## Venv

[venv](https://docs.python.org/3/library/venv.html) Creation of virtual environments

```bash
python -m venv ./my_maccor_env
./my_maccor_env/bin/activate
pip install battery-data-toolkit
```

# Usage

To view the usage instructions:

```bash
python maccor-example.py --help
```

To run the script, specify a target directory that contains MACCOR files using the `--path` option:

```bash
python maccor-example.py --path ./maccor_files
```

