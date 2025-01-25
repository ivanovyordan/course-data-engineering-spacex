import singer  # type: ignore
import pandas as pd
import numpy as np

LOGGER = singer.get_logger()


def get_api_url(endpoint: str) -> str:
    return f"https://api.spacexdata.com/v4/{endpoint}"


def fetch_launches() -> None:
    url: str = get_api_url("launches")
    df = pd.read_json(url)

    records = df.to_dict(orient="records")
    schema = {
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "rocket": {"type": "string"},
            "success": {"type": ["number", "null"]},
            "date_utc": {"type": "string", "format": "date-time"},
        }
    }

    singer.write_schema("launches", schema, "id")
    singer.write_records("launches", records)


def fetch_rockets() -> None:
    url: str = get_api_url("rockets")
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


def main() -> None:
    fetch_launches()
    fetch_rockets()


if __name__ == "__main__":
    main()
