select * from dbt_spacex.launches;

select *
from dbt_spacex.launches
where success = true;

select *
from dbt_spacex.launches
order by launch_date desc;