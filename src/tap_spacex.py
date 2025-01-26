import singer  # type: ignore
import pandas as pd
import numpy as np

from typing import List, Dict, Hashable, Any, TypedDict

LOGGER = singer.get_logger()


class LaunchProperties(TypedDict):
    id: str
    name: str
    rocket: str
    success: int
    date_utc: str


class Launch(TypedDict):
    properties: LaunchProperties


class RocketProperties(TypedDict):
    id: str
    name: str
    active: bool


class Rocket(TypedDict):
    properties: RocketProperties


def get_api_url(endpoint: str) -> str:
    return f"https://api.spacexdata.com/v4/{endpoint}"


def fetch_launches() -> None:
    url: str = get_api_url("launches")
    df: pd.DataFrame = pd.read_json(url)

    records: List[Dict[Hashable, Launch]] = df.to_dict(orient="records")
    schema: Dict[str, Dict[str, Any]] = {
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
    df: pd.DataFrame = pd.read_json(url)

    schema: Dict[str, Dict] = {
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "active": {"type": "boolean"},
        }
    }

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    records: List[Dict[Hashable, Rocket]] = df.to_dict(orient="records")

    singer.write_schema("rockets", schema, "id")
    singer.write_records("rockets", records)


def main() -> None:
    fetch_launches()
    fetch_rockets()


if __name__ == "__main__":
    main()
