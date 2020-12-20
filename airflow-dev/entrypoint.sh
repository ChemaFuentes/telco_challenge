#!/usr/bin/env bash

set -eu

echo "Starting airflow"

echo "Airflow: initdb"

airflow initdb

echo "Airflow: scheduler"

airflow scheduler &

echo "Airflow: webserver"

airflow webserver -p 8080
