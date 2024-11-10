import singer
import pandas as pd
import numpy as np

LOGGER = singer.get_logger()


def fetch_launches():
    url = "https://api.spacexdata.com/v4/launches"
    df = pd.read_json(url)

    schema = {
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "rocket": {"type": "string"},
            "success": {"type": ["number", "null"]},
            "date_utc": {"type": "string", "format": "date-time"},
        }
    }

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    records = df.to_dict(orient="records")

    singer.write_schema("launches", schema, "id")
    singer.write_records("launches", records)

def fetch_rockets():
    url = "https://api.spacexdata.com/v4/rockets"
    df = pd.read_json(url)

    schema = {
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "active": {"type": "boolean"},
        }
    }

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    records = df.to_dict(orient="records")

    singer.write_schema("rockets", schema, "id")
    singer.write_records("rockets", records)

def main():
    fetch_launches()
    fetch_rockets()

if __name__ == "__main__":
    main()
