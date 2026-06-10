from pathlib import Path
from polytope.api import Client
import datetime
from getpass import getpass

# --- Ask the credentials
USER = input('Please insert your username: ')
print("And your password")
PASS = getpass()


home_directory = Path.home()
output_path = home_directory / "scratch" / "ecmwf-polytope" / "grib"
print(f"Output path: {output_path}")

c = Client(
    address="polytope-test.wcp.cscs.ch",
    username=USER,
    password=PASS,
)

years = ["2025"]
months = ["04", "05", "06"]
parameters = ["167", "134"]  # 167: 2m temperature, 134: surface pressure
file_name = "era5_1hr_2t_sp"

for year in years:
    Path.mkdir(output_path / year, parents=True, exist_ok=True)
    for month in months:
        if datetime.datetime(int(year), int(month), 1).month == 2:
            if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
                days_in_month = 29
                dates_key = f"{year}{month}01/{year}{month}02/{year}{month}03/{year}{month}04/{year}{month}05/{year}{month}06/{year}{month}07/{year}{month}08/{year}{month}09/{year}{month}10/{year}{month}11/{year}{month}12/{year}{month}13/{year}{month}14/{year}{month}15/{year}{month}16/{year}{month}17/{year}{month}18/{year}{month}19/{year}{month}20/{year}{month}21/{year}{month}22/{year}{month}23/{year}{month}24/{year}{month}25/{year}{month}26/{year}{month}27/{year}{month}28/{year}{month}29"
            else:
                days_in_month = 28
                dates_key = f"{year}{month}01/{year}{month}02/{year}{month}03/{year}{month}04/{year}{month}05/{year}{month}06/{year}{month}07/{year}{month}08/{year}{month}09/{year}{month}10/{year}{month}11/{year}{month}12/{year}{month}13/{year}{month}14/{year}{month}15/{year}{month}16/{year}{month}17/{year}{month}18/{year}{month}19/{year}{month}20/{year}{month}21/{year}{month}22/{year}{month}23/{year}{month}24/{year}{month}25/{year}{month}26/{year}{month}27/{year}{month}28"
        elif datetime.datetime(int(year), int(month), 1).month in [4, 6, 9, 11]:
            days_in_month = 30
            dates_key = f"{year}{month}01/{year}{month}02/{year}{month}03/{year}{month}04/{year}{month}05/{year}{month}06/{year}{month}07/{year}{month}08/{year}{month}09/{year}{month}10/{year}{month}11/{year}{month}12/{year}{month}13/{year}{month}14/{year}{month}15/{year}{month}16/{year}{month}17/{year}{month}18/{year}{month}19/{year}{month}20/{year}{month}21/{year}{month}22/{year}{month}23/{year}{month}24/{year}{month}25/{year}{month}26/{year}{month}27/{year}{month}28/{year}{month}29/{year}{month}30"
        else:
            days_in_month = 31
            dates_key = f"{year}{month}01/{year}{month}02/{year}{month}03/{year}{month}04/{year}{month}05/{year}{month}06/{year}{month}07/{year}{month}08/{year}{month}09/{year}{month}10/{year}{month}11/{year}{month}12/{year}{month}13/{year}{month}14/{year}{month}15/{year}{month}16/{year}{month}17/{year}{month}18/{year}{month}19/{year}{month}20/{year}{month}21/{year}{month}22/{year}{month}23/{year}{month}24/{year}{month}25/{year}{month}26/{year}{month}27/{year}{month}28/{year}{month}29/{year}{month}30/{year}{month}31"

        target= f"{str(output_path)}/{year}/{file_name}-{year}{month}.grib"

        collection = "mars"
        request = {
            "class": "ea",
            "type": "an",
            "stream": "oper",
            "expver": "0001",
            "repres": "sh",
            "levtype": "sfc",
            "param": parameters,
            "date": dates_key,
            "time": "0000/0100/0200/0300/0400/0500/0600/0700/0800/0900/1000/1100/1200/1300/1400/1500/1600/1700/1800/1900/2000/2100/2200/2300",
            "step": "00",
            "domain": "g",
            "target": target,
            "resol": "auto",
            "grid": "0.25/0.25",
        }

        r = c.retrieve(collection, request, target)

