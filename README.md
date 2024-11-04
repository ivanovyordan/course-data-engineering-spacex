# SpaceX Missions Data Pipeline

This is the code behind my free email data engineering course.

Want to learn more?

https://datagibberish.com/p/free-data-engineering-course

## Run

This is an opinionated setup. You might not need to do it the way I do.

### Step #1: Install UV

Install the uv package manager.

```sh
brew install uv
```

### Step #2: Install Dependencies

Install most dependencies. Target Snowflake is a bit different. It's much easier
to keep it in a separate virtual environment.

```sh
uv sync
```

### Step #3: Setup Target Snowflake

````sh
uv tool install meltanolabs-target-snowflake
```

### Step #4: Run

```sh
python tap-spacex/tap_spacex.py | target-snowflake
````
