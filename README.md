# polytope-ecmwf
This repository holds example scripts to use polytope and the ECMWF-DataCube on AlpsB.

You need a username and password for polytope.

The script polytope-test_1month.py is an example on how to retrieve monthly data for two variables (2m temperature and surface pressure) at the same time.

Retreived data will be saved to scratch if you have a symbolic link to your $SCRATCH folder in your $HOME.
This can be done by issuing the following command in a terminal from your $HOME directory:

ln -s $SCRATCH $HOME/scratch

If you do not have this set-up data will end up in your $HOME.

## Instructions

On santis:

```bash
# Load uenv that contains python 3.13
uenv start --view=climtools climtools/25.2:v1

# Create virtual environment
python -m venv .venv

# Activate environment
source .venv/bin/activate

# Install dependencies
pip install polytope-client
```

Afterwards, one can run the test script:

```bash
python polytope-test.py
```