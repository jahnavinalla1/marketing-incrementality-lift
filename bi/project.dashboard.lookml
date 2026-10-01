- dashboard: experiment_arms_portfolio
  title: "Paid Social Incrementality & Lift — Synthetic Data"
  layout: newspaper
  preferred_viewer: dashboards-next
  elements:
  - name: primary_view
    title: "Paid Social Incrementality & Lift"
    model: marketing
    explore: experiment_arms
    type: looker_column
    fields: [experiment_arms.arm, experiment_arms.conversion_rate]
    row: 0
    col: 0
    width: 24
    height: 10
