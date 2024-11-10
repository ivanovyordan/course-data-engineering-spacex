select * from dbt_spacex.launches;

select *
from dbt_spacex.launches
where success = true;

select *
from dbt_spacex.launches
order by launch_date desc;

select
    rocket,
    count(*) as launch_count
from dbt_spacex.launches
group by rocket;

select
    rocket,
    avg(
        case
            when success = true then 1
            else 0
        end
    ) as success_rate
from dbt_spacex.launches
group by rocket;

select
    year(launch_date) as launch_year,
    count(*) as launches_number
from dbt_spacex.launches
group by launch_year;