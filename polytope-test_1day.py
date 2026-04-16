from polytope.api import Client
import datetime
from getpass import getpass
import os

#from cdo import Cdo
#cdo = Cdo()

# --- Ask the credentials
USER = input('Please insert your username: ')
print("And your password")
PASS = getpass()


c = Client(
    address="polytope-test.wcp.cscs.ch",
    username=USER,
    password=PASS,
)

target="/capstor/scratch/cscs/rlorenz/ecmwf-polytope/grib/era5.2t.20250102"

collection = "mars"
request = {
    "class": "ea",
    "type": "an",
    "stream": "oper",
    "expver": "0001",
    "repres": "sh",
    "levtype": "sfc",
    "param": "167",
    "date": "20250102",
    "time": "0000/0100/0200/0300/0400/0500/0600/0700/0800/0900/1000/1100/1200/1300/1400/1500/1600/1700/1800/1900/2000/2100/2200/2300",
    "step": "00",
    "domain": "g",
    "target": f"{target}.grib",
    "resol": "auto",
    "grid": "0.25/0.25",
}

r = c.retrieve(collection, request, f"{target}.grib")

#cdo.copy("-f nc", input=f"{target}.grib",
#        output=f"{target}.nc")
#os.remove(f"{target}.grib")  # uncomment to remove the intermediate GRIB file