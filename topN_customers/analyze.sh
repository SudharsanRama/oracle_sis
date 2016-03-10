#!/bin/bash
cat Porto_taxi_data_test_partial_trajectories.csv | ./mapper.py | ./reducer.py

