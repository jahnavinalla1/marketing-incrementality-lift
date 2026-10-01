# Data contracts and metric definitions

All records are synthetic. Seeds 41, 52, 63, and 74 regenerate the four respective datasets. No personal data, WHOOP data, scraped ad accounts, or API credentials are used.

## Project 02 — incrementality

`experiment_users.csv`: one record for each of 40,000 synthetic assigned users. `arm` is a Bernoulli 50/50 randomized assignment; realized arm sizes can differ. `exposed` records simulated reach (80% in treatment; zero in control). `converted` is a binary 28-day outcome; `net_revenue_usd` is 136.8 per conversion. The simulated probability is 4% without exposure, 5.5% with exposure. No interference is modeled.

ITT lift Δ = treatment conversions / treatment assignments − control conversions / control assignments. Relative lift = Δ / control rate. Incremental members in the treatment population = Δ × treatment assignments. iCAC = 12,000 / incremental members, only when incremental members > 0. The two-sided 95% interval uses the unpooled normal standard error; the two-sided p-value uses the pooled null standard error. SRM compares observed assignments against the planned 50/50 allocation with a one-degree chi-square tail. Validity threshold for SRM: p ≥ .01. The primary endpoint uses α=.05 at a fixed horizon; subgroup exploration would need multiplicity control.
