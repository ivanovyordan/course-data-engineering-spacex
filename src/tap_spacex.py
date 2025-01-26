from dataclasses import dataclass

import singer  # type: ignore
import pandas as pd
import numpy as np

from typing import List, Dict, Hashable, Any, TypedDict, Optional

LOGGER = singer.get_logger()


@dataclass
class LaunchProperties:
    id: str
    name: str
    rocket: str
    success: int
    date_utc: str


class Launch(TypedDict):
    properties: LaunchProperties


@dataclass
class RocketProperties:
    id: str
    name: str
    active: bool
    payloads: Optional[List[Dict]]


class Rocket(TypedDict):
    properties: RocketProperties


def get_api_url(endpoint: str) -> str:
    return f"https://api.spacexdata.com/v4/{endpoint}"


def fetch_records(endpoint: str) -> List[Dict[Hashable, Launch | Rocket]]:
    url: str = get_api_url(endpoint)
    df: pd.DataFrame = pd.read_json(url)

    df = df.replace({np.nan: None})
    records: List[Dict[Hashable, Launch | Rocket]] = df.to_dict(orient="records")

    return records


def fetch_launches() -> None:
    records = fetch_records("launches")

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
    records = fetch_records("rockets")

    schema: Dict[str, Dict] = {
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "active": {"type": "boolean"},
        }
    }

    singer.write_schema("rockets", schema, "id")
    singer.write_records("rockets", records)


def main() -> None:
    fetch_launches()
    fetch_rockets()


if __name__ == "__main__":
    main()
