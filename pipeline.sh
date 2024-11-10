#!/bin/bash

mkfifo tap_output.pipe

# Activate the tap-spacex environment and run the tap
source tap-spacex/.venv/bin/activate
python tap-spacex/tap_spacex.py > tap_output.pipe &

# Deactivate the tap environment
deactivate

# Activate the target-snowflake environment and run the target with config
source target-snowflake/.venv/bin/activate
target-snowflake --config=target-snowflake/config.json < tap_output.pipe

# Deactivate the target environment
deactivate

# Clean up
rm tap_output.pipe