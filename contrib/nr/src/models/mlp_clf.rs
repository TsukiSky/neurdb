use serde_json::json;
use std::collections::HashMap;
use crate::bindings::python_interface::{PY_MODULE, run_python_function};
use crate::utils::io::send_request;
use std::time::Instant;
// use shared_memory::*;
// use std::ffi::c_long;
// use pgrx::prelude::*;

/// Perform regression using the specified columns, table, and condition.
/// This function calls a Python function to perform the regression and returns the results.
///
/// # Arguments
/// * `columns` - The columns in the SQL.
/// * `table` - The table in the SQL.
/// * `condition` - The WHERE condition in the SQL.
/// * `config_file` - The path to the ML configuration file.
///
/// # Returns
/// A JSON value containing the results of the mlp_clf.
pub fn mlp_clf(
    columns: &String,
    table: &String,
    condition: &String,
    config_file: &String,
) -> serde_json::Value {
    let mut response = HashMap::new();
    let overall_start_time = Instant::now();

    // Step 1: Prepare task map for the Python function
    let mut task_map = HashMap::new();
    task_map.insert("where_cond", condition.to_string());
    task_map.insert("table", table.to_string());
    task_map.insert("label", columns.to_string());
    task_map.insert("config_file", config_file.clone());

    // Convert task map to JSON string
    let task_json = json!(task_map).to_string();

    // Call the Python function to perform regression
    // let eva_results = run_python_function(&PY_MODULE, &task_json, "mlp_clf");
    // Call the send_request function to perform the HTTP request
    let eva_results = send_request("http://localhost:8090/mlp_clf", &task_json);

    // Measure the time taken for the entire process
    let _end_time = Instant::now();
    let model_init_time = _end_time.duration_since(overall_start_time).as_secs_f64();

    // Prepare the response with results and metadata
    response.insert("time_usage", model_init_time.to_string());

    match eva_results {
        Ok(result) => {
            response.insert("result", result);
        }
        Err(e) => {
            response.insert("error", e.to_string());
        }
    }

    response.insert("table", table.to_string());
    response.insert("columns", columns.to_string());
    response.insert("condition", condition.to_string());

    // Return the response as JSON
    serde_json::json!(response)
}
