view: experiment_arms {
  sql_table_name: analytics.experiment_arms ;;
  dimension: arm { primary_key: yes type: string sql: ${TABLE}.arm ;; }
  measure: assigned_users { type: sum sql: ${TABLE}.assigned_users ;; }
  measure: exposed_users { type: sum sql: ${TABLE}.exposed_users ;; }
  measure: conversions { type: sum sql: ${TABLE}.conversions ;; }
  measure: conversion_rate { type: number sql: 1.0 * ${conversions} / NULLIF(${assigned_users},0) ;; value_format_name: percent_2 }
}
