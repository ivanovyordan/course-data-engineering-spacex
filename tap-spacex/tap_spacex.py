import singer
import pandas as pd
import numpy as np

LOGGER = singer.get_logger()

schema = {
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "date_utc": {"type": "string", "format": "date-time"},
        # Add other fields as needed
    }
}


def main():
    url = "https://api.spacexdata.com/v4/launches"
    df = pd.read_json(url)

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    records = df.to_dict(orient="records")

    singer.write_schema("launches", schema, "id")
    singer.write_records("launches", records)


if __name__ == "__main__":
    main()
