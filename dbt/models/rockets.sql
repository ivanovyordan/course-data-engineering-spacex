select
    id,
    name,
    active

from {{ source('public', 'rockets') }}