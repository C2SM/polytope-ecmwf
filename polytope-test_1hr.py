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

target="era5.2t.202501010000.grib"

collection = "mars"
request = {
    "class": "ea",
    "type": "an",
    "stream": "oper",
    "expver": "0001",
    "repres": "sh",
    "levtype": "sfc",
    "param": "167",
    "date": "20250101",
    "time": "0000",
    "step": "00",
    "domain": "g",
    "target": target,
    "resol": "auto",
    "grid": "0.25/0.25",
}

r = c.retrieve(collection, request, target)
print(r[0].describe())
#r[0].download()

