# SpaceX Missions Data Pipeline

This is the code behind my free email data engineering course.

Want to learn more?

https://datagibberish.com/p/free-data-engineering-course

## Run

This is an opinionated setup. You might not need to do it the way I do.
We use a single virtual environment to keep track of all the dependencies.

The only requirement to run this project is uv.
To install uv, run:

```sh
brew install uv
uv sync
```

## Running Scripts

To run Python scripts, run:

```sh
uv run -- src/<script>.py
```

## Running the pipeline

Edit the config.json file to include your snowflake credentials.
Then run:


```sh
uv run -- python src/tap_spacex.py | uv run -- target-snowflake
```

## Running dbt

Run:

```sh
cd dbt
uv run -- dbt run
```
