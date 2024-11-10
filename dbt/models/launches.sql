select
    id,
    name,
    date(to_timestamp(date_utc)) as launch_date,
    success,
    rocket

from {{ source('public', 'launches') }}