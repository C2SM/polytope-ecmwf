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

collection = "mars"
request = {
    "class": "ea",
    "type": "an",
    "stream": "oper",
    "expver": "0001",
    "repres": "sh",
    "levtype": "sfc",
    "param": "167",
    "date": "20250101/20250102/20250103/20250104/20250105/20250106/20250107/20250108/20250109/20250110/20250111/20250112/20250113/20250114/20250115/20250116/20250117/20250118/20250119/20250120/20250121/20250122/20250123/20250124/20250125/20250126/20250127/20250128/20250129/20250130/20250131",
    "time": "0000/0100/0200/0300/0400/0500/0600/0700/0800/0900/1000/1100/1200/1300/1400/1500/1600/1700/1800/1900/2000/2100/2200/2300",
    "step": "00",
    "domain": "g",
    "target": "era5.2t.202501.data",
    "resol": "auto",
    "grid": "0.25/0.25",
}

print(c.retrieve(collection, request, pointer=False))


