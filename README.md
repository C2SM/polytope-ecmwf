# polytope-ecmwf

## Instructions

On santis:

```bash
# Load uenv that contains python 3.13
uenv start --view=netcdf netcdf-tools/2025:v1

# Create virtual environment
python -m venv .venv

# Activate environment
source .venv/bin/activate

# Install dependency
pip install polytope
```

Afterwards, one can run the test script:

```bash
python polytope-test.py
```
