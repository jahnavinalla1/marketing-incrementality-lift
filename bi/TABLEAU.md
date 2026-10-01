# Tableau dashboard build guide

Status: CSV exports and exact build specifications supplied; no Tableau workbook has been created or published. Build these in Tableau Desktop/Public after regenerating data. Every workbook title must include “Synthetic portfolio study.”

## 02 — Incrementality

Connect `outputs/arm_summary.csv` and `outputs/lift_estimates.csv` as **separate sources**, not a physical join. Plot arm conversion rates and assignment counts. For the one-row lift source, use MIN(absolute_lift) and MIN(ci95_lower/upper) as a point and interval; show relative lift, incremental CAC, SRM p-value and primary p-value in a text table. Do not average or sum interval bounds across studies. Format lift as percentage points by multiplying rates by 100. Tooltip: intent-to-treat, 28-day fixed horizon, 95% normal interval, synthetic experiment. Reconcile all values with `results.json`.

## Validation before publishing

Check each dashboard's full-data totals, one filtered slice, zero-denominator behavior, field types, tooltips, and synthetic-data disclosure. Export a screenshot, retain the `.twb`/`.twbx`, and add a real Tableau Public URL only after publishing. Never place real customer IDs in a public workbook.
