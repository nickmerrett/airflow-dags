from airflow_monitor.monitor_as_dag import get_monitor_dag
## This DAG is used by Databand to monitor your Airflow installation.

dag = get_monitor_dag(check_interval=2, monitor_env={"CURL_CA_BUNDLE": ""})

if __name__ == "__main__":
    dag.cli()
