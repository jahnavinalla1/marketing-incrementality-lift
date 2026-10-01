-- Intent-to-treat analysis includes everyone assigned, whether exposed or not.
SELECT arm, COUNT(*) AS assigned_users, SUM(exposed) AS exposed_users,
 SUM(converted) AS conversions, 1.0*SUM(converted)/COUNT(*) AS conversion_rate,
 SUM(net_revenue_usd) AS net_revenue_usd
FROM experiment_users GROUP BY arm ORDER BY arm;
