# Paid Social Incrementality & Lift

Independent, AI-assisted marketing analytics project using **synthetic data** for a fictional fitness subscription business. Findings are simulated and do not represent real campaign results.

![Results preview](outputs/preview.svg)

## Business question

Measure additional acquisitions caused by a simulated randomized paid-social holdout.

## Review the result

- [Decision brief](outputs/decision-brief.md): computed findings and business recommendations.
- [Interactive dashboard source](outputs/dashboard.html): download and open locally for charts, view selection, row search, metric selection, and CSV export. GitHub shows HTML source rather than running it.
- [SQL analysis](analysis.sql) and [Python pipeline](run.py).
- [Looker source and setup](bi/README.md), plus [Tableau build guide](bi/TABLEAU.md).

## Run locally

Requires Python 3.10+; **no packages, API keys or paid accounts are needed**.

```bash
git clone https://github.com/jahnavinalla1/marketing-incrementality-lift.git
cd marketing-incrementality-lift
python3 run.py
python3 -m unittest discover -s tests -v
```

Open `outputs/dashboard.html` in your browser. Generated data CSVs and the SQLite database are excluded from Git and rebuilt with a fixed seed. Committed output CSVs can be inspected immediately.

## Computed findings — simulated data

- Advance to a limited replication test. Treatment versus control is evaluated by original assignment, including unexposed treatment users.
- The estimated 33.3% relative lift has a two-sided p-value of 3.02e-10; sample-ratio mismatch p=0.215.
- A planning baseline of 4% and a 1 percentage-point minimum detectable effect requires approximately 6,746 users per arm at 80% power. This simulated study has about 20,000 per arm.
- Recommend that the analyst, media buyer, and measurement partner agree on holdout exclusions and a fixed decision date before launch. This is a proposed collaboration workflow.

## Deliverables and status

| Deliverable | Status |
|---|---|
| Reproducible SQL/Python analysis | Executable and locally tested |
| Offline interactive dashboard | Generated with embedded computed data |
| Data-quality / numerical tests | See [validation record](VALIDATION.md) |
| Native LookML model, view, dashboard source | Supplied; needs warehouse connection and tenant validation |
| Tableau calculated fields and layout instructions | Supplied; workbook not built or published |
| Business recommendations | Hypothetical; no media spend executed |

The HTML report is the working dashboard. The repository does **not** claim a deployed Looker or Tableau dashboard. LookML is for Looker, not Looker Studio.

## Methods and tools

SQL, marketing measurement, visualization, analytical problem solving, explicit assumptions, business recommendations, and quality-checked AI assistance.

Read [data contracts](DATA-DICTIONARY.md), [AI assistance](AI-ASSISTANCE.md), and [review questions](REVIEW-GUIDE.md).

## Related independent repositories

- [Paid Media Performance & Acquisition](https://github.com/jahnavinalla1/paid-media-performance-analytics)
- [Marketing Investment & Budget Allocation](https://github.com/jahnavinalla1/marketing-budget-optimization)
- [Trusted Marketing Data & Reporting](https://github.com/jahnavinalla1/marketing-data-quality-reporting)
