from polytope.api import Client
import datetime
from getpass import getpass

# --- Ask the credentials
USER = input('Please insert your username: ')
print("And your password")
PASS = getpass()


c = Client(
    address="polytope-test.wcp.cscs.ch",
    username=USER,
    password=PASS,
)

year = "2025"
month = "03"
dates_key = f"{year}{month}01/{year}{month}02/{year}{month}03/{year}{month}04/{year}{month}05/{year}{month}06/{year}{month}07/{year}{month}08/{year}{month}09/{year}{month}10/{year}{month}11/{year}{month}12/{year}{month}13/{year}{month}14/{year}{month}15/{year}{month}16/{year}{month}17/{year}{month}18/{year}{month}19/{year}{month}20/{year}{month}21/{year}{month}22/{year}{month}23/{year}{month}24/{year}{month}25/{year}{month}26/{year}{month}27/{year}{month}28"
target=f"/capstor/scratch/cscs/rlorenz/ecmwf-polytope/grib/era5.2t.sp.{year}{month}.grib"

collection = "mars"
request = {
    "class": "ea",
    "type": "an",
    "stream": "oper",
    "expver": "0001",
    "repres": "sh",
    "levtype": "sfc",
    "param": ["167", "134"],
    "date": dates_key,
    "time": "0000/0100/0200/0300/0400/0500/0600/0700/0800/0900/1000/1100/1200/1300/1400/1500/1600/1700/1800/1900/2000/2100/2200/2300",
    "step": "00",
    "domain": "g",
    "target": target,
    "resol": "auto",
    "grid": "0.25/0.25",
}

r = c.retrieve(collection, request, target)


