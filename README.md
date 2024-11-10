# SpaceX Missions Data Pipeline

This is the code behind my free email data engineering course.

Want to learn more?

https://datagibberish.com/p/free-data-engineering-course

## Run

This is an opinionated setup. You might not need to do it the way I do.
Each folder has a separate virtual requirements and virtoal environment.
This helps us keep the dependencies separate.

The only requirement to run this project is uv.
To install uv, run:

```sh
brew install uv
```

## Intro Scripts

To run the intro scripts, run:

```sh
cd intro
uv sync
uv run -- <script.py>
```

## Tap

Our tap lives in tap-spacex.
To set that up run:

```sh
cd tap-spacex
uv sync
uv run -- python tap_sapcex.py
```

## Target

Our tap lives in tap-spacex.
To set that up run:

```sh
cd tap-spacex
uv sync
```

## Running the pipeline

To run the data integration pipeline run:

```sh
cd target-snowflake
cp sample.config.json config.json
```

Edit the config.json file to include your snowflake credentials.
Then run:

```sh
bash pipeline.sh
```
