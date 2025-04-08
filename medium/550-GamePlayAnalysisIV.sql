SELECT 
ROUND(
(
    SELECT COUNT(DISTINCT initial.player_id)
    FROM Activity AS initial
    INNER JOIN Activity AS day2 ON day2.event_date = initial.event_date + 1
    WHERE initial.player_id = day2.player_id
    AND initial.event_date IN (
        SELECT MIN(event_date)
        FROM Activity
        WHERE player_id = initial.player_id
    )
)::decimal
/
(
    SELECT COUNT(DISTINCT player_id)
    FROM Activity
)::decimal
,2
)
AS fraction;