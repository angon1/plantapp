import os

import pandas as pd

# from .db import PlantsLib


def camel_to_snake(s):
    return "".join(["_" + c.lower() if c.isupper() else c for c in s]).lstrip("_")


def get_datasets_dir():
    return os.getcwd() + "/datasets/"


def parse_plant_info_csv(filename="plant_info_clean.csv"):
    df = pd.read_csv(get_datasets_dir() + filename)
    df.columns = [camel_to_snake(column) for column in df.columns]
    df = df.fillna("")
    return df


def write_plant_lib_to_db(engine, df: pd.DataFrame):
    df.to_sql(name="plantsLibrary", con=engine, if_exists="replace")
