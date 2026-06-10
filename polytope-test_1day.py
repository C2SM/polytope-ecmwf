from polytope.api import Client
import datetime
from getpass import getpass
from pathlib import Path
import os

from cdo import Cdo
cdo = Cdo()

# --- Ask the credentials
USER = input('Please insert your username: ')
print("And your password")
PASS = getpass()


c = Client(
    address="polytope-test.wcp.cscs.ch",
    username=USER,
    password=PASS,
)

home_directory = Path.home()
output_path = home_directory / "scratch" / "ecmwf-polytope" / "grib"
print(f"Output path: {output_path}")

date = "20250102"
parameter = "167"  # 167: 2m temperature
shortName = "2t"

target = f"{str(output_path)}/era5_{shortName}_{date}"

collection = "mars"
request = {
    "class": "ea",
    "type": "an",
    "stream": "oper",
    "expver": "0001",
    "repres": "sh",
    "levtype": "sfc",
    "param": parameter,
    "date": date,
    "time": "0000/0100/0200/0300/0400/0500/0600/0700/0800/0900/1000/1100/1200/1300/1400/1500/1600/1700/1800/1900/2000/2100/2200/2300",
    "step": "00",
    "domain": "g",
    "target": f"{target}.grib",
    "resol": "auto",
    "grid": "0.25/0.25",
}

r = c.retrieve(collection, request, f"{target}.grib")

cdo.copy(options =  "-f nc4 sorttaxis", input=f"{target}.grib",
        output=f"{target}.nc")
os.remove(f"{target}.grib")  # uncomment to remove the intermediate GRIB file